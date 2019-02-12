# _*_ coding: utf-8 _*_
from django.http import HttpResponse
import json
_author_ = 'Ace'
_date_ = '2019-02-12 16:19'

from repository.models import AddFileModel


# def del_file(request):
#     file_id = request.POST['file_id']
#     try:
#         file = AddFileModel.objects.get(id=int(file_id))
#         file.delete()
#         return HttpResponse('1')
#     except:
#         return HttpResponse('2')

def del_file(request):
    ret = {'status': True}
    try:
        nid = request.GET.get('nid')
        print(nid,'Ace try to print nid by way2')
        AddFileModel.objects.filter(nid=nid).delete()
    except Exception as e:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))