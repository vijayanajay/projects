from django.test import TestCase
#import pytest
import random
import string
import factory
from datagrab.models import StockSymbol, StockHistory

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
        assert str(stock), 'ASHOK Leyland'
        
    
        
        
# Create your tests here.
