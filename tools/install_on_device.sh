#/bin/bash

RPMDIR="$HOME/rpmbuild/RPMS/noarch"
RPMFILE=`ls $RPMDIR -tp | grep -v /$ | head -1`
DEVADDRESS=af # added to /etc/hosts
scp $RPMDIR/$RPMFILE nemo@$DEVADDRESS:/tmp
ssh nemo@$DEVADDRESS "devel-su pkcon -y install-local /tmp/$RPMFILE"
