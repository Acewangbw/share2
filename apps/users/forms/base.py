# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-29 14:28'

class BaseForm(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(BaseForm, self).__init__(*args, **kwargs)