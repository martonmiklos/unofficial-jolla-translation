#make sure change these variables to suit your language
%define CONFLANG ca
%define LOCNAME el_
%define RPM_SUFFIX ca
%define QM_SUFFIX ca

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.0
Release:	0.0.1
Summary:	Unofficial Catalan language pack for Jolla Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/hu
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Sun Feb 26 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- Firts release
