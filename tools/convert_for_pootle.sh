#!/bin/bash

TRANSLATIONS_DIR="../translations"
TEMPLATES_DIR="../templates"
OUTPUT_DIR="../converted_for_pootle"
retval=0
for d in $TRANSLATIONS_DIR/*/ ; do
    # componentname will be something like: alarm-ui
    componentName=`basename "$d" | sed -E 's/unofficial-jolla-translations\.(.*)/\1/g'`
    
    # do a find in the templates
    # there might be multiple files with the same contents
    for templatePath in $(find $TEMPLATES_DIR -type f -name "$componentName.ts"); do # Not recommended, will break on whitespace
        # outpath will store something like jolla-alarm-ui/templates
        outpath=`dirname $templatePath | sed -E 's/..\/templates\/(.*)/\1/g'`
        # create that dir in the output folder
        mkdir -p $OUTPUT_DIR/$outpath
        ./transifex_to_pootle_converter.py $d/hu_HU.ts $templatePath $OUTPUT_DIR/$outpath/$componentName.ts
        retval=$?
        if [ $retval -ne 0 ]; then
            echo "./transifex_to_pootle_converter.py $d/hu_HU.ts $templatePath $OUTPUT_DIR/$outpath/$componentName.ts failed"
            break
        fi
    done
    if [ $retval -ne 0 ]; then
        break
    fi
    #break
done