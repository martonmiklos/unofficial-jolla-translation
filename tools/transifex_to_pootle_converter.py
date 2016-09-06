#!/usr/bin/python
# -*- coding: UTF-8 -*-


from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import types
import os.path
''' 

An utility to conmvert between TS file formats used by Pootle and Transifex

It pulls a template file which is translated (to make it easy English) and the same file in the convertable format. 
The output file will be the same as the template just the translation tags will be replaced.

Pootle format:
    <message id="alarm-ui-me-alarm_dialog_dismiss">
        <location filename="../pages/AlarmDialogBase.qml" line="125"></location>
        <source>Dismiss</source>
        <translation>Dismiss</translation>
    </message>
    
Transifex format:
    <message>
        <source>alarm-ui-me-alarm_dialog_dismiss</source>
        <translation>Elutasít</translation>
    </message>
'''

def help() :
    print "Usage:"
    print "transifex_to_pootle_converter.py file_to_convert.ts template_file.ts output_file.ts target_lang"
    print "or if you want to use the \"Translation memory\" feature"
    print "transifex_to_pootle_converter.py file_to_convert.ts template_file.ts output_file.ts target_lang translation_memory.ts"
    
# translation English translation from the template
# translationMemoryFilePath path of the TS file used for translation memory (English TS in transifex format)
# inData translatable TS file context
# returns with the translation or empty string
def findRenamedTranslationIdFromTranslationMemory(translation, translationMemoryFilePath, inData, newId):
    if ( not os.path.isfile(translationMemoryFilePath) ) : 
        return ''
    translationMemoryFile = translationMemoryFilePath
    translationMemoryData = xml.dom.minidom.parse(translationMemoryFile)
    translationMemoryContext = translationMemoryData.documentElement.getElementsByTagName("context")[0]
    oldId = ''
    for translationMemoryMessage in translationMemoryContext.getElementsByTagName("message") :
        if (translationMemoryMessage.getElementsByTagName("translation")[0].firstChild.nodeValue == translation) :
            oldId = translationMemoryMessage.getElementsByTagName("source")[0].firstChild.nodeValue
            break;
    if (oldId == '') :
        return ''
    
    inContext = inData.documentElement.getElementsByTagName("context")[0]
    for inMessage in inContext.getElementsByTagName("message"):
        if (inMessage.getElementsByTagName("source")[0].firstChild.nodeValue == oldId) :
            #print("Found renamed translation: %s -> %s" % (oldId, newId))
            return inMessage.getElementsByTagName("translation")[0].firstChild.nodeValue
    return ''
    
def main() :
    renameCount = 0
    translated = 0
    unTranslated = 0
    if (len(sys.argv) < 5) :
        help()
        return 0

    inFile = sys.argv[1]
    templateFile = sys.argv[2]
    outFile = sys.argv[3]
    targetLang = sys.argv[4]

    inData = xml.dom.minidom.parse(inFile)
    templateData = xml.dom.minidom.parse(templateFile)

    if (len(inData.documentElement.getElementsByTagName("context")) == 0) :
        print("No context tag found in the input file: %s" % inFile)
        return 0
    inContext = inData.documentElement.getElementsByTagName("context")[0]
    
    # overwrite the <TS> tag's language attribute
    langAttr = inData.createAttribute('language')
    langAttr.value = targetLang
    templateData.documentElement.setAttributeNode(langAttr)
    
    if (len(templateData.documentElement.getElementsByTagName("context")) == 0) :
        print("No context tag found in the template file (%s)!" % templateFile)
        return 0
    templateContext = templateData.documentElement.getElementsByTagName("context")[0]

    # all translations in the template will be marked with untranslated to be able 
    # to strings present in the template and not present in the translation unfinished
    # the untranslated attribute will be removed when the translation is found
    for templateMessage in templateContext.getElementsByTagName("message"):
        templateTranslation = templateMessage.getElementsByTagName("translation")[0]
        templateTranslation.setAttribute('type', "unfinished") # mark all translation unfinished
        
        translation = ''
        # loop on the <message> tags of the input file
        for inMessage in inContext.getElementsByTagName("message") :
            if (templateMessage.attributes["id"].value == inMessage.getElementsByTagName("source")[0].firstChild.nodeValue) :
                translation = inMessage.getElementsByTagName("translation")[0].firstChild.nodeValue

        
        if (templateMessage.getElementsByTagName("source")[0].hasChildNodes()) :    
            if (translation == '' and len(sys.argv) == 6) :
                # in message not found
                findRenamedTranslationIdFromTranslationMemory(
                    templateMessage.getElementsByTagName("source")[0].firstChild.nodeValue,
                    sys.argv[5],
                    inData,
                    templateMessage.attributes["id"].value
                )
                if (translation != '') :
                    renameCount = renameCount + 1
        else :
            print("Template translation with empty source: %s " % templateMessage.attributes["id"].value)
            
        if (translation == '') :
            print("%s was not found in the input file" % templateMessage.attributes["id"].value)
            unTranslated = unTranslated + 1
        else :
            translated = translated + 1
            
        if (templateMessage.hasAttribute('numerus') and templateMessage.getAttribute('numerus') == 'yes') :
            numerusform = templateTranslation.getElementsByTagName("numerusform")[0]
            if (numerusform.firstChild is not None) :
                numerusform.firstChild.nodeValue = translation
                templateMessage.removeAttribute('type')
        else :
            if (templateTranslation.firstChild is not None) :
                templateTranslation.firstChild.nodeValue = translation
                if (translation != ''):
                    templateTranslation.removeAttribute('type')
            else :
                templateTranslation.childNodes = [inData.createTextNode(translation)]
                if (translation != ''):
                    templateTranslation.removeAttribute('type')

    file_handle = open(outFile,"wb")
    if not file_handle.closed :
        file_handle.write(templateData.toxml().encode("UTF-8"))
        file_handle.close()
    else :
        print "Unable to open the file for writing"
        return -1
    print("Statistics:")
    print("\tTranslated:\t\t%d" % translated)
    print("\tUntranslated:\t\t%d" % unTranslated)
    print("\tRenamed:\t\t%d" % renameCount)
if __name__ == "__main__":
    main()