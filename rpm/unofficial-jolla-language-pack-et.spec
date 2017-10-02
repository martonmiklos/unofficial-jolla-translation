#make sure change these variables to suit your language
%define CONFLANG et
%define LOCNAME et_EE
%define RPM_SUFFIX et
%define QM_SUFFIX et

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.2
Release:	0.0.3
Summary:	Unofficial Estonian language pack for Jolla Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/hu
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Mon Oct 02 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.2-0.0.3
- Fixed case of the language name and the Localecode in the conf file
* Mon Oct 02 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.2-0.0.2
- Moved localedef from post to preinstall section and swallow the returncode.
This should fix the locale related issues.

* Mon Oct 02 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.2-0.0.1
- Translation update
- RPM postinst script should generate the locale properly

* Mon May 29 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.2
- Translation update

* Mon May 29 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- First RPM build for openrepos
