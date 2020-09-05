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
export POOTLE_LANG=langcode QM_SUFFIX=langcode LANGCODE=langcode
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

You can additionally install the package with the ./tools/install_on_device.sh. The script requires to have the jolla DNS name to be resolved to your device's address. 

If you would like to create a package for a new language please let me know with an issue or a PR.

For hungarian
export POOTLE_LANG=hu QM_SUFFIX=hu LANGCODE=hu
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=nl QM_SUFFIX=nl LANGCODE=nl
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=zh_TW QM_SUFFIX=zh_TW LANGCODE=zh_TW
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=el QM_SUFFIX=el LANGCODE=el
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=sl QM_SUFFIX=sl LANGCODE=sl
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=ja QM_SUFFIX=ja LANGCODE=ja
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=ko QM_SUFFIX=ko LANGCODE=ko
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=ca QM_SUFFIX=ca LANGCODE=ca
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=pt_BR QM_SUFFIX=pt_BR LANGCODE=pt_BR
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=et QM_SUFFIX=et LANGCODE=et
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=tr QM_SUFFIX=tr LANGCODE=tr
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=bg QM_SUFFIX=bg LANGCODE=bg
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=ro QM_SUFFIX=ro LANGCODE=ro
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=id QM_SUFFIX=id LANGCODE=id
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh

export POOTLE_LANG=sk QM_SUFFIX=sk LANGCODE=sk
./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
./tools/createqm.sh
./tools/createrpm.sh
