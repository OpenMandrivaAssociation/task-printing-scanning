%define name task-printing-scanning
%define version 2007.1
%define release %mkrel 4

Summary: Task package for printing and scanning
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Kernel and hardware
Url: http://www.mandriva.com
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: task-printing
Requires: foomatic-db-hpijs
Requires: hplip
Requires: %mklibname sane-hpaio 1
Requires: samba-client
Requires: sane-backends
Requires: saned
Requires: scanner-gui
Requires: usbutils
Requires: xinetd
Requires: xsane

%description
This task package contains the full selection of printing and
scanning packages used in Mandriva.

%files


%package -n task-printing
Group: System/Kernel and hardware
Summary: Task package for printing
Requires: ImageMagick
Requires: a2ps
Requires: cups
Requires: cups-drivers
Requires: cups-common
Requires: foomatic-db
Requires: foomatic-db-engine
Requires: foomatic-filters
Requires: ghostscript
Requires: groff
Requires: gutenprint-cups
Requires: gutenprint-escputil
Requires: gutenprint-foomatic
Requires: gutenprint-gimp2
Requires: gutenprint-ijs
Requires: lesstif
Requires: mpage
Requires: nc
Requires: net-tools
Requires: nmap
Requires: postscript-ppds
Requires: printer-filters
Requires: printer-testpages
Requires: printer-utils
Requires: scli
Requires: xpp

%description -n task-printing
This task package contains the default selection of printing packages
used in Mandriva.

%files -n task-printing


