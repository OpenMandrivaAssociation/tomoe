%define version   0.6.0
%define release   %mkrel 12

%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

Name:      tomoe
Summary:   A program which does Japanese handwriting recognition
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPLv2+
URL:       https://sourceforge.jp/projects/tomoe/
Source0:   %{name}-%{version}.tar.bz2
Patch1:	   tomoe-0.6.0-fix-str-fmt.patch
Patch2:    tomoe-0.6.0-linkage.patch
Patch3:    tomoe-0.6.0-undefined-class.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        %{libname} = %{version}
BuildRequires:   automake intltool gtk-doc
BuildRequires:	 ruby-devel ruby-gnome2-devel python-gobject-devel
BuildRequires:	 pygtk2.0-devel
# (tv) for AM_PATH_GLIB_2_0:
BuildRequires:	 glib2-devel

%description
A program which does Japanese handwriting recognition.

%package    python
Summary:    Python binding of tomoe
Group:      System/Internationalization
Requires:   %{name} = %{version}
Requires:   python

%description python
Python binding of tomoe.

%package    ruby
Summary:    Ruby binding of tomoe
Group:      System/Internationalization
Requires:   %{name} = %{version}
Requires:   ruby ruby-gnome2

%description ruby
Ruby binding of tomoe.

%package -n %{libname}
Summary:    Tomoe library
Group:      System/Internationalization
Conflicts:  %{name}-devel < 0.6.0-5mdv

%description -n %{libname}
tomoe library.

%package -n %{develname}
Summary:    Headers of %{name} for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %{libname}-devel

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/tomoe/config
%{_datadir}/gtk-doc/html/tomoe/*
%{_datadir}/tomoe/*

%files python
%defattr(-,root,root)
%doc COPYING
%{python_sitearch}/*.so

%files ruby
%defattr(-,root,root)
%doc COPYING
%{ruby_sitelibdir}/*.rb
%{ruby_sitelibdir}/*/*.so

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
# uim-tomoe-gtk opens some devel files
%{_libdir}/*.so.0*
%{_libdir}/tomoe/module/*/*.so

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING
%{_includedir}/tomoe/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

%{ruby_sitearchdir}/*.h
%{ruby_sitearchdir}/*.a
%{ruby_sitearchdir}/*.la
%{python_sitearch}/*.a
%{python_sitearch}/*.la
%{_libdir}/tomoe/module/*/*.a
%{_libdir}/tomoe/module/*/*.la
%{_libdir}/pkgconfig/tomoe.pc
%{_libdir}/pkgconfig/pytomoe.pc
