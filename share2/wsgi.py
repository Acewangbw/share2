"""
WSGI config for share2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "share2.settings")
#
# application = get_wsgi_application()


import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
appPath = "c:/share" #new addting for developtment
sys.path.append(appPath)#new addting for developtment
application = get_wsgi_application()