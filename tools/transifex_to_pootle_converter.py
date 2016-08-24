#!/usr/bin/python
# -*- coding: UTF-8 -*-


from xml.dom.minidom import parse
import xml.dom.minidom
import pprint
import sys

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
    print "Usage: transifex_to_pootle_converter.py file_to_convert.ts template_file.ts output_file.ts"

def findTemplateElement(messageName, templateContext) :
    for message in templateContext.getElementsByTagName("message"):
            if (message.attributes["id"].value == messageName) : 
                return message
    return 0

def main() :
    if (len(sys.argv) != 4) :
        help()
        return 0

    inFile = sys.argv[1]
    templateFile = sys.argv[2]
    outFile= sys.argv[3]

    pp = pprint.PrettyPrinter(indent=4)

    inData = xml.dom.minidom.parse(inFile)
    templateData = xml.dom.minidom.parse(templateFile)

    inContext = inData.documentElement.getElementsByTagName("context")[0]
    templateContext = templateData.documentElement.getElementsByTagName("context")[0]

    for inMessage in inContext.getElementsByTagName("message"):    
        source = inMessage.getElementsByTagName("source")[0]
        templateMessage = findTemplateElement(source.firstChild.nodeValue, templateContext)
        if (templateMessage == 0) :
            print "Unable to find the message with the same source in the template file!"
        else :
            inTranslation = inMessage.getElementsByTagName("translation")[0]
            templateTranslation = templateMessage.getElementsByTagName("translation")[0]
            '''print templateMessage
            print templateTranslation.parentNode'''
            templateMessage.replaceChild(inTranslation, templateTranslation)
            inContext.replaceChild(templateMessage, inMessage)

    file_handle = open(outFile,"wb")
    file_handle.write(inContext.toxml().encode("UTF-8"))
    file_handle.close()

if __name__ == "__main__":
    main()