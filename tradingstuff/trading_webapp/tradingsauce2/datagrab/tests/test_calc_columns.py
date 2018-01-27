from django.test import TestCase
import random
import string
import factory
from datagrab.models import StockSymbol, StockHistory
import datagrab.utils as ut
from django.db import transaction


class StockSymbolFactory(factory.DjangoModelFactory):
    class Meta:
        model = StockSymbol
        abstract = False

    name = factory.LazyAttribute(lambda t: random_text(length=50))
    symbol = factory.LazyAttribute(lambda t: random_text(length=10))
    tickerNumber = factory.LazyAttribute(lambda t: random_number(length=6))

class CalculatedColumns(TestCase):

        def setUp(self):
            stock = StockSymbolFactory.create(name='ASHOK Leyland',
                                              symbol='ASHOKLEY', tickerNumber='500477')
            stock.save()
            self.assertEquals(StockSymbol.objects.count(), 1)
            csv_filename = ut.get_csv_filename(stock)
            try:
                with transaction.atomic():
                    count = ut.read_csv_file(stock, csv_filename)
            except:
                self.fail("exception when trying to insert")

        def test_calculated_sma3_is_correct(self):
            stock = StockSymbol.objects.get(tickerNumber='500477')
            ut.calculate_and_store_sma3(stock)
            lastRecord = StockHistory.objects.all().order_by('-id')[:6]
            self.assertAlmostEqual(lastRecord[5].sma3, 52.9333333)
            self.assertAlmostEqual(lastRecord[4].sma3, 52.5333333)
            self.assertAlmostEqual(lastRecord[3].sma3, 51.96666666)
            self.assertAlmostEqual(lastRecord[2].sma3, 51.8333333)
            self.assertAlmostEqual(lastRecord[1].sma3, 51.8333333)

        def test_calculated_daily_returns_is_correct(self):
            stock = StockSymbol.objects.get(tickerNumber='500477')
            ut.calculate_and_store_daily_returns(stock)
            lastRecord = StockHistory.objects.all().order_by('-id')[:6]
            self.assertAlmostEqual(lastRecord[5].dailyReturns * 1000, -7.511737089)
            self.assertAlmostEqual(lastRecord[4].dailyReturns * 1000, 10.43643264)
            self.assertAlmostEqual(lastRecord[3].dailyReturns * 1000, 20.32913843)
            self.assertAlmostEqual(lastRecord[2].dailyReturns * 1000, 1.93986421)
            self.assertAlmostEqual(lastRecord[1].dailyReturns * 1000, -14.34034417)

