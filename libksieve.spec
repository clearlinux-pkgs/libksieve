#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libksieve
Version  : 23.04.1
Release  : 59
URL      : https://download.kde.org/stable/release-service/23.04.1/src/libksieve-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/libksieve-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/libksieve-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules-data
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-staticdev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktextaddons-dev
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

%prep
%setup -q -n libksieve-23.04.1
cd %{_builddir}/libksieve-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685642474
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685642474
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksieve
cp %{_builddir}/libksieve-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libksieve/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libksieve-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libksieve/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/libksieve/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/libksieve-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/libksieve-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libksieve/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/libksieve-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libksieve/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
