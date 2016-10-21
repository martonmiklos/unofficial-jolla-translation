#make sure change these variables to suit your language
%define CONFLANG hu
%define LOCNAME hu_HU
%define RPM_SUFFIX hu
%define QM_SUFFIX hu

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	2.0.5
Release:	0.0.2
Summary:	Nem hivatalos magyar nyelvi csomag

Group: Qt/Qt
License: GPL
URL: https://translate.sailfishos.org/hu
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%include rpm/common.inc

%changelog
* Fri Oct 21 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.2
- Minor changes
- Fixed RPM preinstall script to properly register the language
* Sun Oct 2 2016 Miklos Marton <martonmiklosqdev@gmail.com> 2.0.5-0.0.2
- Minor changes
- Version numbering change to be aligned with the Jolla's version numbering
* Sun Oct 2 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.13
- Minor improvements.
* Tue Sep 27 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.12
- Első release a Transifex -> Pootle migráció után.
- A 2.0.2 releaseben megjelenet stringek lefordítva
* Sat Mar 05 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.11
- Sok apróbb reszelgetés....
* Sat Mar 05 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.10
- Pöckölés/pöccintés/swipe lapozásra cserélve
- Térkép férlefordítások javítva
* Tue Feb 09 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.9
- Minor changes
* Sat Feb 06 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.8
- Minor changes
* Sun Jan 31 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.7
- Minor changes
* Sun Jan 31 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.6
- Pulled and updated translations to SFOS 2.0.1.17
- WLAN -> Wi-fi
- Various minor translation fixes
* Sun Jan 17 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.4
- Pulled and updated translations to SFOS 2.0.0.10
* Mon Jan 11 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.3
- Grammar fixes
* Sun Jan 10 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.2
- Fixed mistakely translated time masks like hh:mm and yyyy mm dd
* Sun Jan 10 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.1
- Created translation package
