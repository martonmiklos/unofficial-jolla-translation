#make sure change these variables to suit your language
%define CONFLANG uk
%define LOCNAME uk_UA
%define RPM_SUFFIX uk
%define QM_SUFFIX uk

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	0.1.0
Release:	0.0.1
Summary:	Unofficial Ukrainian language pack for Jolla Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/uk
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Vitalii Koreniev

%include rpm/common.inc

%changelog
* Mon Aug 15 2022 Vitalii Koreniev <nemish94@gmail.com> 0.1.0-0.0.1
- First release
