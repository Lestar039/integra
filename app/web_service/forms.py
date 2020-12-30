from django import forms
from .models import DomainData, HostingData


class DomainForm(forms.ModelForm):
    url = forms.CharField(required=False, label='http://')
    ya_counter_number = forms.CharField(required=False, label='Yandex counter')
    expiration_date = forms.DateTimeField(required=False, label='Expiration date')

    class Meta:
        model = DomainData
        fields = ('url', 'ya_counter_number', 'expiration_date', 'hosting')


class HostingForm(forms.ModelForm):
    name = forms.CharField(required=False, label='Name')
    account = forms.CharField(required=False, label='Account login')
    expiration_date = forms.DateTimeField(required=False, label='Expiration date')

    class Meta:
        model = HostingData
        fields = ('name', 'account', 'expiration_date')
