# Various scripts for building RPM packages for the community languages

You can find the translation portal here:
https://translate.sailfishos.org

Building an RPM requires the following things:
- Translation project on the Pootle
- RPM spec file in the rpm folder with: unofficial-jolla-language-pack-langcode.spec filename
- Language file with the langcode.conf filename in the usr/share/jolla-supported-languages/ folder
- lrelease in the path (could be installed by installing the Qt Linguist or other Qt dev tools) for creating the qm files.
- wget, awk, bash, other standard Linux utilities

RPM build process:
// all commands executed from the checked out folder
export POOTLE_LANG=langcode; ./tools/fetchts.sh # this will take a while because it downloads the ts files from Pootle
export POOTLE_LANG=langcode; export QM_SUFFIX=langcode; ./tools/createqm.sh 
export LANGCODE=langcode; ./tools/createrpm.sh 

You can additionally install the package with the ./tools/install_on_device.sh. The script requires to have the jolla DNS name to be resolved to your device's address. 

If you would like to create a package for a new language please let me know with an issue or a PR.
