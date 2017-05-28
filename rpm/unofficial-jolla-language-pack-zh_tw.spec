#make sure change these variables to suit your language
%define CONFLANG zh_TW
%define LOCNAME zh_TW
%define RPM_SUFFIX zh_tw
%define QM_SUFFIX zh_TW

Name: unofficial-jolla-language-pack-%{RPM_SUFFIX}
Version:	2.0.5
Release:	0.0.3
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
* Wed Mar 01 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.3
- Changed language name to make it consistent
* Thu Feb 28 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.2
- First RPM build after completing the whole translation
* Sun Oct 2 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.1
- First RPM build
