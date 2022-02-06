#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libksieve
Version  : 21.12.2
Release  : 36
URL      : https://download.kde.org/stable/release-service/21.12.2/src/libksieve-21.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.2/src/libksieve-21.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.2/src/libksieve-21.12.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: libksieve-data = %{version}-%{release}
Requires: libksieve-lib = %{version}-%{release}
Requires: libksieve-license = %{version}-%{release}
Requires: libksieve-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules-data
BuildRequires : karchive-dev
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kio-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : knewstuff-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libkdepim-dev
BuildRequires : pimcommon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev
BuildRequires : syntax-highlighting-dev

%description
This is a legacy code to read/write the old vacation scripts for KDE 4 version of kontact.
If once this new version is rolled out, there is no need to keep the legacy way of read/write the vacation script,
because it is not compatible to any other system. The only need to keep this code is for migration old vacation scripts to new one.

%package data
Summary: data components for the libksieve package.
Group: Data

%description data
data components for the libksieve package.


%package dev
Summary: dev components for the libksieve package.
Group: Development
Requires: libksieve-lib = %{version}-%{release}
Requires: libksieve-data = %{version}-%{release}
Provides: libksieve-devel = %{version}-%{release}
Requires: libksieve = %{version}-%{release}

%description dev
dev components for the libksieve package.


%package doc
Summary: doc components for the libksieve package.
Group: Documentation

%description doc
doc components for the libksieve package.


%package lib
Summary: lib components for the libksieve package.
Group: Libraries
Requires: libksieve-data = %{version}-%{release}
Requires: libksieve-license = %{version}-%{release}

%description lib
lib components for the libksieve package.


%package license
Summary: license components for the libksieve package.
Group: Default

%description license
license components for the libksieve package.


%package locales
Summary: locales components for the libksieve package.
Group: Default

%description locales
locales components for the libksieve package.


%prep
%setup -q -n libksieve-21.12.2
cd %{_builddir}/libksieve-21.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644177710
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644177710
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksieve
cp %{_builddir}/libksieve-21.12.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libksieve/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/libksieve-21.12.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/libksieve-21.12.2/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/libksieve-21.12.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/libksieve-21.12.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/libksieve-21.12.2/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang kio_sieve
%find_lang libksieve

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/knsrcfiles/ksieve_script.knsrc
/usr/share/qlogging-categories5/libksieve.categories
/usr/share/qlogging-categories5/libksieve.renamecategories
/usr/share/sieve/scripts/copy/template.desktop
/usr/share/sieve/scripts/copy/template.txt

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KManageSieve/SieveJob
/usr/include/KF5/KSieveUi/AbstractMoveImapFolderWidget
/usr/include/KF5/KSieveUi/AbstractRegexpEditorLineEdit
/usr/include/KF5/KSieveUi/AbstractSelectEmailLineEdit
/usr/include/KF5/KSieveUi/CheckScriptJob
/usr/include/KF5/KSieveUi/ManageSieveScriptsDialog
/usr/include/KF5/KSieveUi/ManageSieveTreeView
/usr/include/KF5/KSieveUi/ManageSieveWidget
/usr/include/KF5/KSieveUi/MultiImapVacationDialog
/usr/include/KF5/KSieveUi/MultiImapVacationManager
/usr/include/KF5/KSieveUi/RenameScriptJob
/usr/include/KF5/KSieveUi/SieveDebugDialog
/usr/include/KF5/KSieveUi/SieveEditor
/usr/include/KF5/KSieveUi/SieveEditorWidget
/usr/include/KF5/KSieveUi/SieveImapAccountSettings
/usr/include/KF5/KSieveUi/SieveImapInstance
/usr/include/KF5/KSieveUi/SieveImapInstanceInterface
/usr/include/KF5/KSieveUi/SieveImapInstanceInterfaceManager
/usr/include/KF5/KSieveUi/SieveImapPasswordProvider
/usr/include/KF5/KSieveUi/SieveTreeWidgetItem
/usr/include/KF5/KSieveUi/Util
/usr/include/KF5/KSieveUi/VacationManager
/usr/include/KF5/kmanagesieve/kmanagesieve_export.h
/usr/include/KF5/kmanagesieve/sievejob.h
/usr/include/KF5/ksieveui/abstractmoveimapfolderwidget.h
/usr/include/KF5/ksieveui/abstractregexpeditorlineedit.h
/usr/include/KF5/ksieveui/abstractselectemaillineedit.h
/usr/include/KF5/ksieveui/checkscriptjob.h
/usr/include/KF5/ksieveui/ksieveui_export.h
/usr/include/KF5/ksieveui/managesievescriptsdialog.h
/usr/include/KF5/ksieveui/managesievetreeview.h
/usr/include/KF5/ksieveui/managesievewidget.h
/usr/include/KF5/ksieveui/multiimapvacationdialog.h
/usr/include/KF5/ksieveui/multiimapvacationmanager.h
/usr/include/KF5/ksieveui/renamescriptjob.h
/usr/include/KF5/ksieveui/sievedebugdialog.h
/usr/include/KF5/ksieveui/sieveeditor.h
/usr/include/KF5/ksieveui/sieveeditorwidget.h
/usr/include/KF5/ksieveui/sieveimapaccountsettings.h
/usr/include/KF5/ksieveui/sieveimapinstance.h
/usr/include/KF5/ksieveui/sieveimapinstanceinterface.h
/usr/include/KF5/ksieveui/sieveimapinstanceinterfacemanager.h
/usr/include/KF5/ksieveui/sieveimappasswordprovider.h
/usr/include/KF5/ksieveui/sievetreewidgetitem.h
/usr/include/KF5/ksieveui/util.h
/usr/include/KF5/ksieveui/util_p.h
/usr/include/KF5/ksieveui/vacationmanager.h
/usr/include/KF5/libksieve_version.h
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveConfig.cmake
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveConfigVersion.cmake
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveTargets.cmake
/usr/lib64/libKF5KManageSieve.so
/usr/lib64/libKF5KSieve.so
/usr/lib64/libKF5KSieveUi.so
/usr/lib64/qt5/mkspecs/modules/qt_KManageSieve.pri
/usr/lib64/qt5/mkspecs/modules/qt_KSieve.pri
/usr/lib64/qt5/mkspecs/modules/qt_KSieveUi.pri

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/de/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/en/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/es/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/et/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/fr/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/it/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/ko/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/ko/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/nl/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/pt/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/ru/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/sr/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/sv/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/sieve/index.docbook
/usr/share/doc/HTML/uk/kioslave5/sieve/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/sieve/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KManageSieve.so.5
/usr/lib64/libKF5KManageSieve.so.5.19.2
/usr/lib64/libKF5KSieve.so.5
/usr/lib64/libKF5KSieve.so.5.19.2
/usr/lib64/libKF5KSieveUi.so.5
/usr/lib64/libKF5KSieveUi.so.5.19.2
/usr/lib64/qt5/plugins/kf5/kio/sieve.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libksieve/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kio_sieve.lang -f libksieve.lang
%defattr(-,root,root,-)

