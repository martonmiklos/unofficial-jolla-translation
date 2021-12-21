#make sure change these variables to suit your language
%define CONFLANG lv
%define LOCNAME lv_LV
%define RPM_SUFFIX lv
%define QM_SUFFIX lv

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	0.0.1
Release:	1
Summary:	Latvian translation for Sailfish OS

Group: Qt/Qt
License: BSD-3-clause
URL: https://translate.sailfishos.org/lv
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: sledges

%include rpm/common.inc

%changelog
* Tue Dec 21 2020 sledges <sledges@meramo.co.uk>
- first alpha release

