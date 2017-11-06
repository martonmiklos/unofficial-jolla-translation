#make sure change these variables to suit your language
%define CONFLANG tr
%define LOCNAME tr_TR
%define RPM_SUFFIX tr
%define QM_SUFFIX tr

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:    2.1.3
Release:    0.0.1
Summary:    Resmi Olmayan Türkçe Dil Paketi

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/tr
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Mon Nov 06 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.3-0.0.1
- First release to openrepos
* Wed Feb 08 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- First release
