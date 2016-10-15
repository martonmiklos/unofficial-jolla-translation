#make sure change these variables to suit your language
%define CONFLANG zh_TW
%define LOCNAME zh_TW
%define RPM_SUFFIX zh_tw

Name: unofficial-jolla-language-pack-%{RPM_SUFFIX}
Version:	2.0.5
Release:	0.0.1
Summary:	Unofficial community Taiwanese translation for Jolla

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/zh_TW
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Sun Oct 2 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.1
- First RPM build
