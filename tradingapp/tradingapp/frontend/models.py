from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
import pytz
from django_pandas.managers import DataFrameManager
import pandas as pd
import talib
import logging
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import HoverTool, DataRange1d
from plotly.offline import plot
import plotly.graph_objs as go

tz = pytz.timezone('Asia/Kolkata')
logger = logging.getLogger(__name__)
TOOLTIPS = [
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("desc", "@desc"),
        ]


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
        logger.debug("inside models.update_daily_stats")
        start_date = DailyStockStats.objects.filter(company__id=self.id).order_by('date').dates('date', 'day').last()
        logger.debug("intial start_date = " + str(start_date))
        if start_date == None:
            price_data = DailyPrice.objects.filter(company__id=self.id)
            start_date = price_data.order_by('date').dates('date',  'day').first() - datetime.timedelta(days=1)
            logger.debug("intial start_date when none = " + str(start_date))
        else:
            start_date = start_date + datetime.timedelta(days=1)
            price_data = DailyPrice.objects.filter(company__id=self.id,
                                                   date__gte=start_date - datetime.timedelta(days=40))
            logger.debug("intial start_date when already present = " + str(start_date))
        price_data = price_data.to_dataframe()
        debuginfo = self.insert_daily_stats_into_db(price_data, start_date, "daily")
        logger.debug("outside models.update_daily_stats")
        return debuginfo

    def update_weekly_stats(self):
        logger.debug("inside models.update_weekly_stats")
        start_date = DailyStockStats.objects.filter(company__id=self.id).order_by('date').dates('date', 'day').last()
        logger.debug("intial start_date = " + str(start_date))
        if start_date is None:
            price_data = DailyPrice.objects.filter(company__id=self.id)
            start_date = price_data.order_by('date').dates('date',  'day').first() - datetime.timedelta(days=1)
            logger.debug("intial start_date when none = " + str(start_date))
        else:
            start_date = start_date + datetime.timedelta(days=1)
            price_data = DailyPrice.objects.filter(company__id=self.id,
                                                   date__gte=start_date - datetime.timedelta(days=40))
            logger.debug("intial start_date when already present = " + str(start_date))
        price_data = price_data.to_dataframe()
        debuginfo = self.insert_daily_stats_into_db(price_data, start_date, "daily")
        logger.debug("outside models.update_weekly_stats")
        return debuginfo

    def insert_daily_stats_into_db(self, price_data, start_date, type):
        logger.debug("inside models.insert_daily_stats_into_db")
        logger.debug(" price_data['date'] = " + price_data['date'].to_json())
        end_date = price_data.date.max()
        logger.debug("end_date = "+str(end_date))

        df = pd.DataFrame()
        df['date'] = price_data.date
        df['company_id'] = self.id
        df['day_high'] = price_data.close_price.rolling(14).max()
        df['day_low'] = price_data.close_price.rolling(14).min()
        df['mean'] = price_data.close_price.rolling(14).mean()
        df['std_dev'] = price_data.close_price.rolling(14).std()
        df['rsi'] = talib.RSI(price_data.close_price, 14)
        df['macd'], macdsignal, macdhist = talib.MACD(price_data.close_price, 12, 26, 9)
        df['stochastic'], slowd = talib.STOCH(price_data.high_price, price_data.low_price, price_data.close_price)
        df['roc'] = talib.ROC(price_data.close_price, 20)
        df['willr'] = talib.WILLR(price_data.high_price, price_data.low_price, price_data.close_price)
        df['mfi'] = talib.MFI(price_data.high_price, price_data.low_price, price_data.close_price,
                              price_data.volume, 14)
        df['atr'] = talib.ATR(price_data.high_price, price_data.low_price, price_data.close_price, 14)
        df['adx'] = talib.ADX(price_data.high_price, price_data.low_price, price_data.close_price, 14)
        df['bol_high'], middleband, df['bol_low'] = talib.BBANDS(price_data.close_price)
        if type == 'daily':
            stat = pd.DataFrame()
        df = df[(df.date >= start_date) & (df.date <= end_date)]
        logger.debug("df data = "+ str(df.date))
        logger.debug("df len = " + str(len(df)))
        entries = []
        for e in df.T.to_dict().values():
            entries.append(DailyStockStats(**e))
        DailyStockStats.objects.bulk_create(entries, ignore_conflicts=True)
        debuginfo = str(start_date) + " end date = " + str(end_date)
        logger.debug("outside models.insert_daily_stats_into_db")
        return debuginfo

    def get_main_chart(self):
        logger.debug('inside models.get_main_chart')
        df = DailyPrice.objects.filter(company__id=self.id).values('date', 'close_price').to_dataframe()
        #logger.debug('df date type = ' + str(type(df.date[1])))
        #logger.debug('dt date = ' + str(df.date[:10]))
        df = df[-50:]
        title = "Last 50 data points"
        # ---- start of bokeh chart
        #plot = figure(title=title,
        #              x_axis_label='X-Axis',
        #              y_axis_label='Y-Axis',
        #              x_axis_type = 'datetime',
        #              plot_width=800,
        #              plot_height=400,
        #              toolbar_location='above',
        #              tools="pan,wheel_zoom,box_zoom,reset")
        #hover_tool = HoverTool(tooltips=[
        #    ('x','$df.date'),
        #    ('y', '$y'),
        #])
        #plot.tools.append(hover_tool)
        #plot.x_range = DataRange1d(range_padding=0.0)
        #plot.line(df.date, df.close_price, line_width=2)
        #return components(plot)
        # ---- end of bokeh chart

        fig = go.Figure()
        scatter = go.Scatter(x=df.date.values, y=df.close_price.values, mode='lines')
        fig.add_trace(scatter)
        plt_div = plot(fig, output_type='div', include_plotlyjs=False, 
                       show_link=False, link_text="")
        logger.debug('end of models.get_main_chart')
        return plt_div
        


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
    date = models.DateField(null=False)
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
    date = models.DateField(null=False)
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

    date = models.DateField(null=False)
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


class WeeklyStockStats(models.Model):
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE)

    date = models.DateField(null=False)
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
