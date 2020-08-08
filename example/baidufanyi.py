#!/usr/bin/python

import requests
import re
import json


class Baidufanyi(object):
    url = "https://fanyi.baidu.com/sug"

    data = {}

    __User_agent = "Mozilla/5.0 (X11; Linux x86_64)"\
                    " AppleWebKit/537.36 (KHTML, like Gecko)"\
                    " Chrome/84.0.4147.105 Safari/537.36"

    header = {
        'User-Agent': __User_agent
    }

    def __init__(self, target_file_name: str):
        self.file_name = target_file_name

    def get_trans(self):
        with open(f"{self.file_name}", "r") as f:
            text = f.read()
            pattern = re.compile(r'\w+')
            target_list = pattern.findall(text)
            for i in target_list:
                result = self.trans(i)
                with open(f"{self.file_name.split('.')[0]}.txt", 'a') as fp:
                    json.dump(result, fp=fp, ensure_ascii=False)
                    fp.write('\n')
        print('Over!')

    def trans(self, keyword) -> dict:
        self.data['kw'] = keyword
        try:
            res = requests.post(
                url=self.url, data=self.data, headers=self.header)
            return res.json()
        except ConnectionError as err:
            print(err)

    def update_cookie(self) -> str:
        pass  # TODO : 完善更新cookie功能


def main():
    file_name = input('tell me the target file name: ')
    work = Baidufanyi(file_name)
    work.get_trans()


if __name__ == "__main__":
    main()
