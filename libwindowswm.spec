%define major		7
%define libname		%mklibname windowswm %major
%define develname	%mklibname windowswm -d
%define staticname	%mklibname windowswm -d -s

Name:		libwindowswm
Summary:	The WindowsWM Library
Version:	1.0.1
Release:	6
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The WindowsWM Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The WindowsWM Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The WindowsWM Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{mklibname windowswm 7 -d}

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%{_libdir}/libWindowsWM.so
%{_libdir}/pkgconfig/windowswm.pc
%{_mandir}/man3/WindowsWM.3*


#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname windowswm 7 -d -s}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%{_libdir}/libWindowsWM.a

#-----------------------------------------------------------

%prep
%setup -q -n libWindowsWM-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libWindowsWM.so.%{major}*


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2011.0
+ Revision: 661540
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 602614
- rebuild

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.1-1mdv2010.1
+ Revision: 463691
- New version: 1.0.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-7mdv2010.0
+ Revision: 425876
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 223018
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2008.1
+ Revision: 150842
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 04 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-4mdv2008.0
+ Revision: 58799
- manpage isn't bz2 any more
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

