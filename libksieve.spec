#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libksieve
Version  : 24.12.0
Release  : 103
URL      : https://download.kde.org/stable/release-service/24.12.0/src/libksieve-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/libksieve-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/libksieve-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: libksieve-data = %{version}-%{release}
Requires: libksieve-lib = %{version}-%{release}
Requires: libksieve-license = %{version}-%{release}
Requires: libksieve-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : libkdepim-dev
BuildRequires : pimcommon-dev
BuildRequires : pkgconfig(libsasl2)
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libksieve-24.12.0
cd %{_builddir}/libksieve-24.12.0
pushd ..
cp -a libksieve-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735318663
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735318663
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksieve
cp %{_builddir}/libksieve-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libksieve/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libksieve-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/libksieve-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libksieve-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/libksieve-%{version}/readme-build-ftime.txt.license %{buildroot}/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libksieve6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/knsrcfiles/ksieve_script.knsrc
/usr/share/qlogging-categories6/libksieve.categories
/usr/share/qlogging-categories6/libksieve.renamecategories
/usr/share/sieve/scripts/copy/template.desktop
/usr/share/sieve/scripts/copy/template.txt

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KManageSieve/KManageSieve/SieveJob
/usr/include/KPim6/KManageSieve/kmanagesieve/kmanagesieve_export.h
/usr/include/KPim6/KManageSieve/kmanagesieve/sievejob.h
/usr/include/KPim6/KManageSieve/libkmanagesieve_version.h
/usr/include/KPim6/KSieve/libksieve_version.h
/usr/include/KPim6/KSieveCore/KSieveCore/CheckScriptJob
/usr/include/KPim6/KSieveCore/KSieveCore/MultiImapVacationManager
/usr/include/KPim6/KSieveCore/KSieveCore/ParsingUtil
/usr/include/KPim6/KSieveCore/KSieveCore/RenameScriptJob
/usr/include/KPim6/KSieveCore/KSieveCore/SearchServerWithVacationSupportJob
/usr/include/KPim6/KSieveCore/KSieveCore/SieveImapAccountSettings
/usr/include/KPim6/KSieveCore/KSieveCore/SieveImapInstance
/usr/include/KPim6/KSieveCore/KSieveCore/SieveImapInstanceInterface
/usr/include/KPim6/KSieveCore/KSieveCore/SieveImapInstanceInterfaceManager
/usr/include/KPim6/KSieveCore/KSieveCore/SieveImapPasswordProvider
/usr/include/KPim6/KSieveCore/KSieveCore/Util
/usr/include/KPim6/KSieveCore/KSieveCore/VacationCheckJob
/usr/include/KPim6/KSieveCore/KSieveCore/VacationCreateScriptJob
/usr/include/KPim6/KSieveCore/KSieveCore/VacationUtils
/usr/include/KPim6/KSieveCore/KSieveCore/XMLPrintingScriptBuilder
/usr/include/KPim6/KSieveCore/ksievecore/checkscriptjob.h
/usr/include/KPim6/KSieveCore/ksievecore/ksievecore_export.h
/usr/include/KPim6/KSieveCore/ksievecore/multiimapvacationmanager.h
/usr/include/KPim6/KSieveCore/ksievecore/parsingutil.h
/usr/include/KPim6/KSieveCore/ksievecore/renamescriptjob.h
/usr/include/KPim6/KSieveCore/ksievecore/searchserverwithvacationsupportjob.h
/usr/include/KPim6/KSieveCore/ksievecore/sieve-vacation.h
/usr/include/KPim6/KSieveCore/ksievecore/sieveimapaccountsettings.h
/usr/include/KPim6/KSieveCore/ksievecore/sieveimapinstance.h
/usr/include/KPim6/KSieveCore/ksievecore/sieveimapinstanceinterface.h
/usr/include/KPim6/KSieveCore/ksievecore/sieveimapinstanceinterfacemanager.h
/usr/include/KPim6/KSieveCore/ksievecore/sieveimappasswordprovider.h
/usr/include/KPim6/KSieveCore/ksievecore/util.h
/usr/include/KPim6/KSieveCore/ksievecore/vacationcheckjob.h
/usr/include/KPim6/KSieveCore/ksievecore/vacationcreatescriptjob.h
/usr/include/KPim6/KSieveCore/ksievecore/vacationutils.h
/usr/include/KPim6/KSieveCore/ksievecore/xmlprintingscriptbuilder.h
/usr/include/KPim6/KSieveCore/libksievecore_version.h
/usr/include/KPim6/KSieveUi/KSieveUi/AbstractMoveImapFolderWidget
/usr/include/KPim6/KSieveUi/KSieveUi/AbstractRegexpEditorLineEdit
/usr/include/KPim6/KSieveUi/KSieveUi/AbstractSelectEmailLineEdit
/usr/include/KPim6/KSieveUi/KSieveUi/ManageSieveScriptsDialog
/usr/include/KPim6/KSieveUi/KSieveUi/ManageSieveTreeView
/usr/include/KPim6/KSieveUi/KSieveUi/ManageSieveWidget
/usr/include/KPim6/KSieveUi/KSieveUi/MultiImapVacationDialog
/usr/include/KPim6/KSieveUi/KSieveUi/SieveDebugDialog
/usr/include/KPim6/KSieveUi/KSieveUi/SieveEditor
/usr/include/KPim6/KSieveUi/KSieveUi/SieveEditorWidget
/usr/include/KPim6/KSieveUi/KSieveUi/SieveTreeWidgetItem
/usr/include/KPim6/KSieveUi/KSieveUi/VacationManager
/usr/include/KPim6/KSieveUi/ksieveui/abstractmoveimapfolderwidget.h
/usr/include/KPim6/KSieveUi/ksieveui/abstractregexpeditorlineedit.h
/usr/include/KPim6/KSieveUi/ksieveui/abstractselectemaillineedit.h
/usr/include/KPim6/KSieveUi/ksieveui/ksieveui_export.h
/usr/include/KPim6/KSieveUi/ksieveui/managesievescriptsdialog.h
/usr/include/KPim6/KSieveUi/ksieveui/managesievetreeview.h
/usr/include/KPim6/KSieveUi/ksieveui/managesievewidget.h
/usr/include/KPim6/KSieveUi/ksieveui/multiimapvacationdialog.h
/usr/include/KPim6/KSieveUi/ksieveui/sievedebugdialog.h
/usr/include/KPim6/KSieveUi/ksieveui/sieveeditor.h
/usr/include/KPim6/KSieveUi/ksieveui/sieveeditorwidget.h
/usr/include/KPim6/KSieveUi/ksieveui/sievetreewidgetitem.h
/usr/include/KPim6/KSieveUi/ksieveui/vacationmanager.h
/usr/include/KPim6/KSieveUi/libksieveui_version.h
/usr/lib64/cmake/KPim6KManageSieve/KPim6KManageSieveConfig.cmake
/usr/lib64/cmake/KPim6KManageSieve/KPim6KManageSieveConfigVersion.cmake
/usr/lib64/cmake/KPim6KManageSieve/KPim6KManageSieveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6KManageSieve/KPim6KManageSieveTargets.cmake
/usr/lib64/cmake/KPim6KSieve/KPim6KSieveConfig.cmake
/usr/lib64/cmake/KPim6KSieve/KPim6KSieveConfigVersion.cmake
/usr/lib64/cmake/KPim6KSieve/KPim6KSieveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6KSieve/KPim6KSieveTargets.cmake
/usr/lib64/cmake/KPim6KSieveCore/KPim6KSieveCoreConfig.cmake
/usr/lib64/cmake/KPim6KSieveCore/KPim6KSieveCoreConfigVersion.cmake
/usr/lib64/cmake/KPim6KSieveCore/KPim6KSieveCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6KSieveCore/KPim6KSieveCoreTargets.cmake
/usr/lib64/cmake/KPim6KSieveUi/KPim6KSieveUiConfig.cmake
/usr/lib64/cmake/KPim6KSieveUi/KPim6KSieveUiConfigVersion.cmake
/usr/lib64/cmake/KPim6KSieveUi/KPim6KSieveUiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6KSieveUi/KPim6KSieveUiTargets.cmake
/usr/lib64/libKPim6KManageSieve.so
/usr/lib64/libKPim6KSieve.so
/usr/lib64/libKPim6KSieveCore.so
/usr/lib64/libKPim6KSieveUi.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6KManageSieve.so.6.3.0
/V3/usr/lib64/libKPim6KSieve.so.6.3.0
/V3/usr/lib64/libKPim6KSieveCore.so.6.3.0
/V3/usr/lib64/libKPim6KSieveUi.so.6.3.0
/usr/lib64/libKPim6KManageSieve.so.6
/usr/lib64/libKPim6KManageSieve.so.6.3.0
/usr/lib64/libKPim6KSieve.so.6
/usr/lib64/libKPim6KSieve.so.6.3.0
/usr/lib64/libKPim6KSieveCore.so.6
/usr/lib64/libKPim6KSieveCore.so.6.3.0
/usr/lib64/libKPim6KSieveUi.so.6
/usr/lib64/libKPim6KSieveUi.so.6.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libksieve/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libksieve6.lang
%defattr(-,root,root,-)

