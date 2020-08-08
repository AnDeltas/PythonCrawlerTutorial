import requests
import re
# 爬取图片
header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
proxy = {
    "http": "110.243.15.253:9999"
}
# src="//pic.qiushibaike.com/system/pictures/12341/123414893/medium/SHJ4T60E5FZY4SV0.jpg"
if __name__ == "__main__":
    for page in range(1, 14):
        print(f"第{page}页开始下载")
        url = f"https://www.qiushibaike.com/imgrank/page/{page}/"

        html = requests.get(url=url, headers=header, proxies=proxy).text
        pattern = re.compile(r'(?<=img src=")//pic.*?jpg(?=")')
        pic_list = pattern.findall(html)
        for i in pic_list:
            pic_name = i.split('/')[-1]
            with open(f"qiutu/{pic_name}", "wb") as f:
                req = requests.session()
                req.keep_alive = False
                pic = req.get(url=f"https:{i}", headers=header, proxies=proxy)
                f.write(pic.content)
                print('下载完成!!!')
