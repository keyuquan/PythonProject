#!/usr/bin/python
# encoding: utf-8


import requests
from lxml import etree


def getJokeList(baseurl='http://www.budejie.com/text/{0}'):
    nextPage = True
    pagenum = 1
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    while nextPage:
        url=baseurl.format(pagenum)
        response = requests.get(url, headers=header)
        selector=etree.HTML(response.text)

        jokes = selector.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
        for joke in jokes:
            yield joke

        hasNext= selector.xpath('//a[@class="pagenxt"]')
        if hasNext:
            pagenum += 1
        else :
            nextPage = False


if __name__=='__main__':
    f=open('basejie.txt','w')
    for joke in getJokeList():
        f.writelines('~' * 100)
        f.writelines('\r\n')
        f.writelines('\r\n')
        f.writelines(joke.encode('utf8'))
        f.writelines('\r\n')
        f.writelines('\r\n')

    f.close()
