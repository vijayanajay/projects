from django.contrib import admin

# Register your models here.
from getopinions.models import *
from django.contrib import admin

class ArticleAdmin (admin.ModelAdmin):
	list_display = ['site_name', 'title', 'content', 'link']

admin.site.register(Article, ArticleAdmin)