#/bin/bash

RPMDIR="$HOME/rpmbuild/RPMS/noarch"
RPMFILE=`ls $RPMDIR -tp | grep -v /$ | head -1`
scp $RPMDIR/$RPMFILE nemo@jolla:/tmp
ssh nemo@jolla "pkcon -y install-local /tmp/$RPMFILE"