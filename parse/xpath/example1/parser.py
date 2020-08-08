from lxml import etree

if __name__ == "__main__":
    with open("./parse/xpath/example1/xpath.html", 'r') as f:
        # 这就是一般情况下的写法
        tree = etree.HTML(f.read())
        path = "/html/body/div" #  <- 这里写我们的xpath表达式
        #  你可以尝试替换成其他的样子
        data = tree.xpath(path)
        print(data)
