from lxml import etree
import requests

if __name__ == "__main__":
    url = "http://pic.netbian.com"
    header = {
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    req = requests.session()
    req.keep_alive = False
    data = req.get(url=url, headers=header)
    data.encoding = 'utf-8'
    html = data.text

    print('html ready')
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(html, parser=parser)
    pic_url_list = tree.xpath('//div[@class="slist"]//ul/li//img/@src')
    print('pic_url ready')
    print(pic_url_list)
    for i in pic_url_list:
        pic_url = url + i
        pic = requests.get(pic_url, headers=header).content
        with open(f'{i.split("/")[-1]}', 'wb') as f:
            f.write(pic)
            print('download')
