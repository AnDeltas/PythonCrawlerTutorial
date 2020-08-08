from lxml import etree

if __name__ == "__main__":
    with open("./parse/xpath/example2/baidu.html", 'r') as f:
        parser = etree.HTMLParser(recover=f)
        # 出现这种情况是因为对应的html文件语法错误太多
        # 我们需要手动添加一个HTMLParser
        tree = etree.parse(f, parser=parser)
        path = "/html/body/div/@id" 
        data = tree.xpath(path)
        print(data)