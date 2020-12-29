from django import forms
from .models import WebsiteData


class WebsiteForm(forms.ModelForm):

    class Meta:
        model = WebsiteData
        fields = ('url', )
