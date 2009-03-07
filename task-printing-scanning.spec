# First, high-level tasks. Then, manufacturer-level tasks

Summary: Task package for printing and scanning
Name: task-printing-scanning
Version: 2009.0
Release: %mkrel 4
License: GPL
Group: System/Printing
Url: http://www.mandriva.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
# <mrl> Due to sane-hpaio and to avoid rebuilding sane now (2008rc2)
#BuildArch: noarch
Requires: task-printing = %{version}
Requires: foomatic-db-hpijs
Requires: hplip-gui
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
Group: System/Printing
Summary: Task package for printing
Requires: imagemagick
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
Requires: netcat-traditional
Requires: net-tools
Requires: nmap
Requires: postscript-ppds
Requires: printer-filters
Requires: printer-testpages
Requires: printer-utils
Requires: scli
Requires: task-printing-canon      = %{version}-%{release}
Requires: task-printing-epson      = %{version}-%{release}
Requires: task-printing-hp         = %{version}-%{release}
Requires: task-printing-lexmark    = %{version}-%{release}
Requires: task-printing-misc       = %{version}-%{release}
Requires: task-printing-okidata    = %{version}-%{release}
Requires: task-printing-server     = %{version}-%{release}

%description -n task-printing
This task package contains the default selection of printing packages
used in Mandriva.

%files -n task-printing

#-------------------------------------------------------------------------------
# Manufacturer-level tasks

%define c2050_ver		0.4
%define c2070_ver		0.99
%define cjet_ver		0.8.9
%define cups_ver		1.3.0
%define drv_z42_ver		0.4.3
%define cups_drivers_foo2zjs_ver	0.0
%define foomatic_ver		1:3.0.2
%define foomatic_db_hpijs_ver	20070820
%define ghostscript_ver		8.15.4
%define gutenprint_ver		5.0.1
%define hplip_ver		2.8.2-2mdv
%define lexmark2070_ver		0.6
%define lexmark7000linux_ver	990516
%define lm1100_ver		1.0.2a
%define lxcontrol_ver		1.3
%define cups_drivers_lz11_ver	1.2
%define ml85p_ver		0.2.0
%define mtink_ver		1.0.14
%define oki4linux_ver		2.1gst
%define pbm2l2030_ver		1.4
%define pbm2lwxl_ver		0
%define pentaxpj_ver		1.0.0
%define pnm2ppa_ver		1.12
%define ppmtomd_ver		1.5
%define printer_testpages_ver	2006
%define printer_tools_ver	2008
%define stylewriter_ver		0.9.9

#-------------------------------------------------------------------------------

