#/bin/bash

RPMDIR="$HOME/rpmbuild/RPMS/noarch"
RPMFILE=`ls $RPMDIR -tp | grep -v /$ | head -1`
scp $RPMDIR/$RPMFILE nemo@192.168.1.66:/tmp
ssh nemo@192.168.1.66 "pkcon -y install-local /tmp/$RPMFILE"