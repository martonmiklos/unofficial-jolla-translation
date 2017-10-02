#make sure change these variables to suit your language
%define CONFLANG nl
%define LOCNAME nl_NL
%define RPM_SUFFIX nl
%define QM_SUFFIX nl

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.1.2
Release:	0.0.2
Summary:	Community Nederlands language pack for the Sailfish OS

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/nl
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Mon Oct 02 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.2-0.0.2
- Moved localedef from post to preinstall section and swallow the returncode.
This should fix the locale related issues.
* Sun Oct 01 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.2-0.0.1
- Updated from pootle to make translation up to date
- RPM installation script fixed: generates the locale properly
* Thu Feb 28 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.2
- Updated from pootle to make translation up to date
* Wed Feb 08 2017 Miklos Marton <martonmiklosqdev@gmail.com> 2.1.0-0.0.1
- Updated from pootle to make translation up to date with the just released 2.1.0
* Fri Oct 21 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.3
- Fixed RPM preinstall script to properly register the language
* Sun Oct 2 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.2
- Minor changes
- Version numbering change to be aligned with the Jolla's version numbering
* Sun Oct 2 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.1
- First RPM build after the Nederlands community translation is finished
