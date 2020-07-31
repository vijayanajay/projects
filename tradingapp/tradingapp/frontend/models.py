from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
import pytz
from django_pandas.managers import DataFrameManager
import pandas as pd
import talib

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
        elif datetime.datetime.now(tz) > self.last_updated_date:
            return "Refresh?"
        else:
            return None

    def update_daily_stats(self):
        start_date = DailyStockStats.objects.filter(company__id=self.id).order_by('date').dates('date', 'day').last()
        if start_date == None:
            price_data = DailyPrice.objects.filter(company__id=self.id)
            start_date = price_data.order_by('date').dates('date', 'day').first()
        else:
            price_data = DailyPrice.objects.filter(company__id=self.id, date__gte=start_date)
        price_data = price_data.to_dataframe()
        price_data['date'] = price_data['date'].dt.date
        end_date = price_data.date.max()

        df = pd.DataFrame()
        while start_date <= end_date:
            df = price_data[price_data['date'] == start_date]
            if len(df) > 0:
                mean = df.close_price.mean()
                day_high = df.close_price.max()
                day_low = df.close_price.min()
                std_dev = df.close_price.std()
                rsi = talib.RSI(df.close_price, 14)
                macd, macdsignal, macdhist = talib.MACD(df.close_price, 12, 26, 9)
                slowk, slowd = talib.STOCH(df.high_price, df.low_price, df.close_price)
                roc = talib.ROC(df.close_price, 20)
                willr = talib.WILLR(df.high_price, df.low_price, df.close_price)
                mfi = talib.MFI(df.high_price, df.low_price, df.close_price, df.volume, 14)
                atr = talib.ATR(df.high_price, df.low_price, df.close_price, 14)
                adx = talib.ADX(df.high_price, df.low_price, df.close_price, 14)
                upperband, middleband, lowerband = talib.BBANDS(df.close_price)
            start_date = start_date + datetime.timedelta(days=1)

        debuginfo = upperband
        return debuginfo


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


class DailyPrice(models.Model):
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


class WeeklyPrice(models.Model):
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


