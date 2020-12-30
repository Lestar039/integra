from django import forms
from .models import WebsiteData


class WebsiteForm(forms.ModelForm):
    url = forms.CharField(required=False, label='http://')
    ya_counter_number = forms.CharField(required=False, label='Yandex counter')
    expiration_date = forms.DateTimeField(required=False, label='Expiration date')

    class Meta:
        model = WebsiteData
        fields = ('url', 'ya_counter_number', 'expiration_date')
