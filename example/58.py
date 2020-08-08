import requests
from lxml import etree

# 爬取58中的二手房信息

if __name__ == "__main__":
    url = "https://tj.58.com/ershoufang"
    req = requests.session()
    req.keep_alive = False

    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    proxy = {
        # "http": "123.54.40.133:9999"
    }
    html = req.post(url, headers=header, proxies=proxy).text

    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(html)

    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(html, parser=parser)
    info = tree.xpath("//div[@class='content-wrap']//h2[@class='title']/a/text()")

    with open('test.txt', 'w') as f:
        for i in info:
            f.write(i)
            f.write('\n')
