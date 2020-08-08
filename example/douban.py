#!/usr/bin/python
import requests
import json


url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": "17",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

proxy = {
    # "http": "175.42.129.160:9999",
}

if __name__ == "__main__":
    s = requests.session()
    s.keep_alive = False
    response = s.get(url, params=param, headers=header, proxies=proxy)
    result = response.json()
    with open("test.json", "w") as f:
        json.dump(result, fp=f, ensure_ascii=False)
