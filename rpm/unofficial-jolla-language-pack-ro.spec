#make sure change these variables to suit your language
%define CONFLANG ro
%define LOCNAME ro_RO
%define RPM_SUFFIX ro
%define QM_SUFFIX ro

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.2
Release:	0.0.1
Summary:	Unofficial Romanian community translation for Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/bg
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: fnkka

%include rpm/common.inc

%changelog
* Wed Apr 17 2019 fnkka <fnkka@mailbox.org>
- first release

