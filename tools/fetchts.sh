#!/bin/sh
##############################################
#
# fetchts.sh
#
# This script fetch ts files from pootle.
#
##############################################


POOTLE_PREFIX="https://translate.sailfishos.org/download"
PACKAGELIST_FILE="tools/packagelist.txt"

if [ -z $POOTLE_LANG ] 
then
    echo "The POOTLE_LANG variable is not set!"
    echo "Please set it with export POOTLE_LANG=hu before calling this script!"
    echo "The variable should match with the language code on the pootle."
    exit -1
fi

TRANSLATIONS_DIR=translations/$POOTLE_LANG

i=0
TS_COUNT=$(wc -l < $PACKAGELIST_FILE)
while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    TS_DIR=$(dirname "${line}")
    mkdir -p $TRANSLATIONS_DIR/$TS_DIR
    wget --quiet $POOTLE_PREFIX/$POOTLE_LANG/$line -O $TRANSLATIONS_DIR/$line
    ((i++))
    echo "$i/$TS_COUNT ts files downloaded ($line)"
done < $PACKAGELIST_FILE
