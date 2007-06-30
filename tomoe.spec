%define version   0.6.0
%define release   %mkrel 1

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

Name:      tomoe
Summary:   A program which does Japanese handwriting recognition
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPL
URL:       https://sourceforge.jp/projects/tomoe/
Source0:   %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:        %{libname} = %{version}
BuildRequires:   automake gtk-doc
BuildRequires:	 ruby-devel ruby-gnome2-devel python-gobject-devel
# (tv) for AM_PATH_GLIB_2_0:
BuildRequires:	 glib2-devel

%description
A program which does Japanese handwriting recognition.


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
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
tomoe library.

%package -n %{develname}
Summary:    Headers of %{name} for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   %{libname_orig}-devel = %{version}-%{release}
Obsoletes:  %{libname}-devel

%description -n %{develname}
Headers of %{name} for development.


%prep
%setup -q
#cp /usr/share/automake-1.9/mkinstalldirs .

%build
# force to regenerate configure
./autogen.sh

%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f $RPM_BUILD_ROOT/%{_includedir}/tomoe/tomoe-debug.h

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/tomoe/config
%{_datadir}/gtk-doc/html/tomoe/*
%{_datadir}/tomoe/*

%files ruby
%defattr(-,root,root)
%doc COPYING
%{ruby_sitelibdir}/*.rb

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
# uim-tomoe-gtk opens some devel files
%{_libdir}/*.so.0*
#%{_libdir}/tomoe/module/*/*.so.0*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING
%{_includedir}/tomoe/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

%{ruby_sitearchdir}/*
%{python_sitearch}/*
%{_libdir}/tomoe/module/*/*.a
%{_libdir}/tomoe/module/*/*.la
%{_libdir}/tomoe/module/*/*.so
%{_libdir}/pkgconfig/*.pc
