import requests
from lxml import etree
import fateadm_api


if __name__ == "__main__":
    pd_id = "125194"  # 用户中心页可以查询到pd信息
    pd_key = "YJbdXa7Fxpfr+4roIOFL3gY3uVwmuwrx"
    app_id = "325194"  # 开发者分成用的账号，在开发者中心可以查询到
    app_key = "3defiZZPh4yCyuEXvcuxJOfL8kq2f7Pp"
    api = fateadm_api.FateadmApi(pd_id=pd_id, pd_key=pd_key, app_id=app_id, app_key=app_key)
    for cnt in range(20):
        url = f"https://bing.ioliu.cn/ranking?p={cnt}"
        header = {
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,"\
            " like Gecko) Chrome/84.k.4147.105 Safari/537.36",
        }
        data = requests.get(url=url, headers=header)
        
        html = data.text
        tree = etree.HTML(html)
        part_url = tree.xpath('//div[@class="card progressive"]/img/@data-progressive')

        pic_list = []
        tail = "1920x1080.jpg"
        for i in part_url:
            pic_list.append(i.split('?')[0][0:-11] + tail)

        for i in pic_list:
            pic = requests.get(url=i, headers=header).content
            with open(f'assets/{i.split("/")[-1]}', "wb") as f:
                f.write(pic)

