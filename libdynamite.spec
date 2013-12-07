%define major	0
%define libname	%mklibname dynamite %major
%define devname	%mklibname -d dynamite

Summary:	SynCE: PKWARE decompressor
Name:		libdynamite
Version:	0.1.1
Release:	7
License:	MIT
Group:		System/Libraries
Url:		http://synce.sourceforge.net/
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
BuildRequires:	gettext-devel

%description
Dynamite is a tool and library for decompressing data compressed
with the PKWARE Data Compression Library.

%package -n dynamite
Group:		Archiving/Other
Summary:	SynCE: PKWARE decompressor

%description -n dynamite
Dynamite is a tool for decompressing data compressed with the PKWARE
Data Compression Library.

%package -n %{libname}
Group:		System/Libraries
Summary:	SynCE: PKWARE decompressor

%description -n %{libname}
Libdynamite is part of the SynCE project. This package contains shared
libraries.

%package -n	%{devname}
Group:		Development/C
Summary:	SynCE: PKWARE decompressor
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libdynamite is part of the SynCE project. This package contains development
headers.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n dynamite
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%doc LICENSE
%{_libdir}/%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/*.pc

