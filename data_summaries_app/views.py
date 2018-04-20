import os,sys
sys.path.insert(1, os.path.join(sys.path[0], './scripts'))

from django.http import HttpResponse
from scripts import pretend_i_am_data_summary_script


def callScript():
    return pretend_i_am_data_summary_script.summary()

def homePageView(request):
    return HttpResponse(callScript())
