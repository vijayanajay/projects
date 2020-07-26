from django import forms
from frontend.models import *


class SelectCompany(forms.Form):
    class Meta:
        model = Company
        fields = ['name', 'bom_id']
