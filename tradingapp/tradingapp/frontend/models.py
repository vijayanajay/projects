from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=200)
    bom_id = models.CharField(max_length = 20, 
                              unique=True, null=False)
    last_updated_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name + "/" + self.bom_id

    def update_status(self):
        if self.last_updated_date is None:
            return ("Never Updated. Refresh ?")
        elif datetime.today().date()  > self.last_updated_date:
            return ("Refresh?")
        else:
            return (None)
           
class Price(models.Model):

    class Period (models.TextChoices):
        one_min = '1M', _('1minute')
        five_min = '5M', _('5minute')
        fifteen_min = '15M', _('15minute')
        thirty_min = '30M', _('30minute')
        one_day = '1D', _('1 Day')

    date = models.DateField(null=False)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    wap = models.FloatField()
    volume = models.PositiveIntegerField()
    trades = models.PositiveIntegerField()
    turnover = models.FloatField()
    deliverable_quantity = models.IntegerField()
    percent_del_traded_qty = models.FloatField()
    spread_highLow = models.FloatField()
    spread_closeOpen = models.FloatField()
    rsi = models.FloatField(null=True, blank=True)
    sma_periodSmall = models.FloatField(null=True, blank=True)
    sma_periodBig = models.FloatField(null=True, blank=True)
    period = models.CharField(max_length=3, choices=Period.choices,
                              default=Period.one_day)

    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ['company', 'date']

    def __str__(self):
        return (self.company.bom_id + " " + self.date.strftime("%m/%d/%Y") + " " + str(self.open_price))