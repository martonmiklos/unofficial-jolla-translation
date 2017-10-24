#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enchant import DictWithPWL
from enchant.checker import SpellChecker
from enchant.tokenize import EmailFilter, URLFilter
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import types
import os.path
import libxml2
import re
import os


def checkFile(fileName, chkr) :
    print "Checking "+ fileName
    doc = libxml2.parseFile(fileName)
    ctxt = doc.xpathNewContext()
    res = ctxt.xpathEval("//translation")
    for translation in res :
        ok = True
        problemString = ''
        stringToCheck = translation.content
        stringToCheck = stringToCheck.replace('<br>', '\n')
        stringToCheck = stringToCheck.replace('<br/>', '\n')
        stringToCheck = stringToCheck.replace('<p>', ' ')
        stringToCheck = stringToCheck.replace('</p>', ' ')
        stringToCheck = stringToCheck.replace('<b>', ' ')
        stringToCheck = stringToCheck.replace('</b>', ' ')
        chkr.set_text(stringToCheck)
        for err in chkr: 
            ok = False
            problemString = problemString + " - " +err.word + "\n"
        
        if (not ok) : 
            print "Following words are problematic in \""+ translation.content +"\": "
            print problemString
    doc.freeDoc()
    ctxt.xpathFreeContext()

def checkAllFiles() :
    lang = os.environ.get('POOTLE_LANG')
    spellCheckLang = os.environ.get('SPELLCHECK_LANG')
    if (os.environ.get('POOTLE_LANG') == None) :
        print "The POOTLE_LANG variable is not set!"
        print "Please set it with export POOTLE_LANG=hu before calling this script!"
        print "The variable should match with the language code on the pootle."
        return
    
    if (spellCheckLang == None) :
        print "The SPELLCHECK_LANG variable is not set!"
        print "Please set it with export SPELLCHECK_LANG=hu_HU before calling this script!"
        print "The variable should match with the language code on the pootle."
        return
    
    pwl = DictWithPWL(spellCheckLang, "known_words_database/" +lang+ ".txt")
    chkr = SpellChecker(pwl)

    with open("tools/packagelist.txt") as f:
        fileList = f.readlines()
    
    fileList = [x.strip() for x in fileList] 
    
    for filename in fileList :
        checkFile("translations/"+lang+"/" + filename, chkr)

checkAllFiles()
