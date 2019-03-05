import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    key = '9a3e1fa6cb79d69f1594af5cb219a469'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(json_data)
    result = json_data.get('result')
    sk = result.get('today')
    city = result.get('wind')
    response = dict()
    response['city'] = sk.get('city')
    response['temperature'] = sk.get('temperature')
    response['weather'] = sk.get('weather')
    response['date_y'] = sk.get('date_y')
    response['week'] = sk.get('week')
    print(response)
    return response


if __name__ == '__main__':
    data = weather('深圳')