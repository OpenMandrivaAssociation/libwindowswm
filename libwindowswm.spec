%define major	7
%define libname	%mklibname windowswm %{major}
%define devname	%mklibname windowswm -d

Summary:	The WindowsWM Library
Name:		libwindowswm
Version:	1.0.1
Release:	8
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The WindowsWM Library

%package -n %{libname}
Summary:	The WindowsWM Library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libname}
The WindowsWM Library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libWindowsWM-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libWindowsWM.so.%{major}*

%files -n %{devname}
%{_libdir}/libWindowsWM.so
%{_libdir}/pkgconfig/windowswm.pc
%{_mandir}/man3/WindowsWM.3*

