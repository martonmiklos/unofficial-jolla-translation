#make sure change these variables to suit your language
%define CONFLANG id
%define LOCNAME id_ID
%define RPM_SUFFIX id
%define QM_SUFFIX id

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	3.2.0
Release:	0.0.2
Summary:	Community Bahasa Indonesia pack for the Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/id
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Fandy Permana

%include rpm/common.inc

%changelog
* Mon Oct 11 2019 Fandy Permana <fpermana@outlook.com> 3.2.0-0.0.2
- Initiate.

