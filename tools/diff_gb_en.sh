#!/bin/bash
##############################################
#
# diff_gb_en.sh
#
# This script check if unique file exists
# on ether en_GB or eng_en files and delete
# duplicated ts files.
#
##############################################

TSDIR=./tsfiles
TRANSLATIONDIR=./translations
TMPFILE=/tmp/ts.tmp
OUTFILE=./difftxt.out

rm ${TMPFILE} ${OUTFILE}

for FILE in `ls -1 ${TSDIR}/*en_GB*`
do
    basename ${FILE} -en_GB.ts >> ${TMPFILE}
done

for FILE in `ls -1 ${TSDIR}/*_eng_en*`
do
    basename ${FILE} _eng_en.ts >> ${TMPFILE}
done

sort ${TMPFILE} | uniq > ${OUTFILE}

for FILE in `cat ${OUTFILE}`
do
    if [ -e ${TSDIR}/${FILE}-en_GB.ts -a -e ${TSDIR}/${FILE}_eng_en.ts ]
    then
        rm ${TSDIR}/${FILE}_eng_en.ts
    fi
done

ls -l ${TSDIR}

if [ ! -d ${TRANSLATIONDIR} ]
then
  echo "directory translations not found"
  exit 2
fi

for n in `cat ${OUTFILE}`
do
    if [ -e ${TSDIR}/${n}-en_GB.ts ]
    then
        COPYSOURCE=${TSDIR}/${n}-en_GB.ts
    else
        COPYSOURCE=${TSDIR}/${n}_eng_en.ts
    fi

    RESOURCEDIR=./translations/unofficial-jolla-translations.$n

    if [ ! -e ${RESOURCEDIR} ]
    then
        mkdir ${RESOURCEDIR}
    fi

    cp ${COPYSOURCE} ./translations/unofficial-jolla-translations.$n/en_GB.ts

done

ls -lR ./translations
