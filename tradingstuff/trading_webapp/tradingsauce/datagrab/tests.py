from django.test import TestCase
from .models import StockSymbol, StockHistory

class DataGrab(TestCase):
    def setUp(self):
        someObject = StockSymbol.objects.create(name = 'ASHOK Leyland', 
                                           symbol = 'ASHOKLEY',
                                           tickerNumber = '500478')
    
    def test_stocksymbol_stringrepresentation(self):
        stock = StockSymbol.objects.create(name = 'ASHOK Leyland', 
                                           symbol = 'ASHOKLEY',
                                           tickerNumber = '500477')
        stock = StockSymbol.objects.get(tickerNumber = '500477')
        self.assertEqual(str(stock), 'ASHOK Leyland')
        
# Create your tests here.
