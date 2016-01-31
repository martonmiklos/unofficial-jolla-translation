#!/bin/sh
##############################################
#
# inittx.sh
#
# This script initialize transifex project on local.
#
##############################################

if [ -d .tx ]; then
    if [ x"$1" == "x-f" ]; then
        rm -rf .tx
    else
        exit 0
    fi
fi

tx init --host https://www.transifex.com
tx set --auto-remote https://www.transifex.com/projects/p/unofficial-jolla-translations/

exit $?
