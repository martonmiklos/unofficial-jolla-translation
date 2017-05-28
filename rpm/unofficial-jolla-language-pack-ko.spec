#make sure change these variables to suit your language
%define CONFLANG ko
%define LOCNAME ko_KR
%define RPM_SUFFIX ko
%define QM_SUFFIX ko

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.0
Release:	0.0.3
Summary:	Korean community language pack

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/ko
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Shinjo Park

%include rpm/common.inc

%changelog
* Wed Feb 08 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.2
- Updated from pootle to make translation up to date with the just released 2.1.0

* Fri Dec 09 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- First build for openrepos

* Thu Dec 08 2016 Shinjo Park <me@peremen.name> 2.0.5-0.0.1
- Migrate to use Sailfish OS Pootle

* Sun Oct 16 2016 Shinjo Park <me@peremen.name> 2.0.4.14-1
- Update translations

* Sun Jan 24 2016 Shinjo Park <me@peremen.name> 2.0.1.7-1
- Update translations

* Fri Sep 11 2015 Shinjo Park <me@peremen.name> 1.1.9.28-1
- Update translations

* Sun May 10 2015 Shinjo Park <me@peremen.name> 1.1.4.29-2
- Update typo on translation

* Sun May 10 2015 Shinjo Park <me@peremen.name> 1.1.4.29-1
- Update translations

* Sun Oct 26 2014 Shinjo Park <me@peremen.name> 1.1.0.39-1
- Update translations

* Fri Jun 20 2014 Shinjo Park <me@peremen.name> 1.0.7.16-1
- Initial translations
- Based on Takahiro HASHIMOTO's package
