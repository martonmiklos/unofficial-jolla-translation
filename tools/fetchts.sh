#!/bin/sh
##############################################
#
# fetchts.sh
#
# This script fetch ts files from pootle.
#
##############################################


POOTLE_PREFIX="https://translate.sailfishos.org/download"
TRANSLATIONS_DIR=translations
PACKAGELIST_FILE="tools/packagelist.txt"
if [ x"$TSLANG" == "x" ]; then
    TSLANG=hu
fi

i=0
TS_COUNT=$(wc -l < $PACKAGELIST_FILE)
while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    TS_DIR=$(dirname "${line}")
    mkdir -p $TRANSLATIONS_DIR/$TS_DIR
    wget --quiet $POOTLE_PREFIX/$TSLANG/$line -O $TRANSLATIONS_DIR/$line
    ((i++))
    echo $i/$TS_COUNT ts files downloaded
done < $PACKAGELIST_FILE
