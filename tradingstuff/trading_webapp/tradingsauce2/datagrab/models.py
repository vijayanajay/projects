from django.db import models

# Create your models here.
class StockSymbol(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    tickerNumber = models.IntegerField()

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    symbol = models.ForeignKey(StockSymbol,
                               on_delete=models.CASCADE,
                               )
    date = models.DateTimeField()
    openPrice = models.FloatField(null = True)
    highPrice = models.FloatField(null = True)
    lowPrice = models.FloatField(null = True)
    closePrice = models.FloatField(null = True)
    wap = models.FloatField(null = True)
    numberOfShares = models.IntegerField(null = True)
    numberOfTrades = models.IntegerField(null = True)
    totalTurnover = models.FloatField(null = True)
    spreadHighLow = models.FloatField(null = True)
    spreadCloseOpen = models.FloatField(null = True)
    dailyReturns = models.FloatField(null = True)
    rsi3 = models.FloatField(null = True)
    sma3 = models.FloatField(null = True)

    def __str__(self):
        return u'%s %s' % (self.symbol)




# Create your models here.
