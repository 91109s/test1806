from django.http import HttpResponse,JsonResponse,FileResponse
from blog.weatheRequest import juheWeather
import json
def helloworld(request):
    print('request method: ',request.method)
    #print('request Meta: ',request.META)
    print('request cookies: ',request.COOKIES)
    print('request QueryDict: ',request.GET) #获取请求参数
    #return HttpResponse(content="request ok",status=200)
    message={"message":"hello Django Response"}
    return JsonResponse(data=message,safe=False,status=200)#safe:是否检查json格式

def getweather(request):
    print(request.method)
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juheWeather.weather(city)
        return JsonResponse(data=data, status=200)
    elif request.method == 'POST':
        print("ksjdsk")
        receive_body = request.body
        receive_body = json.loads(receive_body)
        cities = receive_body.get('cities')
        print(cities)
        response_data = []
        for city in cities:
            result = juheWeather.weather(city)
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)
