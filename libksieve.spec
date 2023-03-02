#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libksieve
Version  : 22.12.3
Release  : 50
URL      : https://download.kde.org/stable/release-service/22.12.3/src/libksieve-22.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.3/src/libksieve-22.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.3/src/libksieve-22.12.3.tar.xz.sig
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
BuildRequires : qt6base-dev
BuildRequires : qtwebengine-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

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
%setup -q -n libksieve-22.12.3
cd %{_builddir}/libksieve-22.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677799398
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1677799398
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksieve
cp %{_builddir}/libksieve-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/libksieve/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/libksieve-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libksieve/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libksieve/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libksieve-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/libksieve-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libksieve-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd
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
/usr/include/KF5/KManageSieve/KManageSieve/SieveJob
/usr/include/KF5/KManageSieve/kmanagesieve/kmanagesieve_export.h
/usr/include/KF5/KManageSieve/kmanagesieve/sievejob.h
/usr/include/KF5/KSieve/libksieve_version.h
/usr/include/KF5/KSieveUi/KSieveUi/AbstractMoveImapFolderWidget
/usr/include/KF5/KSieveUi/KSieveUi/AbstractRegexpEditorLineEdit
/usr/include/KF5/KSieveUi/KSieveUi/AbstractSelectEmailLineEdit
/usr/include/KF5/KSieveUi/KSieveUi/CheckScriptJob
/usr/include/KF5/KSieveUi/KSieveUi/ManageSieveScriptsDialog
/usr/include/KF5/KSieveUi/KSieveUi/ManageSieveTreeView
/usr/include/KF5/KSieveUi/KSieveUi/ManageSieveWidget
/usr/include/KF5/KSieveUi/KSieveUi/MultiImapVacationDialog
/usr/include/KF5/KSieveUi/KSieveUi/MultiImapVacationManager
/usr/include/KF5/KSieveUi/KSieveUi/RenameScriptJob
/usr/include/KF5/KSieveUi/KSieveUi/SieveDebugDialog
/usr/include/KF5/KSieveUi/KSieveUi/SieveEditor
/usr/include/KF5/KSieveUi/KSieveUi/SieveEditorWidget
/usr/include/KF5/KSieveUi/KSieveUi/SieveImapAccountSettings
/usr/include/KF5/KSieveUi/KSieveUi/SieveImapInstance
/usr/include/KF5/KSieveUi/KSieveUi/SieveImapInstanceInterface
/usr/include/KF5/KSieveUi/KSieveUi/SieveImapInstanceInterfaceManager
/usr/include/KF5/KSieveUi/KSieveUi/SieveImapPasswordProvider
/usr/include/KF5/KSieveUi/KSieveUi/SieveTreeWidgetItem
/usr/include/KF5/KSieveUi/KSieveUi/Util
/usr/include/KF5/KSieveUi/KSieveUi/VacationManager
/usr/include/KF5/KSieveUi/ksieveui/abstractmoveimapfolderwidget.h
/usr/include/KF5/KSieveUi/ksieveui/abstractregexpeditorlineedit.h
/usr/include/KF5/KSieveUi/ksieveui/abstractselectemaillineedit.h
/usr/include/KF5/KSieveUi/ksieveui/checkscriptjob.h
/usr/include/KF5/KSieveUi/ksieveui/ksieveui_export.h
/usr/include/KF5/KSieveUi/ksieveui/managesievescriptsdialog.h
/usr/include/KF5/KSieveUi/ksieveui/managesievetreeview.h
/usr/include/KF5/KSieveUi/ksieveui/managesievewidget.h
/usr/include/KF5/KSieveUi/ksieveui/multiimapvacationdialog.h
/usr/include/KF5/KSieveUi/ksieveui/multiimapvacationmanager.h
/usr/include/KF5/KSieveUi/ksieveui/renamescriptjob.h
/usr/include/KF5/KSieveUi/ksieveui/sievedebugdialog.h
/usr/include/KF5/KSieveUi/ksieveui/sieveeditor.h
/usr/include/KF5/KSieveUi/ksieveui/sieveeditorwidget.h
/usr/include/KF5/KSieveUi/ksieveui/sieveimapaccountsettings.h
/usr/include/KF5/KSieveUi/ksieveui/sieveimapinstance.h
/usr/include/KF5/KSieveUi/ksieveui/sieveimapinstanceinterface.h
/usr/include/KF5/KSieveUi/ksieveui/sieveimapinstanceinterfacemanager.h
/usr/include/KF5/KSieveUi/ksieveui/sieveimappasswordprovider.h
/usr/include/KF5/KSieveUi/ksieveui/sievetreewidgetitem.h
/usr/include/KF5/KSieveUi/ksieveui/util.h
/usr/include/KF5/KSieveUi/ksieveui/util_p.h
/usr/include/KF5/KSieveUi/ksieveui/vacationmanager.h
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveConfig.cmake
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveConfigVersion.cmake
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5LibKSieve/KF5LibKSieveTargets.cmake
/usr/lib64/libKF5KManageSieve.so
/usr/lib64/libKF5KSieve.so
/usr/lib64/libKF5KSieveUi.so
/usr/lib64/qt5/mkspecs/modules/qt_KManageSieve.pri
/usr/lib64/qt5/mkspecs/modules/qt_KSieveUi.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KManageSieve.so.5
/usr/lib64/libKF5KManageSieve.so.5.22.3
/usr/lib64/libKF5KSieve.so.5
/usr/lib64/libKF5KSieve.so.5.22.3
/usr/lib64/libKF5KSieveUi.so.5
/usr/lib64/libKF5KSieveUi.so.5.22.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libksieve/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libksieve/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/libksieve/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libksieve.lang
%defattr(-,root,root,-)

