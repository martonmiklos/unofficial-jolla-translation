# Various scripts for building RPM packages for the community languages

You can find the translation portal here:
https://translate.sailfishos.org

Building an RPM requires the following things:
- Translation project on the Pootle
- RPM spec file in the rpm folder with: unofficial-jolla-language-pack-langcode.spec filename
- Language file with the langcode.conf filename in the usr/share/jolla-supported-languages/ folder
- lrelease in the path (could be installed by installing the Qt Linguist or other Qt dev tools) for creating the qm files.
- wget, awk, bash, rpm, other standard Linux utilities

RPM build process:
// all commands executed from the checked out folder
export POOTLE_LANG=langcode; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=langcode; export QM_SUFFIX=langcode; ./tools/createqm.sh 
export LANGCODE=langcode; ./tools/createrpm.sh 

You can additionally install the package with the ./tools/install_on_device.sh. The script requires to have the jolla DNS name to be resolved to your device's address. 

If you would like to create a package for a new language please let me know with an issue or a PR.

For hungarian
export POOTLE_LANG=hu; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=hu; export QM_SUFFIX=hu; ./tools/createqm.sh 
export LANGCODE=hu; ./tools/createrpm.sh 

export POOTLE_LANG=nl; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=nl; export QM_SUFFIX=nl; ./tools/createqm.sh 
export LANGCODE=nl; ./tools/createrpm.sh 

export POOTLE_LANG=zh_TW; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=zh_TW; export QM_SUFFIX=zh_TW; ./tools/createqm.sh 
export LANGCODE=zh_TW; ./tools/createrpm.sh 

export POOTLE_LANG=el; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=el; export QM_SUFFIX=el; ./tools/createqm.sh 
export LANGCODE=el; ./tools/createrpm.sh 

export POOTLE_LANG=sl; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=sl; export QM_SUFFIX=sl; ./tools/createqm.sh 
export LANGCODE=sl; ./tools/createrpm.sh 

export POOTLE_LANG=ja; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=ja; export QM_SUFFIX=ja; ./tools/createqm.sh 
export LANGCODE=ja; ./tools/createrpm.sh 

export POOTLE_LANG=ko; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=ko; export QM_SUFFIX=ko; ./tools/createqm.sh 
export LANGCODE=ko; ./tools/createrpm.sh 

export POOTLE_LANG=ca; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=ca; export QM_SUFFIX=ca; ./tools/createqm.sh 
export LANGCODE=ca; ./tools/createrpm.sh 

export POOTLE_LANG=pt_BR; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=pt_BR; export QM_SUFFIX=pt_BR; ./tools/createqm.sh 
export LANGCODE=pt_BR; ./tools/createrpm.sh 

export POOTLE_LANG=et; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=et; export QM_SUFFIX=et; ./tools/createqm.sh 
export LANGCODE=et; ./tools/createrpm.sh 

export POOTLE_LANG=tr; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=tr; export QM_SUFFIX=tr; ./tools/createqm.sh 
export LANGCODE=tr; ./tools/createrpm.sh

export POOTLE_LANG=bg QM_SUFFIX=bg LANGCODE=bg
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh
