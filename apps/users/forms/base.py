# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-29 14:28'
'''
这里是复杂别人博客项目的，我做参考使用的。

'''
class BaseForm(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(BaseForm, self).__init__(*args, **kwargs)