from django.test import TestCase
import random
import string
import factory
from datagrab.models import StockSymbol, StockHistory
from django.test import Client
from django.core.urlresolvers import reverse
import datagrab.utils as ut
import os
from django.db import transaction

def random_text(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))

def random_number(length=6):
    return u''.join(random.choice(string.digits) for x in range(length))


class StockSymbolFactory(factory.DjangoModelFactory):
    class Meta:
        model = StockSymbol
        abstract = False
    
    name = factory.LazyAttribute(lambda t: random_text(length = 50))
    symbol = factory.LazyAttribute(lambda t: random_text(length = 10))
    tickerNumber = factory.LazyAttribute(lambda t: random_number(length = 6))
    
    
class DataGrab(TestCase):
    
    def test_stocksymbol_stringrepresentation(self):
        stock = StockSymbolFactory.create(name = 'ASHOK Leyland', 
                                           symbol = 'ASHOKLEY',
                                           tickerNumber = '500477')
        stock = StockSymbol.objects.get(tickerNumber = '500477')
        self.assertEqual(str(stock), 'ASHOK Leyland')
        
    def test_derived_csv_filename_is_correct(self):
        stock = StockSymbolFactory.create(name = 'ASHOK Leyland', 
                                           symbol = 'ASHOKLEY',
                                           tickerNumber = '500477')
        csv_filename = ut.get_csv_filename(stock) 
        #real_filename = os.path.dirname(os.path.realpath(__file__))
        real_filename = os.getcwd()
        real_filename = os.path.join(real_filename, 'datagrab',
                                     'csvData', '500477.csv')
        print (real_filename)
        self.assertEqual (csv_filename, real_filename)
                      
    def test_derived_csv_filename_is_found_and_opened(self):
        stock = StockSymbolFactory.create(name = 'ASHOK Leyland', 
                                           symbol = 'ASHOKLEY',
                                           tickerNumber = '500477')
        csv_filename = ut.get_csv_filename(stock)
        try:
            file = open (csv_filename, 'r')
        except Exception as e:
             template = "An exception of type {0} occurred. Arguments:\n{1!r}"
             message = template.format(type(e).__name__, e.args)
             self.fail(message)             
    
    def test_derived_csv_filename_is_not_found_returns_no_issue(self):
        stock = StockSymbolFactory.create()
        csv_filename = ut.get_csv_filename(stock)
        csv_file = ut.read_csv_file(stock, csv_filename)
        self.assertEqual(csv_file, False)

    def test_derived_csv_filename_is_found(self):
        stock = StockSymbolFactory.create(name='ASHOK Leyland',
                                          symbol='ASHOKLEY', tickerNumber='500477')
        csv_filename = ut.get_csv_filename(stock)
        csv_file = ut.read_csv_file(stock, csv_filename)
        self.assertNotEquals(csv_file, False)

    def test_csv_file_import_to_StockHistory(self):
        stock = StockSymbolFactory.create(name = 'ASHOK Leyland',
                                           symbol = 'ASHOKLEY', tickerNumber = '500477')
        stock.save()
        self.assertEquals(StockSymbol.objects.count(),1)
        csv_filename = ut.get_csv_filename(stock)
        try:
            with transaction.atomic():
                count = ut.read_csv_file(stock, csv_filename)
        except:
            self.fail("exception when trying to insert")
        #count = StockHistory.objects.count()
        self.assertGreater(StockHistory.objects.count(), 1)
        lastRecord = StockHistory.objects.all().last()
        self.assertEquals(lastRecord.openPrice, 50.5)
        self.assertEquals(lastRecord.highPrice, 52.6)
        self.assertEquals(lastRecord.lowPrice, 50.0)
        self.assertEquals(lastRecord.closePrice, 52.3)
        self.assertEquals(lastRecord.wap, 51.723125410140653536)
        self.assertEquals(lastRecord.numberOfShares, 3035544)
        self.assertEquals(lastRecord.numberOfTrades, 8128)
        self.assertEquals(lastRecord.totalTurnover, 157007823)
        self.assertEquals(lastRecord.spreadHighLow, 2.60)
        self.assertEquals(lastRecord.spreadCloseOpen, 1.80)

    def test_calculated_sma3_is_correct(self):
        stock = StockSymbolFactory.create(name = 'ASHOK Leyland',
                                           symbol = 'ASHOKLEY', tickerNumber = '500477')
        stock.save()
        self.assertEquals(StockSymbol.objects.count(),1)
        csv_filename = ut.get_csv_filename(stock)
        try:
            with transaction.atomic():
                count = ut.read_csv_file(stock, csv_filename)
        except:
            self.fail("exception when trying to insert")
        ut.calculate_and_store_sma3(stock)
        lastRecord = StockHistory.objects.all().order_by('-id')[:6]
        self.assertEquals(lastRecord[5].sma3, 0)

    def test_same_data_is_not_inserted_into_db(self):
        stock = StockSymbolFactory.create(name='ASHOK Leyland',
                                          symbol='ASHOKLEY', tickerNumber='500477')
        stock.save()
        self.assertEquals(StockSymbol.objects.count(), 1)
        csv_filename = ut.get_csv_filename(stock)
        #first insert
        try:
            with transaction.atomic():
                count = ut.read_csv_file(stock, csv_filename)
        except:
            self.fail("exception when trying to insert")
        self.assertEquals(StockHistory.objects.count(), 1854)

        # second insert
        try:
            with transaction.atomic():
                count = ut.read_csv_file(stock, csv_filename)
        except:
            self.fail("exception when trying to insert")
        self.assertEquals(StockHistory.objects.count(), 1854)






