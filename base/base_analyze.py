import json
from page.login_page import LoginPage

# 解析json数据
def analyze_data(filename):
    with open("./data/" + filename, "r", encoding="utf-8") as f:
        list_data = []
        dict_data = json.load(f)
        for value in dict_data.values():
            list_data.append(value)
        return list_data