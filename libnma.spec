# TODO: gtk4 variant (--with-libnma-gtk4; uses gtk4-builder-tool, which fails without $DISPLAY)
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc documentation
%bcond_without	static_libs	# shared library
%bcond_without	vala		# Vala API
#
Summary:	NetworkManager UI utilities (libnm version)
Summary(pl.UTF-8):	Narzędzia UI NetworkManagera (wersja libnm)
Name:		libnma
Version:	1.8.34
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libnma/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	145967daaaf36ee83ee9fdb9b228caf7
URL:		https://gitlab.gnome.org/GNOME/libnma
BuildRequires:	NetworkManager-devel >= 2:1.7
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gcr-ui-devel >= 3.14
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel >= 0.9.6
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	tar >= 1:1.22
%if %{with vala}
BuildRequires:	vala >= 2:0.17.1.24
BuildRequires:	vala-NetworkManager
%endif
BuildRequires:	xz
Requires:	NetworkManager-libs >= 2:1.7
Requires:	gcr-ui >= 3.14
Requires:	glib2 >= 1:2.38
Requires:	gtk+3 >= 3.10
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
Requires:	NetworkManager-devel >= 2:1.7
Requires:	glib2-devel >= 1:2.38
Requires:	gtk+3-devel >= 3.10
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

%package -n vala-libnma
Summary:	Vala API for libnma library
Summary(pl.UTF-8):	API języka Vala do biblioteki libnma
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.17.1.24
BuildArch:	noarch

%description -n vala-libnma
Vala API for libnma library.

%description -n vala-libnma -l pl.UTF-8
API języka Vala do biblioteki libnma.

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
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnma.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/libnma.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnma.so.0
%{_libdir}/girepository-1.0/NMA-1.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnma.so
%{_includedir}/libnma
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_pkgconfigdir}/libnma.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnma.a
%endif

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
