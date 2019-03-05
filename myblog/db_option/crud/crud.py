import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")# project_name 项目名称
django.setup()
from authorization.models import Users
import random
def ranstr(length):
    CHS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ranstr= ''
    for i in range(length):
        ranstr += random.choice(CHS)
    return ranstr

#添加一个用户

def add_one_user():
    Users.objects.create(name='tom', address='jiujiangm', city='jiujiang', country='en')
#批量添加
def add_batch_user():
    new_user_list = []
    for i in range(3):
        name = ranstr(5)
        address = ranstr(13)
        city = ranstr(20)
        country = ranstr(10)
        user = Users(name=name, city=city, country=country, address=address)
        new_user_list.append(user)
    #添加一组用户
    Users.objects.bulk_create(new_user_list)

#查询
def get_one():
    user = Users.objects.get(open_id='test_open_id')
    print(user)
# 数据过滤
def get_filter():
    users = Users.objects.filter(open_id__contains='test_')
    # open_id__startswith
    # 大于: open_id__gt(greater than)
    # 小于: open_id__lt(little than)
    # 大于等于：open_id__gte(greater than equal)
    # 小于等于：open_id__lte(little than equal)
    print(users)

# 数据排序
def get_order():
    users = Users.objects.order_by('open_id')
    print(users)

# 连锁查询
def get_chain():
    users = Users.objects.filter(open_id__contains='test_').order_by('open_id')
    print(users)

# 改一个
def modify_one():
    user = Users.objects.get(open_id = 'test_open_id')
    user.nickname = 'modify_username'
    user.save()

# 批量改
def modify_batch():
    Users.objects.filter(open_id__contains='test_').update(nickname='modify_username')

def delete_one():
    Users.objects.get(open_id='test_open_id').delete()

# 批量删除
def delete_batch():
    Users.objects.filter(open_id__contains='test_').delete()

# 全部删除
def delete_all():
    Users.objects.all().delete()
    # User.objects.delete()

# -------------------------
# 数据库函数
# 字符串拼接：Concat

from django.db.models import Value
from django.db.models.functions import Concat

def concat_function():
    user = Users.objects.filter(open_id='test_open_id').annotate(
        # open_id=(open_id), nickname=(nickname)
        screen_name = Concat(
            Value('open_id='),
            'open_id',
            Value(', '),
            Value('nickname='),
            'nickname')
        )[0]
    print('screen_name = ', user.screen_name)

# 字符串长度： Length
from django.db.models.functions import Length

def length_function():
    user = Users.objects.filter(open_id='test_open_id').annotate(
        open_id_length = Length('open_id'))[0]

    print(user.open_id_length)

# 大小写函数
from django.db.models.functions import Upper, Lower

def case_function():
    user = Users.objects.filter(open_id='test_open_id').annotate(
        upper_open_id=Upper('open_id'),
        lower_open_id=Lower('open_id')
    )[0]
    print('upper_open_id:', user.upper_open_id, ', lower_open_id:', user.lower_open_id)
    pass

# 日期处理函数
# Now()
'''
from apis.models import App
from django.db.models.functions import Now

def now_function():
    # 当前日期之前发布的所有应用
    apps = App.objects.filter(publish_date__lte=Now())
    for app in apps:
        print(app)


# 时间截断函数
# Trunc
from django.db.models import Count
from django.db.models.functions import Trunc


def trunc_function():
    # 打印每一天发布的应用数量
    app_per_day = App.objects.annotate(publish_day=Trunc('publish_date', 'month'))\
        .values('publish_day')\
        .annotate(publish_num=Count('appid'))

    for app in app_per_day:
        print('date:', app['publish_day'], ', publish num:', app['publish_num'])

    pass
'''

if __name__ == '__main__':
    add_one_user()