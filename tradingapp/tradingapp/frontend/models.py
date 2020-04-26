from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    bom_id = models.CharField(unique=True, null=False)

    def __str__(self):
        return self.name + "/" + bom_id
    
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
    rsi = models.FloatField()
    sma_periodSmall = models.FloatField()
    sma_periodBig = models.FloatField()

    bom_id = models.ForeignKey(
        'Company',
        on_delete = models.CASCADE)

    class Meta:
        unique_together = ['bom_id', 'date']
               
    def __str__(self):
        return self.bom_id + " " + self.date + " " + self.open_price