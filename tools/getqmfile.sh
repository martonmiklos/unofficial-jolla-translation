#!/bin/bash
##############################################
#
# getqmfiles.sh
#
# This script fetch qm file from Jolla device
#
##############################################

JOLLA_DEVICE_IP=192.168.2.15
JOLLA_USERID=nemo

SAVE_DIR=./qmfiles

if [ ! -e ${SAVE_DIR} ]
then
	mkdir ${SAVE_DIR}
fi

#fetch "*eng_en" qmfiles
scp ${JOLLA_USERID}@${JOLLA_DEVICE_IP}:/usr/share/translations/*eng_en.qm ${SAVE_DIR}/

#fetch "*en_GB" qmfiles
scp ${JOLLA_USERID}@${JOLLA_DEVICE_IP}:/usr/share/translations/*en_GB.qm ${SAVE_DIR}/

ls ${SAVE_DIR}

exit 

