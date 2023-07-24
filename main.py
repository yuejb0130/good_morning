import os
import random
import time
from datetime import date
from datetime import datetime

import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]

# 获取天气信息使用到的key
key = "&key=c7a171525cda4c689a2abd796bbdbcfd"

# 测试数据
# start_date = "2022-02-04"
# city = "吉林"
# birthday = "12-23"
# app_id = "wxe3b9865fad1bf47d"
# app_secret = "eff75a2a646389b7f38a8a4bb035a5b4"
# user_id = "ob5YG6azKXTtS3NbSmXl60r4lCiQ,ob5YG6dBBWxInyoVYMpRLjs7JBaw"
# template_id = "Q0pJMawrHpKFOvK6MyGme2ww0kTqNpGCrqWDUIE33Nc"

""""
早上好，妍妍!{{thing.DATA}}
今天是 {{day.DATA}} 
城市：{{city.DATA}} 
温度：{{temp.DATA}} ℃ 
天气：{{weather.DATA}} 
风向：{{wind.DATA}} 
综合指数：{{zonghe.DATA}} 
幸运颜色：{{yanse.DATA}} 
幸运数字：{{shuzi.DATA}} 
距离考研还有{{birthday_left.DATA}}天 
今日文案：{{wenan.DATA}}
"""


# 获取用中文表示的星期
def get_chinese_weekday():
    weekday_map = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期天'
    }
    weekday = datetime.today().strftime('%A')
    return weekday_map.get(weekday, '未知')


# 和风天气开发服务
def get_hf_info():
    # 1.获取地点
    location_url = "https://geoapi.qweather.com/v2/city/lookup?location=" + city + key
    location_res = requests.get(location_url).json()
    location = location_res['location'][0]['id']
    # 2.获取天气信息
    weather_url = "https://devapi.qweather.com/v7/weather/now?location=" + location + key
    weather_res = requests.get(weather_url).json()
    return weather_res['now']['temp'], weather_res['now']['text'], weather_res['now']['windDir']


# 通过生日计算星座
def calculate_zodiac_sign():
    month, day = map(int, birthday.split('-'))
    zodiac_dates = [
        (1, 20, 2, 18, "水瓶座"),
        (2, 19, 3, 20, "双鱼座"),
        (3, 21, 4, 19, "白羊座"),
        (4, 20, 5, 20, "金牛座"),
        (5, 21, 6, 21, "双子座"),
        (6, 22, 7, 22, "巨蟹座"),
        (7, 23, 8, 22, "狮子座"),
        (8, 23, 9, 22, "处女座"),
        (9, 23, 10, 23, "天秤座"),
        (10, 24, 11, 22, "天蝎座"),
        (11, 23, 12, 21, "射手座"),
        (12, 22, 1, 19, "摩羯座")
    ]
    zodiac = next((sign for start_month, start_day, end_month, end_day, sign in zodiac_dates if
                   (month == start_month and day >= start_day) or (month == end_month and day <= end_day)), None)
    if zodiac:
        return zodiac
    else:
        return "无效的日期！"


# 星座运势
def get_xingzuo():
    url = "http://api.tianapi.com/star/index?key=21fe23d36674cff7afc2c12e4f3133ec&astro=" + calculate_zodiac_sign() + "&date=" + \
          time.strftime("%Y-%m-%d")
    res = requests.get(url).json()
    return res['newslist'][0]['content'], res['newslist'][2]['content'], res['newslist'][3]['content'], \
           res['newslist'][4]['content'], res['newslist'][5]['content'], res['newslist'][6]['content'], \
           res['newslist'][8]['content']


# 计算纪念日天数
def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


# 计算距离生日天数
def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - (today.replace(hour=0, minute=0, second=0, microsecond=0))).days


# 获取文案
def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    text = words.json()['data']['text']
    if len(text) > 20:
        return get_words()
    return text


# 获取字体颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 温度 天气 风向
temp, weather, wind = get_hf_info()
# 综合指数 工作指数 财运指数
# 健康指数 幸运颜色 幸运数字
# 今日概述
zonghe, gongzuo, caiyun, jiankang, yanse, shuzi, gaishu = get_xingzuo()

data = {
    "thing": {"value": "\n"},
    "day": {"value": time.strftime("%Y-%m-%d") + " " + get_chinese_weekday(), "color": get_random_color()},
    "city": {"value": city, "color": get_random_color()},
    "temp": {"value": temp, "color": get_random_color()},
    "weather": {"value": weather, "color": get_random_color()},
    "wind": {"value": wind, "color": get_random_color()},
    "zonghe": {"value": zonghe, "color": get_random_color()},
    "yanse": {"value": yanse, "color": get_random_color()},
    "shuzi": {"value": shuzi, "color": get_random_color()},
    # "love_days": {"value": get_count(), "color": get_random_color()},
    "birthday_left": {"value": get_birthday(), "color": get_random_color()},
    "wenan": {"value": get_words(), "color": get_random_color()}}

client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)
# 定时推送
#res1 = wm.send_template(user_id[:28], template_id, data)
#res2 = wm.send_template(user_id[-28:], template_id, data)
