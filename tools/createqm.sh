#!/bin/sh
##############################################
#
# createqm.sh
#
# This script compile ts file to qm file
#
##############################################

if [ x"$TSLANG" == "x" ]; then
    TSLANG=ja_JP
fi

PACKAGELISTFILE="tools/packagelist.txt"

rm -rf usr/share/translations/*
i=0
TS_COUNT=$(wc -l < $PACKAGELISTFILE)
while IFS='' read -r line || [[ -n "$line" ]]; do
    FILENAME=$(echo "$line" | sed "s/.*\///")
    FILENAME=$(echo $FILENAME | awk -F"." '{print $1}')
    lrelease -removeidentical -idbased translations/$line -qm usr/share/translations/$FILENAME-${TSLANG}.qm
done < $PACKAGELISTFILE

find usr/share/translations -name "*-${TSLANG}.qm"
