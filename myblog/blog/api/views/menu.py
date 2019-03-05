import os
import yaml
from django.http import JsonResponse
from myblog import settings
import utils.response

def init_app_data():
    #获取文件路径
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    #打开文件
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps
#返回文件列表
def get_menu(request):
    global_app_data = init_app_data()
    published_app_data = global_app_data.get('published')
    response = utils.response.wrap_json_response(data=global_app_data,code=utils.response.ReturnCode.SUCCESS)
    return JsonResponse(data=response,safe=False)