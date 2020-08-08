import requests

url = "https://baidu.com/s?"
keyword = input('enter a keyword: ')
param = {
    'wd': keyword
}
User_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
header = {
    "user-agent": User_agent
}
if __name__ == '__main__':

    response = requests.get(url=url, params=param, headers=header)
    print(response.encoding)
    print(response.headers)
    response.encoding = 'utf-8'
    page_text = response.text
    with open('{}.html'.format(keyword), 'w', encoding='utf-8') as f:
        f.write(page_text)
    print('ok')
