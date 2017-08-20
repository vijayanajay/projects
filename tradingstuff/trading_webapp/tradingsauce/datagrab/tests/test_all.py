from django.test import TestCase
import random
import string
import factory
from datagrab.models import StockSymbol, StockHistory
from django.test import Client
from django.core.urlresolvers import reverse
import datagrab.utils as ut
import os

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
    
    def test_derived_csv_filename_is_not_found(self):
        stock = StockSymbolFactory.create()
        csv_filename = ut.get_csv_filename(stock)
        csv_file = ut.read_csv_file(csv_filename)
        self.assertEqual(csv_file, False)
