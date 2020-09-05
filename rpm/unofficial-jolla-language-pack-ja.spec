#make sure change these variables to suit your language
%define CONFLANG ja
%define LOCNAME ja_JP
%define RPM_SUFFIX ja
%define QM_SUFFIX ja

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	3.4.0
Release:	0.0.1
Summary:	Unofficial Japanese language pack for Jolla Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/hu
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Mon Aug 17 2020 Miklos Marton <martonmiklosqdev@gmail.com> 3.4.0-0.0.1
- Generate updated RPM as per ttpr's request
* Wed Feb 08 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.2
- Updated from pootle to make translation up to date with the just released 2.1.0
* Thu Nov 24 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- First release
