#!/bin/sh
##############################################
#
# fetchts.sh
#
# This script fetch ts files from transifex.
#
##############################################

OPT=""

if [ x"$1" == "x-f" ]; then
    OPT=$1
    rm -rf translations
fi

if [ x"$TSLANG" == "x" ]; then
    TSLANG=ja_JP
fi

tx pull -l $TSLANG $OPT

find . -name ${TSLANG}.ts
