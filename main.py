import math
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

# 测试数据
# start_date = "2022-02-04"
# city = "西安"
# birthday = "09-04"
# app_id = "wx49e7eddadffbf05e"
# app_secret = "d25ab0ba046f79c110b620a9837da35d"
# user_id = "o_Tnm6BNGYVt4b7Rd6rn91ucKIbk,o_Tnm6JVuaTN4U2URm4oSbWKLZ5U"
# template_id = "OdhnBv_P8t7p-3GnFblHgdURfAkXw3IsPr8aqrhqhWg"

# 定时发送数据
# o_Tnm6JVuaTN4U2URm4oSbWKLZ5U,o_Tnm6GhHixABnUhzXOqhympo7ZI

""""
宁仙子的专属消息提醒

{{day.DATA}}  {{week.DATA}}
城市：{{city.DATA}}
天气：{{weather.DATA}}
最低温度：{{low.DATA}} ℃
当前温度：{{temperature.DATA}} ℃
最高温度：{{high.DATA}} ℃
今天是我们在一起：{{love_days.DATA}} 天
距离宁宁的生日还有：{{birthday_left.DATA}}天
{{words.DATA}}
"""


# 获取天气以及温度
def get_weather():
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather['weather'], math.floor(weather['temp']), math.floor(weather['low']), math.floor(weather['high'])


# 计算纪念日天数
def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


# 计算距离生日天数
def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


# 获取文案
def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


# 获取字体颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, low, high = get_weather()
data = {"day": {"value": time.strftime("%Y-%m-%d")},
        "week": {"value": datetime.today().strftime('%A'), "color": get_random_color()},
        "city": {"value": city, "color": get_random_color()},
        "weather": {"value": wea, "color": get_random_color()},
        "temperature": {"value": temperature, "color": get_random_color()},
        "low": {"value": low, "color": get_random_color()},
        "high": {"value": high, "color": get_random_color()},
        "love_days": {"value": get_count(), "color": get_random_color()},
        "birthday_left": {"value": get_birthday(), "color": get_random_color()},
        "words": {"value": get_words(), "color": get_random_color()}}
# 设置同时给宁宁以及我定时推送
res1 = wm.send_template(user_id[:28], template_id, data)
res2 = wm.send_template(user_id[-28:], template_id, data)
print(res1)
print(res2)
