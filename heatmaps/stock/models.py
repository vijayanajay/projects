from django.db import models
from django.core.validators import MinLengthValidator


class Stock(models.Model):
    """Model for individual stock information."""

    symbol = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(1)],
        help_text="Stock symbol (e.g., RELIANCE, TCS)",
    )
    name = models.CharField(max_length=100, help_text="Full company name")
    sector = models.CharField(
        max_length=50, help_text="Industry sector of the stock"
    )
    is_nifty50 = models.BooleanField(
        default=False, help_text="Whether the stock is part of Nifty 50 index"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["symbol"]
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"{self.symbol} - {self.name}"


class PriceHistory(models.Model):
    """Model for storing stock price history."""

    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name="price_history"
    )
    date = models.DateField(help_text="Date of the price data")
    open_price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Opening price"
    )
    high_price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Highest price of the day"
    )
    low_price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Lowest price of the day"
    )
    close_price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Closing price"
    )
    volume = models.BigIntegerField(help_text="Trading volume")

    class Meta:
        ordering = ["-date"]
        verbose_name = "Price History"
        verbose_name_plural = "Price Histories"
        unique_together = ["stock", "date"]

    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"
