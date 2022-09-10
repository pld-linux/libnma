# TODO: gcr-4-gtk4 >= 3.90? (needs update for gcr-4 3.92?)
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc documentation
%bcond_without	static_libs	# shared library
%bcond_without	vala		# Vala API
%bcond_without	gtk4		# Gtk4 variant
#
Summary:	NetworkManager UI utilities (libnm version)
Summary(pl.UTF-8):	Narzędzia UI NetworkManagera (wersja libnm)
Name:		libnma
Version:	1.10.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libnma/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	5ace2e91cceccb61279cd31947c92037
URL:		https://gitlab.gnome.org/GNOME/libnma
BuildRequires:	NetworkManager-devel >= 2:1.7
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gcr-ui-devel >= 3.14
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.12
BuildRequires:	gtk-doc >= 1.0
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.6.2}
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	tar >= 1:1.22
%if %{with vala}
BuildRequires:	vala >= 2:0.17.1.24
BuildRequires:	vala-NetworkManager
%endif
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Requires:	NetworkManager-libs >= 2:1.7
Requires:	gcr-ui >= 3.14
Requires:	glib2 >= 1:2.38
Requires:	gtk+3 >= 3.12
Requires:	iso-codes
Requires:	mobile-broadband-provider-info
Provides:	NetworkManager-gtk-lib = %{version}-%{release}
Obsoletes:	NetworkManager-gtk-lib < 1.8.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager UI utilities (libnm version).

%description -l pl.UTF-8
Narzędzia UI NetworkManagera (wersja libnm).

%package devel
Summary:	Header files for libnma library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnma
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-headers = %{version}-%{release}
Requires:	NetworkManager-devel >= 2:1.7
Requires:	glib2-devel >= 1:2.38
Requires:	gtk+3-devel >= 3.12
Provides:	NetworkManager-gtk-lib-devel = %{version}-%{release}
Obsoletes:	NetworkManager-gtk-lib-devel < 1.8.26

%description devel
Header files for libnma library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnma.

%package static
Summary:	Static libnma library
Summary(pl.UTF-8):	Statyczna biblioteka libnma
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnma library.

%description static -l pl.UTF-8
Statyczna biblioteka libnma.

%package -n vala-libnma
Summary:	Vala API for libnma library
Summary(pl.UTF-8):	API języka Vala do biblioteki libnma
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.17.1.24
BuildArch:	noarch

%description -n vala-libnma
Vala API for libnma library.

%description -n vala-libnma -l pl.UTF-8
API języka Vala do biblioteki libnma.

%package data
Summary:	Common data for libnma libraries
Summary(pl.UTF-8):	Wspólne dane bibliotek libnma
Group:		X11/Libraries
Requires(post,postun):	glib2 >= 1:2.38
Conflicts:	libnma < 1.8.36-2

%description data
Common data for libnma libraries.

%description data -l pl.UTF-8
Wspólne dane bibliotek libnma.

%package headers
Summary:	Header files for libnma libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libnma
Group:		X11/Development/Libraries
Conflicts:	libnma-devel < 1.8.36-2

%description headers
Header files for libnma libraries.

%description headers -l pl.UTF-8
Pliki nagłówkowe bibliotek libnma.

%package apidocs
Summary:	API documentation for libnma library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libnma
Group:		Documentation
Obsoletes:	NetworkManager-gtk-lib-apidocs < 1.8.26
BuildArch:	noarch

%description apidocs
API documentation for libnma library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnma.

%package gtk4
Summary:	NetworkManager UI utilities (libnm version) for GTK 4
Summary(pl.UTF-8):	Narzędzia UI NetworkManagera (wersja libnm) dla GTK 4
Group:		X11/Libraries
Requires:	%{name}-data = %{version}-%{release}
Requires:	NetworkManager-libs >= 2:1.7
Requires:	gcr-ui >= 3.14
Requires:	glib2 >= 1:2.38
Requires:	gtk4 >= 4.6.2

%description gtk4
NetworkManager UI utilities (libnm version) for GTK 4.

%description gtk4 -l pl.UTF-8
Narzędzia UI NetworkManagera (wersja libnm) dla GTK 4.

%package gtk4-devel
Summary:	Header files for libnma library for GTK 4
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnma dla GTK 4
Group:		X11/Development/Libraries
Requires:	%{name}-gtk4 = %{version}-%{release}
Requires:	%{name}-headers = %{version}-%{release}
Requires:	NetworkManager-devel >= 2:1.7
Requires:	glib2-devel >= 1:2.38
Requires:	gtk4-devel >= 4.6.2

%description gtk4-devel
Header files for libnma library for GTK 4.

%description gtk4-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnma dla GTK 4.

%package gtk4-static
Summary:	Static libnma library for GTK 4
Summary(pl.UTF-8):	Statyczna biblioteka libnma dla GTK 4
Group:		X11/Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}

%description gtk4-static
Static libnma library for GTK 4.

%description gtk4-static -l pl.UTF-8
Statyczna biblioteka libnma dla GTK 4.

%package -n vala-libnma-gtk4
Summary:	Vala API for libnma library for GTK 4
Summary(pl.UTF-8):	API języka Vala do biblioteki libnma dla GTK 4
Group:		X11/Development/Libraries
Requires:	%{name}-gtk4-devel = %{version}-%{release}
Requires:	vala >= 2:0.17.1.24
BuildArch:	noarch

%description -n vala-libnma-gtk4
Vala API for libnma library for GTK 4.

%description -n vala-libnma-gtk4 -l pl.UTF-8
API języka Vala do biblioteki libnma dla GTK 4.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-iso-codes \
	--disable-mobile-broadband-provider-info \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{__enable_disable vala} \
	--with-html-dir=%{_gtkdocdir} \
	%{?with_gtk4:--with-libnma-gtk4}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnma*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post data
%glib_compile_schemas

%postun data
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnma.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnma.so.0
%{_libdir}/girepository-1.0/NMA-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnma.so
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_pkgconfigdir}/libnma.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnma.a
%endif

%files data -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%files headers
%defattr(644,root,root,755)
%{_includedir}/libnma

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnma
%endif

%if %{with vala}
%files -n vala-libnma
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libnma.deps
%{_datadir}/vala/vapi/libnma.vapi
%endif

%if %{with gtk4}
%files gtk4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnma-gtk4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnma-gtk4.so.0
%{_libdir}/girepository-1.0/NMA4-1.0.typelib

%files gtk4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnma-gtk4.so
%{_datadir}/gir-1.0/NMA4-1.0.gir
%{_pkgconfigdir}/libnma-gtk4.pc

%if %{with static_libs}
%files gtk4-static
%defattr(644,root,root,755)
%{_libdir}/libnma-gtk4.a
%endif

%if %{with vala}
%files -n vala-libnma-gtk4
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libnma-gtk4.deps
%{_datadir}/vala/vapi/libnma-gtk4.vapi
%endif
%endif
