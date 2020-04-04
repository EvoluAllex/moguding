# -*- coding: utf-8 -*-
import json
import requests
def send(token):
    # planId 是设备id可以随便改 address 自己填一下就可以了 longitude 经度  latitude纬度  在地图上搜一下
    data = {"country": "中国", "address": "河北省 · 石家庄市 · 石家庄水电机动车驾驶员学校", "province": "河北省", "city": "石家庄市",
            "latitude": "38.038716", "description": "", "planId": "28ebd7aa4e5342c9229f17d1b0f5c066", "type": "START",
            "device": "Android", "longitude": "114.411354"}
    data = json.dumps(data)
    url = 'https://api.moguding.net:9000/attendence/clock/v1/save'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json; charset=UTF-8'
    }
    res = requests.post(url=url, data=data, headers=headers).text
    print(res)
def login():
    # 请自行更换 账号和密码
    data = {
        "phone": "157321",
        "password": "a123456",
        "loginType": "android"
    }
    res = requests.post('https://api.moguding.net:9000/session/user/v1/login',
                        data=json.dumps(data),
                        headers={
                            'Content-Type': 'application/json; charset=UTF-8'
                        }, ).text
    res = json.loads(res)
    if (res['code'] != 200):
        print("请检查账号")
        exit()
    token = res['data']['token']
    send(token)
if __name__ == '__main__':
    login()
