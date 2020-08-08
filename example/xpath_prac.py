import requests
from lxml import etree


def main():
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse("test.html", parser=parser)
    data1 = tree.xpath("//div[@id='ftConw']/p/text()")
    data2 = tree.xpath("//div[@id='ftConw']/p//text()")
    data3 = tree.xpath("//div[@id='ftConw']/p/a/text()")
    print(data1)
    print(data2)
    print(data3)


if __name__ == "__main__":
    main()
