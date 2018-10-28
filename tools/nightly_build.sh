#!/bin/dash

log() {
	>>log.txt echo "$@"
}

we=`basename $0`

usage() {
	[ -n "$1" ] && echo $we: $@
	cat <<.
	$we:

	this script builds a new package if there are differences in the
	translation compared to the last time it had built a package. It
	automatically increases minor version numbers for new builds,
	generates diffs and publishes both diffs and packages to the
	configured destination.

	The resulting target directory may look like this after running
	it 3 times:

	diffs/
	latest.rpm
	log.txt
	unofficial-jolla-language-pack-bg-2.1.2-0.0.1.noarch.rpm
	unofficial-jolla-language-pack-bg-2.1.2-0.0.2.noarch.rpm
	unofficial-jolla-language-pack-bg-2.1.2-0.0.3.noarch.rpm
	...


	Usage:
	% export lang=bg maintainer=omkpuBamev uploadsrvr=example.com uploadpath=websites/public/sailfish
	% $we

	Example invocation as cronjob every night at 1:30am:
	30      1      *       *       *       lang=bg maintainer=omkpuBamev uploadsrvr=example.com uploadpath=websites/public/sailfish /home/omkpuBamev/repos/unofficial-jolla-translation/tools/nightly_build.sh
.
	exit 1
}

# make sure vars we expect are set
[ -n "$lang" ] || usage "lang not set"
[ -n "$maintainer" ] || usage "maintainer not set"
[ -n "$uploadsrvr" ] || usage "uploadsrvr not set"
[ -n "$uploadpath" ] || usage "uploadpath not set"

# conf
export POOTLE_LANG=$lang QM_SUFFIX=$lang LANGCODE=$lang
spec=rpm/unofficial-jolla-language-pack-$lang.spec
upload=$uploadsrvr:$uploadpath
echo using "
	spec: $spec
	maintainer: $maintainer
	upload: $upload
"
this=`realpath $0`
thisdir=`dirname $this`

# go to one above tools/
cd $thisdir
cd ..

# get new version from file
lastver=`sed -n "/^Release:/ { s/Release:\s*//; p}" $spec`
lastnum=`echo $lastver | cut -d. -f3`
newnum=$(($lastnum + 1))
majorminor=`echo $lastver | cut -d. -f1,2`
newver=$majorminor.$newnum

ts=`date +%FT%T`
log running $ts
echo "last: $lastver"
echo "new:  $newver"

rm -rf translations.old.bak
mv translations.old translations.old.bak
cp -r translations/ translations.old

echo doing... ./tools/fetchts.sh
./tools/fetchts.sh

# found diffs?
mkdir diffs
difffile=diffs/$ts.diff
changelog=`date +"%a %b %d %Y"`" "$maintainer
if diff -r -u translations.old translations > $difffile
then
	echo "no differences found"
	log "no differences found"
	exit 0
else
	read -p "create new package? <ctrl-c> to brake | <enter> to continue" usrinput
	log "creating new package: $newver"
	sed -i.$ts "
		/^Release:/ s/$lastver/$newver/
		/%changelog/ a * $changelog
		/%changelog/ a - nightly. changes: $difffile
	" $spec
	./tools/createqm.sh
	./tools/createrpm.sh
	echo rsync releases and diffs to $upload/ ...
	rsync -rav --progress release_rpms/ $upload
	rsync -rav --progress diffs $upload
	ssh $uploadsrvr "cd $uploadpath;"' l=`ls -t *.rpm | sed 1q`;  ln -s -f $l latest.rpm'
	log "done."
fi

rsync -rav --progress log.txt $upload
