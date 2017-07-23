from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location = settings.BASE_DIR + '/media/csvData')

# Create your models here.
class StockSymbol(models.Model):
    name =  models.CharField (max_length = 50)
    symbol = models.CharField (max_length = 10)
    tickerNumber = models.IntegerField()
    file = models.FileField(storage = fs, default = fs)
    
    def __str__(self):
       return self.name
    
class StockHistory(models.Model):
    symbol = models.ForeignKey (StockSymbol, 
                                on_delete = models.CASCADE,
                                )
    date = models.DateTimeField()
    openPrice = models.FloatField()
    highPrice = models.FloatField()
    lowPrice = models.FloatField()
    closePrice = models.FloatField()
    wap = models.FloatField()
    numberOfShares = models.IntegerField()
    numberOfTrades = models.IntegerField()
    totalTurnover = models.FloatField()
    spreadHighLow = models.FloatField()
    spreadCloseOpen = models.FloatField()
    
    def __str__(self):
        return u'%s %s' % (self.symbol)
    
