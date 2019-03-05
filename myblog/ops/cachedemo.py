import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")# project_name 项目名称
django.setup()

from django.core.cache import cache

#缓存模块

def basic_use():
    s = 'hello Djingo cache '
    cache.set('key', s, 5)# 设置缓存数据,5秒有效期
    cache_result = cache.get('key')#获取缓存数据
    print(cache_result)


if __name__ == '__main__':
    basic_use()