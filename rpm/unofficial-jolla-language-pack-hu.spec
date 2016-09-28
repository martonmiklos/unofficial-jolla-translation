#make sure change these variables to suit your language
%define CONFLANG hu
%define LOCNAME %{CONFLANG}

Name: unofficial-jolla-language-pack-%{CONFLANG}
Version:	1.0.0
Release:	0.0.12
Summary:	Nem hivatalos magyar nyelvi csomag

Group: Qt/Qt
License: GPL
URL: http://codereview.qt-users.jp
Source0: %{name}.tar.bz2
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-XXXXXX
Packager: Miklós Márton

%define INSTALLDIR %{buildroot}/usr/share

%description
%{summary}

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{INSTALLDIR}
mkdir -p %{INSTALLDIR}/{translations,jolla-supported-languages}
echo $PWD
cp -a usr/share/translations/*-%{LOCNAME}.qm %{INSTALLDIR}/translations/
cp -a usr/share/jolla-supported-languages/%{CONFLANG}.conf %{INSTALLDIR}/jolla-supported-languages/

%clean
rm -rf ${buildroot}

%files
%{_datadir}/translations/*-%{LOCNAME}.qm
%{_datadir}/jolla-supported-languages/%{CONFLANG}.conf

%post
localedef -i %{LOCNAME} -f UTF-8 %{LOCNAME}.utf8

%postun
localedef --delete-from-archive %{LOCNAME}.utf8

%changelog
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
* Sun Feb 06 2016 Miklos Marton <martonmiklosqdev@gmail.com> 1.0.0-0.0.8
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
