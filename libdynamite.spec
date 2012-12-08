%define major		0
%define libname		%mklibname dynamite %major
%define develname	%mklibname -d dynamite

Name:		libdynamite
Summary:	SynCE: PKWARE decompressor
Version:	0.1.1
Release:	%{mkrel 4}
License:	MIT
Group:		System/Libraries
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
URL:		http://synce.sourceforge.net/
BuildRequires:	gettext-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-root

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

%package -n	%{develname}
Group:		Development/C
Summary:	SynCE: PKWARE decompressor
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	dynamite-devel < %{version}-%{release}
Obsoletes:	%{mklibname dynamite 0 -d} < %{version}-%{release}

%description -n %{develname}
Libdynamite is part of the SynCE project. This package contains development
headers.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n dynamite
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/%{name}.so
%{_libdir}/%{name}.*a
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.1-4mdv2010.0
+ Revision: 429725
- rebuild

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.1-3mdv2009.0
+ Revision: 237761
- since the binary's still called dynamite, let's have the package called
  dynamite not libdynamite

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.1-2mdv2009.0
+ Revision: 237750
- add back the devel package obsoletes
- provides dynamite
- obsolete old name (dynamite)
- br gettext-devel (as old package)

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.1-1mdv2009.0
+ Revision: 237714
- import libdynamite


