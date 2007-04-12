%define version   0.5.1
%define release   %mkrel 1

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

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
BuildRequires:   automake1.8 gtk-doc
BuildRequires:	 ruby-devel ruby-gnome2-devel
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

%package -n %{libname}-devel
Summary:    Headers of %{name} for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   %{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers of %{name} for development.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
# force to regenerate configure
./autogen.sh

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f $RPM_BUILD_ROOT/%{_includedir}/tomoe/tomoe-debug.h

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/tomoe/config
%{_datadir}/gtk-doc/html/tomoe/*
%{_datadir}/tomoe/*

%files ruby
%defattr(-,root,root)
%doc COPYING
/usr/lib/ruby/site_ruby/*/*.rb
/usr/lib/ruby/site_ruby/*/*/*.so.0*


%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
# uim-tomoe-gtk opens some devel files
%{_libdir}/*.so.0*
%{_libdir}/tomoe/module/*/*.so.0*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_includedir}/tomoe/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

/usr/lib/ruby/site_ruby/*/*/*.h
/usr/lib/ruby/site_ruby/*/*/*.a
/usr/lib/ruby/site_ruby/*/*/*.la
/usr/lib/ruby/site_ruby/*/*/*.so
%{_libdir}/tomoe/module/*/*.a
%{_libdir}/tomoe/module/*/*.la
%{_libdir}/tomoe/module/*/*.so
%{_libdir}/pkgconfig/*.pc


