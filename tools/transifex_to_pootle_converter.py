#!/usr/bin/python
# -*- coding: UTF-8 -*-


from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import types

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
    print "Usage: transifex_to_pootle_converter.py file_to_convert.ts template_file.ts output_file.ts target_lang"

def findTemplateElement(messageName, templateContext) :
    for message in templateContext.getElementsByTagName("message"):
            if (message.attributes["id"].value == messageName) : 
                return message
    return 0

def main() :
    if (len(sys.argv) != 5) :
        help()
        return 0

    inFile = sys.argv[1]
    templateFile = sys.argv[2]
    outFile = sys.argv[3]
    targetLang = sys.argv[4]

    inData = xml.dom.minidom.parse(inFile)
    templateData = xml.dom.minidom.parse(templateFile)

    if (len(inData.documentElement.getElementsByTagName("context")) == 0) :
        print("No context tag found in the input file (%s).", inFile)
        return 0
    inContext = inData.documentElement.getElementsByTagName("context")[0]
    
    # overwrite the <TS> tag's language attribute
    langAttr = inData.createAttribute('language')
    langAttr.value = targetLang
    inData.documentElement.setAttributeNode(langAttr)
    
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
        
        if (templateMessage.hasAttribute('numerus') and templateMessage.getAttribute('numerus') == 'yes') :
            numerusform = templateTranslation.getElementsByTagName("numerusform")[0]
            if (numerusform.firstChild is not None) :
                numerusform.firstChild.nodeValue = ''
        else :
            if (templateTranslation.firstChild is not None) :
                templateTranslation.firstChild.nodeValue = ''

    for inMessage in inContext.getElementsByTagName("message"):    
        source = inMessage.getElementsByTagName("source")[0]
        templateMessage = findTemplateElement(source.firstChild.nodeValue, templateContext)
        if (templateMessage == 0) :
            print("Deprecated string: %s unable to find the message with the same source in the template file!" % source.firstChild.nodeValue) 
        else :
            inTranslation = inMessage.getElementsByTagName("translation")[0]
            templateTranslation = templateMessage.getElementsByTagName("translation")[0]
            templateTranslation.removeAttribute('type') # mark all found messages translated
            
            # Transifex files seems to be ignoring the numerus formats...
            if (templateMessage.hasAttribute('numerus') and templateMessage.getAttribute('numerus') == 'yes') :
                # numerous item -> overwrite the numerusform
                numerusform = templateTranslation.getElementsByTagName("numerusform")[0]
                if (numerusform.firstChild is None) :
                    newNumerusform = templateData.createTextNode(inTranslation.firstChild.nodeValue)
                    newNumerusform.value = inTranslation.firstChild.nodeValue
                    numerusform.appendChild(newNumerusform)
                else :
                    numerusform.firstChild.nodeValue = inTranslation.firstChild.nodeValue
            else :
                # non numerous item -> simply replace the translation in the template message
                templateMessage.replaceChild(inTranslation, templateTranslation)
            # and then put the template message to the input context
            inContext.replaceChild(templateMessage, inMessage)

    file_handle = open(outFile,"wb")
    if not file_handle.closed :
        file_handle.write(inData.toxml().encode("UTF-8"))
        file_handle.close()
    else :
        print "Unable to open the file for writing"
        return -1

if __name__ == "__main__":
    main()