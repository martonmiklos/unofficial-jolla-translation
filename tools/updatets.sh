TSLANG=hu_HU

LCONVERT=/home/mm/Projektek/jolla/qttools-opensource-src-5.3.2/bin/lconvert

for i in tsfiles/*en_GB.ts; 
do 
	COMPNAME="$(echo $i | sed -e "s/tsfiles\/\(.*\)-en_GB.ts/\1/";)";
	TSFILE=translations/unofficial-jolla-translations.$COMPNAME/$TSLANG.ts
	if [ -f $TSFILE ]; then
		${LCONVERT} -i $i -o $TSFILE -keep-translations    
	else
		echo $TSFILE
		echo "File not found!"
		mkdir -p translations/unofficial-jolla-translations.$COMPNAME
		${LCONVERT} -i $i -o $TSFILE -mark-all-unfinished
	fi
done;

for i in tsfiles/*eng_en.ts; 
do 
	COMPNAME="$(echo $i | sed -e "s/tsfiles\/\(.*\)_eng_en.ts/\1/";)";
	TSFILE=translations/unofficial-jolla-translations.$COMPNAME/$TSLANG.ts
	if [ -f $TSFILE ]; then
		${LCONVERT} -i $i -o $TSFILE -keep-translations    
	else
		echo $TSFILE
		echo "File not found!"
		mkdir -p translations/unofficial-jolla-translations.$COMPNAME
		${LCONVERT} -i $i -o $TSFILE -mark-all-unfinished
	fi
done;
