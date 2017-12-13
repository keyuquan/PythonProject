#!/usr/bin/python
# encoding: utf-8

from lxml import etree
import requests
import json

def getBooksNum():
    x =requests.get(u'http://www.douban.com/j/tag/items?start=0&limit=1&topic_id=255&topic_name=小说&mod=book'.encode('utf-8'))
    bookjson = x.json()
    booksnum = bookjson['total']
    print json.dumps(bookjson,indent= 4)

    return booksnum

print getBooksNum()

def getBooks():
    dynurl = u'http://www.douban.com/j/tag/items?start={0}&limit={1}&topic_id=255&topic_name=小说&mod=book'
    booksnum=getBooksNum()

    start = 0
    limit = 10
    while start < booksnum:
        x = requests.get(dynurl.format(start,limit).encode('utf-8'))
        bookjson= x.json()
        bookslist=bookjson['html']
        yield bookslist
        start += limit

def parseBookHTML(bookslist):
    for books in bookslist:
        bookshtml = u'<dbook>'.encode('utf-8')+ books + u'</dbook>'.encode('utf-8')
        doc = etree.fromstring(bookshtml)
        for eachbook in doc.xpath('//dl/dd'):
            bookname = eachbook.xpath('a/text()')[0]
            bookurl = eachbook.xpath('a/@href')[0]
            pubs = eachbook.xpath('div[@class="desc"]/text()')
            pub = pubs[0] if pubs else None
            rates = eachbook.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()')
            rate = rates[0] if rates else None
            yield bookname,bookurl,pub,rate



if __name__=='__main__':
    bookslist=getBooks()
    books=parseBookHTML(bookslist)

    line=lambda x: x


    for bookname,bookurl,pub,rate in books:
        print line(bookurl)
        print line(bookname)