#make sure change these variables to suit your language
%define CONFLANG sk
%define LOCNAME sk_SK
%define RPM_SUFFIX sk
%define QM_SUFFIX sk

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	3.4.0
Release:	0.0.1
Summary:	Unofficial Slovak language pack for Jolla Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/sk
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Fri Sep 04 2020 Miklos Marton <martonmiklosqdev@gmail.com> 3.4.0-0.0.1
- Updated from pootle
