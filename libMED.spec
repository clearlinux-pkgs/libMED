#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libMED
Version  : 4.0.0+repack
Release  : 7
URL      : https://deb.debian.org/debian/pool/main/m/med-fichier/med-fichier_4.0.0+repack.orig.tar.gz
Source0  : https://deb.debian.org/debian/pool/main/m/med-fichier/med-fichier_4.0.0+repack.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: libMED-bin = %{version}-%{release}
Requires: libMED-lib = %{version}-%{release}
Requires: libMED-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gfortran
BuildRequires : hdf5-dev
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : python3-tcl
BuildRequires : zlib-dev
Patch1: build.patch

%description
------------------
TABLE DES MATIERES
------------------
1. 	Obtenir la derniere version

%package bin
Summary: bin components for the libMED package.
Group: Binaries
Requires: libMED-license = %{version}-%{release}

%description bin
bin components for the libMED package.


%package dev
Summary: dev components for the libMED package.
Group: Development
Requires: libMED-lib = %{version}-%{release}
Requires: libMED-bin = %{version}-%{release}
Provides: libMED-devel = %{version}-%{release}
Requires: libMED = %{version}-%{release}

%description dev
dev components for the libMED package.


%package lib
Summary: lib components for the libMED package.
Group: Libraries
Requires: libMED-license = %{version}-%{release}

%description lib
lib components for the libMED package.


%package license
Summary: license components for the libMED package.
Group: Default

%description license
license components for the libMED package.


%prep
%setup -q -n med-fichier-4.0.0+repack
cd %{_builddir}/med-fichier-4.0.0+repack
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585792538
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-python
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1585792538
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libMED
cp %{_builddir}/med-fichier-4.0.0+repack/COPYING %{buildroot}/usr/share/package-licenses/libMED/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/med-fichier-4.0.0+repack/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libMED/e203d4ef09d404fa5c03cf6590e44231665be689
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/libmed3.settings

%files bin
%defattr(-,root,root,-)
/usr/bin/mdump
/usr/bin/mdump2
/usr/bin/mdump3
/usr/bin/medconforme
/usr/bin/medimport
/usr/bin/xmdump
/usr/bin/xmdump2
/usr/bin/xmdump3

%files dev
%defattr(-,root,root,-)
/usr/include/2.3.6/MEDerreur.hxx
/usr/include/2.3.6/med.h
/usr/include/2.3.6/med.hf
/usr/include/2.3.6/med23v30.h
/usr/include/2.3.6/med23v30_proto.h
/usr/include/2.3.6/medC_win_dll.h
/usr/include/2.3.6/med_exit_if.h
/usr/include/2.3.6/med_proto.h
/usr/include/2.3.6/med_utils.h
/usr/include/MEDerreur.hxx
/usr/include/MEDimport.h
/usr/include/MEDimport.hxx
/usr/include/med.h
/usr/include/med.hf
/usr/include/med.hf77
/usr/include/med.hf90
/usr/include/medC_win_dll.h
/usr/include/med_err.h
/usr/include/med_exit_if.h
/usr/include/med_parameter.hf
/usr/include/med_proto.h
/usr/include/med_utils.h
/usr/include/medequivalence.h
/usr/include/medfamily.h
/usr/include/medfield.h
/usr/include/medfile.h
/usr/include/medfilter.h
/usr/include/medimport_win_dll.h
/usr/include/medimportcxx_win_dll.h
/usr/include/medinterp.h
/usr/include/medlibrary.h
/usr/include/medlink.h
/usr/include/medlocalization.h
/usr/include/medmesh.h
/usr/include/medparameter.h
/usr/include/medprofile.h
/usr/include/medstructelement.h
/usr/include/medsubdomain.h
/usr/lib64/libmed.so
/usr/lib64/libmedC.so
/usr/lib64/libmedimport.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmed.so.11
/usr/lib64/libmed.so.11.0.0
/usr/lib64/libmedC.so.11
/usr/lib64/libmedC.so.11.0.0
/usr/lib64/libmedimport.so.0
/usr/lib64/libmedimport.so.0.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libMED/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/libMED/e203d4ef09d404fa5c03cf6590e44231665be689
