# _*_ coding: utf-8 _*_
from django.forms import Form, fields, widgets

_author_ = 'Ace'
_date_ = '2019-02-02 18:12'

class ProcessMaker(Form):
    title = fields.CharField(
        max_length=32,
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    detail = fields.CharField(
        widget=widgets.Textarea(attrs={'id':'detail','class':'kind-content'})
    )
