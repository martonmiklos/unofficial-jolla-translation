#!/bin/sh
##############################################
#
# createnewresource.sh
#
# This script create new resource definition
#
##############################################

TRANSRATIONDIR=./translations
TXCONFIG=.tx/config

cp -p ${TXCONFIG} ${TXCONFIG}.bak

for n in `ls -1 ${TRANSRATIONDIR}`
do
   grep "[$n]" ${TXCONFIG} > /dev/null 2>&1
   
   if [ $? -ne 0 ]
   then
     echo "" >> ${TXCONFIG}
     echo "[$n]" >> ${TXCONFIG}
     echo "file_filter = translations/$n/<lang>.ts" >> ${TXCONFIG}
     echo "source_lang = en_GB" >> ${TXCONFIG}
     echo "type = QT" >> ${TXCONFIG}
   fi
done
