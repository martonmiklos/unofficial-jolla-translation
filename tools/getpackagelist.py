#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pyquery import PyQuery as pq
from lxml import etree
import urllib

packageList = []

def processPackageNames(node, groupName):
    packageList.append(groupName+ "/" + node.text)
    

def getPackageFiles(index, node):
    if node.text != 'terminology' :
        d = pq(url='https://translate.sailfishos.org/hu/'+node.text, opener=lambda url, **kw: urllib.urlopen(url).read())
        p=d("td.stats-name > a > span").each(lambda index, e: processPackageNames(e, node.text))


d = pq(url='https://translate.sailfishos.org/hu/', opener=lambda url, **kw: urllib.urlopen(url).read())
p=d("td.stats-name > a > span").each(getPackageFiles)

packageList = sorted(packageList)

for p in packageList:
    print p
