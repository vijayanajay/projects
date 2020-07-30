from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
import pytz
from django_pandas.managers import DataFrameManager

tz = pytz.timezone('Asia/Kolkata')


class Company(models.Model):
    name = models.CharField(max_length=200)
    bom_id = models.CharField(max_length=20,
                              unique=True, null=False)
    yahoo_id = models.CharField(max_length=20, unique=True,
                                null=True, blank=True)
    last_updated_date = models.DateTimeField(null=True, blank=True)

    objects = DataFrameManager()

    def __str__(self):
        return self.name + "/" + self.bom_id

    def update_status(self):
        if self.last_updated_date is None:
            return "Never Updated. Refresh ?"
        elif datetime.now(tz) > self.last_updated_date:
            return "Refresh?"
        else:
            return None


class IntradayPrice(models.Model):
    date = models.DateTimeField(null=False)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    wap = models.FloatField(null=True, blank=True)
    volume = models.PositiveIntegerField(null=True, blank=True)
    trades = models.PositiveIntegerField(null=True, blank=True)
    turnover = models.FloatField(null=True, blank=True)
    deliverable_quantity = models.IntegerField(null=True, blank=True)
    percent_del_traded_qty = models.FloatField(null=True, blank=True)
    spread_highLow = models.FloatField(null=True, blank=True)
    spread_closeOpen = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE)

    objects = DataFrameManager()

    class Meta:
        unique_together = ['company', 'date']

    def __str__(self):
        return (self.company.bom_id + " " + self.date.strftime("%m/%d/%Y") + " " + str(self.open_price))


class DailyStockStats(models.Model):
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE)

    date = models.DateTimeField(null=False)
    day_high = models.FloatField(null=True, blank=True)
    day_low = models.FloatField(null=True, blank=True)
    mean = models.FloatField(null=True, blank=True)
    std_dev = models.FloatField(null=True, blank=True)
    rsi = models.FloatField(null=True, blank=True)
    macd = models.FloatField(null=True, blank=True)
    stochastic = models.FloatField(null=True, blank=True)
    roc = models.FloatField(null=True, blank=True)
    willr = models.FloatField(null=True, blank=True)
    mfi = models.FloatField(null=True, blank=True)
    atr = models.FloatField(null=True, blank=True)
    adx = models.FloatField(null=True, blank=True)
    bol_high = models.FloatField(null=True, blank=True)
    bol_low = models.FloatField(null=True, blank=True)
    sma_5 = models.FloatField(null=True, blank=True)
    sma_10 = models.FloatField(null=True, blank=True)
    sma_20 = models.FloatField(null=True, blank=True)
    sma_50 = models.FloatField(null=True, blank=True)
    sma_100 = models.FloatField(null=True, blank=True)
    sma_200 = models.FloatField(null=True, blank=True)

    objects = DataFrameManager()

    class Meta:
        unique_together = ['company', 'date']
