Summary:	A quick previewer for Nautilus
Name:		sushi
Version:	3.8.1
Release:	1
License:	GPLv2+ with exceptions
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sushi/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	c602997a795f9d9eb00d69ab4a7fe58c
URL:		https://live.gnome.org/ThreePointOne/Features/FilePreviewing
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel >= 1.0.2
BuildRequires:	evince-devel >= 3.2.0
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.23.0
BuildRequires:	gjs-devel >= 1.34
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.30.0
Obsoletes:	sushi-devel < 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop file
manager.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/sushi/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/sushi
%attr(755,root,root) %{_libexecdir}/sushi-start
%dir %{_libdir}/sushi
%attr(755,root,root) %{_libdir}/sushi/libsushi-1.0.so
%dir %{_libdir}/sushi/girepository-1.0
%{_libdir}/sushi/girepository-1.0/Sushi-1.0.typelib
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
%{_datadir}/glib-2.0/schemas/org.gnome.sushi.gschema.xml
