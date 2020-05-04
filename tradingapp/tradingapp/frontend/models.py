from django.db import models
from datetime import datetime

class Company(models.Model):
    name = models.CharField(max_length=200)
    bom_id = models.CharField(max_length = 20, 
                              unique=True, null=False)
    last_updated_date = models.DateField(null=True)

    def __str__(self):
        return self.name + "/" + self.bom_id

    def update_status(self):
        if self.last_updated_date is None:
            return ("Never Updated. Refresh ?")
        else:
            return (self.last_updated_date)
           
class Price(models.Model):
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

    company = models.ForeignKey(
        'Company',
        on_delete = models.CASCADE)

    class Meta:
        unique_together = ['company', 'date']
               
    def __str__(self):
        return (self.company.bom_id + " " + self.date.strftime("%m/%d/%Y") + " " + str(self.open_price))
