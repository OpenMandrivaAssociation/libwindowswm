%define libwindowswm %mklibname windowswm 7
Name: libwindowswm
Summary:  The WindowsWM Library
Version: 1.0.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The WindowsWM Library

#-----------------------------------------------------------

%package -n %{libwindowswm}
Summary:  The WindowsWM Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libwindowswm}
The WindowsWM Library

#-----------------------------------------------------------

%package -n %{libwindowswm}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libwindowswm} = %{version}
Provides: libwindowswm-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{libwindowswm}-devel
Development files for %{name}

%files -n %{libwindowswm}-devel
%defattr(-,root,root)
%{_libdir}/libWindowsWM.so
%{_libdir}/libWindowsWM.la
%{_libdir}/pkgconfig/windowswm.pc
%{_mandir}/man3/WindowsWM.3.bz2


#-----------------------------------------------------------

%package -n %{libwindowswm}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libwindowswm}-devel = %{version}
Provides: libwindowswm-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libwindowswm}-static-devel
Static development files for %{name}

%files -n %{libwindowswm}-static-devel
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

%files -n %{libwindowswm}
%defattr(-,root,root)
%{_libdir}/libWindowsWM.so.7
%{_libdir}/libWindowsWM.so.7.0.0


