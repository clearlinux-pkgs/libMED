#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libMED
Version  : 3.3.1+repack
Release  : 1
URL      : http://deb.debian.org/debian/pool/main/m/med-fichier/med-fichier_3.3.1+repack.orig.tar.gz
Source0  : http://deb.debian.org/debian/pool/main/m/med-fichier/med-fichier_3.3.1+repack.orig.tar.gz
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
%setup -q -n med-fichier-3.3.1+repack
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543922252
%configure --disable-static --disable-python
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1543922252
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libMED
cp COPYING %{buildroot}/usr/share/package-licenses/libMED/COPYING
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/libMED/COPYING.LESSER
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
/usr/include/*.h
/usr/include/*.hf
/usr/include/*.hf77
/usr/include/*.hf90
/usr/include/*.hxx
/usr/include/2.3.6/MEDerreur.hxx
/usr/include/2.3.6/med.h
/usr/include/2.3.6/med.hf
/usr/include/2.3.6/med23v30.h
/usr/include/2.3.6/med23v30_proto.h
/usr/include/2.3.6/medC_win_dll.h
/usr/include/2.3.6/med_exit_if.h
/usr/include/2.3.6/med_proto.h
/usr/include/2.3.6/med_utils.h
/usr/lib64/libmed.so
/usr/lib64/libmedC.so
/usr/lib64/libmedimport.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmed.so.1
/usr/lib64/libmed.so.1.9.1
/usr/lib64/libmedC.so.1
/usr/lib64/libmedC.so.1.9.1
/usr/lib64/libmedimport.so.0
/usr/lib64/libmedimport.so.0.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libMED/COPYING
/usr/share/package-licenses/libMED/COPYING.LESSER