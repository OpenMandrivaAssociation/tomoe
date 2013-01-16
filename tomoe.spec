%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

Name:      tomoe
Summary:   A program which does Japanese handwriting recognition
Version:   0.6.0
Release:   14
Group:     System/Internationalization
License:   LGPLv2+
URL:       https://sourceforge.jp/projects/tomoe/
Source0:   %{name}-%{version}.tar.bz2
Patch1:	   tomoe-0.6.0-fix-str-fmt.patch
Patch2:    tomoe-0.6.0-linkage.patch
Patch3:    tomoe-0.6.0-undefined-class.patch
Patch4:    tomoe-0.6.0-fix-glib-includes.patch
Patch5:    tomoe-automake-1.13.patch
Requires:        %{libname} = %{version}
BuildRequires:   automake intltool gtk-doc
#BuildRequires:	 ruby-devel ruby-gnome2-devel
BuildRequires:   python-gobject-devel
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

#%package    ruby
#Summary:    Ruby binding of tomoe
#Group:      System/Internationalization
#Requires:   %{name} = %{version}
#Requires:   ruby ruby-gnome2

#%description ruby
#Ruby binding of tomoe.

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
%patch4 -p1
%patch5 -p1 -b .am13~

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

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

#%files ruby
#%defattr(-,root,root)
#%doc COPYING
#%{ruby_sitelibdir}/*.rb
#%{ruby_sitelibdir}/*/*.so

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
%{_libdir}/*.so

#%{ruby_sitearchdir}/*.h
#%{ruby_sitearchdir}/*.a
%{python_sitearch}/*.a
%{_libdir}/tomoe/module/*/*.a
%{_libdir}/pkgconfig/tomoe.pc
%{_libdir}/pkgconfig/pytomoe.pc


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-12mdv2011.0
+ Revision: 670716
- mass rebuild

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-11mdv2011.0
+ Revision: 591509
- rebuild for python-2.7

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 0.6.0-10mdv2010.1
+ Revision: 505917
- add fedora patch to fix segment fault (bug#54314)
- more link flags fixes

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.6.0-9mdv2010.0
+ Revision: 453273
- fix linkage
- we are using gcc 4.4, so workaround for gcc 4.2 not needed any more

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0-8mdv2009.1
+ Revision: 319727
- build with python 2.6

  + Funda Wang <fwang@mandriva.org>
    - fix str fmt
    - rebuild for new python

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-6mdv2009.0
+ Revision: 225832
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.0-5mdv2008.1
+ Revision: 136550
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 03 2007 Funda Wang <fwang@mandriva.org> 0.6.0-5mdv2008.0
+ Revision: 58428
- Acturally conflict

* Fri Aug 03 2007 Funda Wang <fwang@mandriva.org> 0.6.0-4mdv2008.0
+ Revision: 58414
- fix file conflicts

* Thu Aug 02 2007 Funda Wang <fwang@mandriva.org> 0.6.0-3mdv2008.0
+ Revision: 58130
- Try parallel build
- fix bug#31577

  + Pixel <pixel@mandriva.com>
    - workaround gcc 4.2 exhausting memory (it can't solve aliasing graph) (#31799)

* Wed Jul 04 2007 Funda Wang <fwang@mandriva.org> 0.6.0-2mdv2008.0
+ Revision: 47805
- BR pygtk2.0. Thanks UTUMI Hirosi

* Sun Jul 01 2007 Funda Wang <fwang@mandriva.org> 0.6.0-1mdv2008.0
+ Revision: 46431
- BR intltool
- fix file list
- New version


* Wed Feb 28 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5.1-1mdv2007.0
+ Revision: 130179
- simpler fix that doesn't require having ruby on the building srpm host
- fix rpm macro
- fix build (UTUMI Hirosi)
- new release
- add buildrequire on glib2-devel b/c of AM_PATH_GLIB_2_0
- new release
- Import tomoe

* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.1-6mdv2007.1
- rebuild for E libs

* Wed Feb 22 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-5mdk
- rebuild due to E libs having been altered

* Thu Dec 01 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-4mdk
- rebuild against current libs (#19983)

* Fri Nov 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-3mdk
- add missing buildrequires
- relax requires
- run ldconfig in %%post and %%postun

* Fri Nov 18 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.2.1-2mdk
- rebuild against openssl-0.9.8

* Tue Aug 16 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.2.1-1mdk
- new release

* Sat Aug 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.0-2.20050812.1mdk
- latest snapshot from UTUMI Hirosi <utuhiro78@yahoo.co.jp>

* Sun Feb 27 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.1.1-2mdk
- fix automake buildrequires

* Thu Feb 17 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.1.1-1mdk
- new release

* Thu Jan 13 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.0.1-0.cvs20050113.1mdk
- first spec

