import os
import utils.response
import hashlib
from django.http import Http404,HttpResponse,JsonResponse,FileResponse
from myblog import settings
from django.views import View
from utils.response import ReturnCode
from utils.response import CommonResponseMixin
#直接获取图片
def getSourceImage(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')#获取参数
        imgfile = os.path.join(settings.IMAGES_DIR, md5)
        if not os.path.exists(imgfile):
            return Http404
        else:
            #data = open(imgfile, 'rb').read()
            #return HttpResponse(content=data,content_type='image/png')
            data = open(imgfile, 'rb')
            return FileResponse(data, content_type='image/png')
#返回路径
def getImageUrl(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR,md5)
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(
                code=utils.response.ReturnCode.SUCCESS)
        else:
            response_data = {}
            response_data['name'] = md5
            response_data['url'] = '/service/image?md5=' + md5
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)

#类视图
class getImagetol(View, CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get('md5')  # 获取参数
        imgfile = os.path.join(settings.IMAGES_DIR, md5)
        if not os.path.exists(imgfile):
            return Http404
        else:
            # data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data,content_type='image/png')
            data = open(imgfile, 'rb')
            return FileResponse(data, content_type='image/png')
    def post(self ,request):
        files = request.FILES
        response = []
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR,md5)
            with open(path,'wb')as f:
                f.write(content)
            response.append({
                'name':key,
                'md5':md5
            })

        message = 'post method succes'
        #response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(data=response, code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)
    def put(self ,request):
        message = 'put method succes'
        #response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)
    def delete(self ,request):
        md5 = request.GET.get('md5')
        path = os.path.join(settings.IMAGES_DIR,md5)
        if os.path.exists(path):
            os.remove(path)
            message = 'remove success'
        else:
            message = 'file(%s) not found' % md5
        response = utils.response.wrap_json_response(message=message,code=ReturnCode.SUCCESS)
        return JsonResponse(data=response, safe=False)

#返回所有图片地址
class ImageListView(View , CommonResponseMixin):
    def get(self, request):
        image_files = os.listdir(settings.IMAGES_DIR)
        response_data = []
        for image_file in image_files:
            response_data.append({
                "md5": image_files
            })
        response_data = self.wrap_json_response(data=response_data)
        return JsonResponse(data=response_data)

