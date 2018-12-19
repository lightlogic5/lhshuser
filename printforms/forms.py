from django import forms
from django.utils import timezone

from .models import PrintForm


# class PrintForm(forms.Form):
#     repair_man = forms.CharField(required=True)
#     unit = forms.CharField(required=True)
#     content = forms.CharField(required=True, min_length=5)
#     telephone = forms.CharField(required=True)


class MyPrintForm(forms.ModelForm):
    # repair_man = timezone.now()
    # pub_date = forms.DateTimeField(auto_now_add = True)

    class Meta:
        model = PrintForm
        fields = ['repair_man', 'unit', 'content', 'telephone', 'pub_date']
        # labels = {
        #     'pub_date': '2018-12-04 11:50:00',
        # }