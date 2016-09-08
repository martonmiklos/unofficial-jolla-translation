#!/bin/bash

TRANSLATIONS_DIR="../translations"
TEMPLATES_DIR="../templates"
OUTPUT_DIR="../converted_for_pootle"
TARGET_LANG="hu"
TRANSLATION_MEMORY_PATH="../transifex_eng/translations"
TRANSLATION_MEMORY_LANG="en_GB"

retval=0

for d in $TRANSLATIONS_DIR/*/ ; do
    # componentname will be something like: alarm-ui
    componentName=`basename "$d" | sed -E 's/unofficial-jolla-translations\.(.*)/\1/g'`
    
    # do a find in the templates
    # there might be multiple files with the same contents
    for templatePath in $(find $TEMPLATES_DIR -type f -name "$componentName.ts"); do
        # outpath will store something like jolla-alarm-ui/templates
        outpath=`dirname $templatePath | sed -E 's/..\/templates\/(.*)\/templates/\1/g'`
        # create that dir in the output folder
        outpath=$OUTPUT_DIR/$TARGET_LANG/$outpath/$TARGET_LANG
        echo $outpath
        mkdir -p $outpath
        rm -rf $outpath/*
        ./transifex_to_pootle_converter.py $d/hu_HU.ts $templatePath $outpath/$componentName.ts $TARGET_LANG $TRANSLATION_MEMORY_PATH/$d/$TRANSLATION_MEMORY_LANG.ts
        retval=$?
        if [ $retval -ne 0 ]; then
            echo "./transifex_to_pootle_converter.py $d/hu_HU.ts $templatePath $outpath/$componentName.ts $TARGET_LANG $TRANSLATION_MEMORY_PATH/$d/$TRANSLATION_MEMORY_LANGts failed"
            break
        fi
    done
    if [ $retval -ne 0 ]; then
        break
    fi
    #break
done