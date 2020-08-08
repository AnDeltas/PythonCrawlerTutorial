import requests
import re
import json

# first url
url = "http://125.35.6.84:81/xk/itownet/portalAction.do"

header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

# get ID


def first_post():

    data = {
        "on": "true",
        "page": 1,
        "pageSize": 1,
        "productName": "",
        "conditionType": 1,
        "applyname": "",
        "applysn": ""
    }

    param = {
        "method": "getXkzsList"
    }

    req = requests.session()
    req.keep_alive = False
    try:
        result = req.post(url=url, data=data, headers=header, params=param)
        print(result.url)
        print("get data succesfully")
        return result.text
    except:
        print('first error')

def par_url(text: str) -> list:
    pattern = re.compile(r'(?<="ID":").*?(?=")')
    return pattern.findall(text)


def second_post(id: str):
    data = {
        "id": id
    }
    param = {
        "method": "getXkzsById"
    }
    req = requests.session()
    req.keep_alive = False
    try:
        result = req.post(url=url, data=data, headers=header, params=param)
        return result.json()
    except:
        print('second error')


def main():
    text = first_post()
    li = par_url(text)
    for i in li:
        result = second_post(i)
        with open(f"{i}.json", "w") as f:
            json.dump(result, fp=f, ensure_ascii=False)




if __name__ == "__main__":
    main()
