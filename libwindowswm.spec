%define name	libwindowswm
%define version	1.0.0
%define release	%mkrel 4

%define major		7
%define libname		%mklibname windowswm %major
%define develname	%mklibname windowswm -d
%define staticname	%mklibname windowswm -d -s

Name:		%{name}
Summary:	The WindowsWM Library
Version:	%{version}
Release:	%{release}
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
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
%defattr(-,root,root)
%{_libdir}/libWindowsWM.so
%{_libdir}/libWindowsWM.la
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
%defattr(-,root,root)
%{_libdir}/libWindowsWM.a

#-----------------------------------------------------------

%prep
%setup -q -n libWindowsWM-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libWindowsWM.so.%{major}*
