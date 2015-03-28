from django.db import models

# Create your models here.
class Article(models.Model):

	site_name = models.CharField(max_length=30)
	title = models.CharField(max_length=256)
	content = models.CharField(max_length=1024)
	link = models.CharField(max_length=1024)

