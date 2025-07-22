import requests
from settings import *
from bark_send import SendBark

# 获取热榜数据
class DyHot:
    def __init__(self, params):
        self.params = params

    # 获取响应数据，jso格式
    def get_json(self):
        resp = requests.get(url=HOST,params=self.params[0],headers=HEADERS)
        dy_json = resp.json()
        return dy_json

    # 获取实时上升热点
    def get_rise(self):
        rise_list = []
        all_data = self.get_json()['data']
        update_time = all_data['active_time']
        for data in all_data['trending_list']:
            rise_list.append(data['word'])
        return update_time, rise_list

    # 获取榜单数据，50条
    def get_hot_list(self):
        hot_list = []
        all_data = self.get_json()['data']
        update_time = all_data['active_time']
        for data in all_data['word_list']:
            hot_list.append(data['word'])
        return update_time, hot_list

# 获取bark发送格式数据
class BarkText:
    def __init__(self, params):
        self.params = params
        self.dy_hot = DyHot(params)

    def get_rise_bark(self):
        rise = self.dy_hot.get_rise()
        title = f"抖音实时上升热点 {rise[0]}"
        content = "\n✅ " + "\n\n✅ ".join(rise[1])  # 一共5条
        return title, content
    
    def get_hot_bark(self):
        hot = self.dy_hot.get_hot_list()
        title = f"抖音{self.params[1]} {hot[0]}"
        content = "\n✅ " + "\n\n✅ ".join(hot[1][0:30])  # 只取前30条,bark超过30条不发送
        return title, content
