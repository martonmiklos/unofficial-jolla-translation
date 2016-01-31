#!/bin/sh
##############################################
#
# convert2ts.sh
#
# This script convert qm file to ts file.
#
##############################################

QMDIR=./qmfiles
TSDIR=./tsfiles

if [ ! -e ${TSDIR} ]
then
	mkdir ${TSDIR}
fi

for FILE in `ls -1 ${QMDIR}`
do
    lconvert -i ${QMDIR}/${FILE} -if qm -o ${TSDIR}/`basename ${FILE} .qm`.ts -of ts
done

ls -l ${TSDIR}




