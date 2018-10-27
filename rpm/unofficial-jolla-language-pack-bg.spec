#make sure change these variables to suit your language
%define CONFLANG bg
%define LOCNAME bg_BG
%define RPM_SUFFIX bg
%define QM_SUFFIX bg

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.2
Release:	0.1.0
Summary:	Unofficial Bulgarian community translation for Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/bg
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: omkpuBamev

%include rpm/common.inc

%changelog
* Fri Oct 26 2018 omkpuBamev
- first published package. Full translation.
* Mon Sep 17 2018 omkpuBamev 
- Initial translation package with 99% translated strings
