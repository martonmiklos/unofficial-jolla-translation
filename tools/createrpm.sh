#!/bin/sh
##############################################
#
# createrpm.sh
#
# This script create the langupack rpm.
#
##############################################


PKGNAME=unofficial-jolla-language-pack-${TSLANG}

if [ x"${TOPDIR}" == x ]; then
    TOPDIR=$HOME/rpmbuild
fi

#if [ ! -d ${TOPDIR} ]; then
    rm -rf ${TOPDIR}
    mkdir ${TOPDIR}
#fi

for n in SOURCES RPMS SRPMS BUILD BUILDROOT SPECS
do
    if [ ! -d ${TOPDIR}/$n ]; then
        mkdir ${TOPDIR}/$n
    fi  
done

SOURCEFILE=${TOPDIR}/SOURCES/${PKGNAME}.tar.bz2

if [ ! -e ${SOURCEFILE} ]; then
	rm -rf rpmbuild
    mkdir -p rpmbuild/${PKGNAME}
    cp -r rpm rpmbuild
    mkdir -p rpmbuild/${PKGNAME}/usr/share
    cp -r usr/share/translations rpmbuild/${PKGNAME}/usr/share/translations
    mkdir -p rpmbuild/${PKGNAME}/usr/share/jolla-supported-languages
    cp usr/share/jolla-supported-languages/$TSLANG.conf rpmbuild/${PKGNAME}/usr/share/jolla-supported-languages/$TSLANG.conf
	cd rpmbuild
    tar jcvf ${TOPDIR}/SOURCES/${PKGNAME}.tar.bz2 ${PKGNAME}
fi

rpmbuild --define "_topdir ${TOPDIR}" -ba rpm/unofficial-jolla-language-pack-${TSLANG}.spec --target noarch

ls -l ${TOPDIR}/RPMS/noarch
ls -l ${TOPDIR}/SRPMS
