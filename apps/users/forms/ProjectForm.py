# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-02-02 19:59'

from  django import forms


class ProjectForm(forms.Form):

    project = forms.CharField(required=True)
