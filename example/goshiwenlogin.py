import requests
from lxml import etree
from fateadm_api import FateadmApi


def get_code_value(file=""):
    pd_id = "125194"
    pd_key = "YJbdXa7Fxpfr+4roIOFL3gY3uVwmuwrx"
    app_id = "325194"
    app_key = "3defiZZPh4yCyuEXvcuxJOfL8kq2f7Pp"
    api = FateadmApi(app_id, app_key, pd_id, pd_key)
    # 通过文件形式识别：
    pred_type = "30400"
    # 直接返回识别结果
    rsp = api.PredictExtend(pred_type, file)

    return rsp


if __name__ == "__main__":

    header = {
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/14.0.835.163Safari/535.1',
    }

    url = "https://so.gushiwen.cn"
    login = "/user/login.aspx"
    code_url = "/RandCode.ashx"

    # 所有过程必须在一个会话中完成
    s = requests.session()

    # 构造参数
    # 1. 验证码
    randcode = s.get(url + code_url, headers=header).content
    with open('test.gif', 'wb') as f:
        f.write(randcode)
    prev = get_code_value(randcode)
    print("验证码: " + prev)

    # 2. 获取其他参数
    html = s.get(url + login, headers=header).text
    tree = etree.HTML(html)
    __VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')
    __VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')

    params = {
        "from": "http://so.gushiwen.cn/user/collect.aspx"
    }
    data = {
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "from": "",
        "email": "18215446098",
        "pwd": "pulinsidun@1",
        "code": prev,
        "denlu": "登录"
    }

    html = s.post(url=url + login, data=data, headers=header, params=params)
    html.encoding = 'utf-8'
    html_text = html.text
    with open('test.html', 'w') as f:
        f.write(html_text)