%package -n task-printing-server
Summary: Meta package for a full CUPS server
Group: System/Printing
Requires: cups			>= %{cups_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: printer-tools		>= %{printer_tools_ver}
#Requires: task-foomatic		>= %{foomatic_ver}
Requires: foomatic-db
Requires: foomatic-db-engine
Requires: foomatic-filters

%description -n task-printing-server
This meta package will install every package needed for a full
CUPS server, including some utilities.

%files -n task-printing-server

################################################################################
############### Manufacturer specific tasks sits bellow this ###################
################################################################################

%package -n task-printing-canon
Summary: Meta package for Cannon printer drivers
Group: System/Printing
Requires: task-printing-server	= %{version}-%{release}

# The drivers
Requires: cjet			>= %{cjet_ver}
Requires: foomatic-db-hpijs	>= %{foomatic_db_hpijs_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: gutenprint-cups	>= %{gutenprint_ver}
Requires: gutenprint-foomatic	>= %{gutenprint_ver}
Requires: gutenprint-ijs	>= %{gutenprint_ver}
Requires: hplip-hpijs		>= %{hplip_ver}

%description -n task-printing-canon
This meta package will install every printer driver available for Cannon
printers.

If you have a printer of this kind installing this package is all you need to
get it working.

%files -n task-printing-canon

#-------------------------------------------------------------------------------

%package -n task-printing-epson
Summary: Meta package for printer drivers for Epson
Group: System/Printing
Requires: task-printing-server	= %{version}-%{release}

# The drivers
Requires: foomatic-db-hpijs	>= %{foomatic_db_hpijs_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: gutenprint-cups	>= %{gutenprint_ver}
Requires: gutenprint-foomatic	>= %{gutenprint_ver}
Requires: gutenprint-ijs	>= %{gutenprint_ver}
Requires: hplip-hpijs		>= %{hplip_ver}

# Some utils
Requires: gutenprint-escputil	>= %{gutenprint_ver}
Requires: printer-tools		>= %{printer_tools_ver}

%description -n task-printing-epson
This meta package will install every printer driver available for printers from
Epson.

If you have a printer of this kind installing this package is all you need to
get it working.

%files -n task-printing-epson

#-------------------------------------------------------------------------------

%package -n task-printing-hp
Summary: Meta package for printer drivers for HP
Group: System/Printing
Requires: task-printing-server	= %{version}-%{release}

# The drivers
Requires: foomatic-db-hpijs	>= %{foomatic_db_hpijs_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: gutenprint-cups	>= %{gutenprint_ver}
Requires: gutenprint-foomatic	>= %{gutenprint_ver}
Requires: gutenprint-ijs	>= %{gutenprint_ver}
Requires: cups-drivers-foo2zjs	>= %{cups_drivers_foo2zjs_ver}
Requires: hplip			>= %{hplip_ver}
Suggests: hplip-gui             >= %{hplip_ver}
Requires: pnm2ppa		>= %{pnm2ppa_ver}

%description -n task-printing-hp
This meta package will install every printer driver available for printers from
HP.

If you have a printer of this kind installing this package is all you need to
get it working.

%files -n task-printing-hp

#-------------------------------------------------------------------------------

%package -n task-printing-lexmark
Summary: Meta package for printer drivers for Lexmark
Group: System/Printing
Requires: task-printing-server = %{version}-%{release}

# The drivers
Requires: c2050			>= %{c2050_ver}
Requires: c2070			>= %{c2070_ver}
Requires: drv_z42		>= %{drv_z42_ver}
Requires: foomatic-db-hpijs	>= %{foomatic_db_hpijs_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: gutenprint-cups	>= %{gutenprint_ver}
Requires: gutenprint-foomatic	>= %{gutenprint_ver}
Requires: gutenprint-ijs	>= %{gutenprint_ver}
Requires: hplip-hpijs		>= %{hplip_ver}
Requires: lexmark2070		>= %{lexmark2070_ver}
Requires: lexmark7000linux	>= %{lexmark7000linux_ver}
Requires: lm1100		>= %{lm1100_ver}
Requires: cups-drivers-lz11	>= %{cups_drivers_lz11_ver}
Requires: pbm2l2030		>= %{pbm2l2030_ver}

# Some lex utils
Requires: printer-tools		>= %{printer_tools_ver}
Requires: z42tool		>= %{drv_z42_ver}
Requires: lxcontrol		>= %{lxcontrol_ver}

%description -n task-printing-lexmark
This meta package will install every printer driver available for printers from
Lexmark.

If you have a printer of this kind installing this package is all you need to
get it working.

%files -n task-printing-lexmark

#-------------------------------------------------------------------------------

%package -n task-printing-misc
Summary: Meta package for printer drivers for miscelaneous printers
Group: System/Printing
Requires: task-printing-server	= %{version}-%{release}

# The drivers
Requires: drv_z42		>= %{drv_z42_ver}
Requires: cups-drivers-foo2zjs	>= %{cups_drivers_foo2zjs_ver}
Requires: foomatic-db-hpijs	>= %{foomatic_db_hpijs_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: hplip-hpijs		>= %{hplip_ver}
Requires: stylewriter		>= %{stylewriter_ver}
Requires: ml85p			>= %{ml85p_ver}
Requires: pbm2lwxl		>= %{pbm2lwxl_ver}
Requires: pentaxpj		>= %{pentaxpj_ver}
Requires: ppmtomd		>= %{ppmtomd_ver}

%description -n task-printing-misc
This meta package will install every printer driver available for printers from
miscelaneous manufacturers.

This package should cover printers from:
Alps, Anitech, Apollo, Apple, Avery, Brother, Citizen, Citoh, Compaq, Dec,
Dell, Dymo, Fujitsu, IBM, Imagen, Infotec, Kodak, Kyocera, Minolta, Mitsubishi,
Nec, Oce, Olivetti, Panasonic, Pcpi, Pentax, QMS, Ricoh, Samsung, Star,
Tektronix and Xerox.

%files -n task-printing-misc

#-------------------------------------------------------------------------------

%package -n task-printing-okidata
Summary: Meta package for printer drivers for Okidata
Group: System/Printing
Requires: task-printing-server	= %{version}-%{release}

# The drivers
Requires: foomatic-db-hpijs	>= %{foomatic_db_hpijs_ver}
Requires: ghostscript		>= %{ghostscript_ver}
Requires: hplip-hpijs		>= %{hplip_ver}
Requires: oki4linux		>= %{oki4linux_ver}
Requires: ppmtomd		>= %{ppmtomd_ver}

%description -n task-printing-okidata
This meta package will install every printer driver available for printers from
Okidata.

If you have a printer of this kind installing this package is all you need to
get it working.

%files -n task-printing-okidata

#-------------------------------------------------------------------------------

