%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	A program which does Japanese handwriting recognition
Name:		tomoe
Version:	0.6.0
Release:	19
Group:		System/Internationalization
License:	LGPLv2+
Url:		https://sourceforge.jp/projects/tomoe/
Source0:	%{name}-%{version}.tar.bz2
Patch1:		tomoe-0.6.0-fix-str-fmt.patch
Patch2:		tomoe-0.6.0-linkage.patch
Patch3:		tomoe-0.6.0-undefined-class.patch
Patch4:		tomoe-0.6.0-fix-glib-includes.patch
Patch5:		tomoe-automake-1.13.patch
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)

%description
A program which does Japanese handwriting recognition.

%package    python
Summary:	Python binding of tomoe
Group:		System/Internationalization
Requires:	%{name} = %{version}-%{release}
Requires:	python

%description python
Python binding of tomoe.

%package -n %{libname}
Summary:	Tomoe library
Group:		System/Internationalization
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
tomoe library.

%package -n %{devname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%config(noreplace) %{_sysconfdir}/tomoe/config
%{_datadir}/gtk-doc/html/tomoe/*
%{_datadir}/tomoe/*

%files python
%{python_sitearch}/*.so

%files -n %{libname}
%{_libdir}/libtomoe.so.%{major}*
%{_libdir}/tomoe/module/*/*.so

%files -n %{devname}
%{_includedir}/tomoe/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/tomoe.pc
%{_libdir}/pkgconfig/pytomoe.pc

