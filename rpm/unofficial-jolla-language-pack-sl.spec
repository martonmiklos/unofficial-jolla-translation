#make sure change these variables to suit your language
%define CONFLANG sl
%define LOCNAME sl_SI
%define RPM_SUFFIX sl
%define QM_SUFFIX sl

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.0
Release:	0.0.1
Summary:	Unofficial Slovenian language pack for Jolla Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/hu
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Wed Nov 23 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- First build from partially completed translation