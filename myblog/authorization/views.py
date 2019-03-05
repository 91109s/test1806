from typing import Dict, Any, Union

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from utils.response import wrap_json_response,ReturnCode

def test_session(request):
    print("ok")
    request.session['message'] = 123
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)
    #return JsonResponse(data='jdhfh',safe=False)
#获取cookie
def test_getCooice(requset):
    print('session content: ', requset.session.items())
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)