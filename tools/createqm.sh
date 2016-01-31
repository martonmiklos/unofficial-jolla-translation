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

for n in $(ls -1 translations)
do
	lrelease -removeidentical translations/$n/${TSLANG}.ts -qm usr/share/translations/$(echo $n | awk -F"." '{print $2}')-${TSLANG}.qm
done

find usr/share/translations -name "*-${TSLANG}.qm"
