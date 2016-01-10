Summary:	A quick previewer for Nautilus
Summary(pl.UTF-8):	Szybki podgląd dla Nautilusa
Name:		sushi
Version:	3.18.0
Release:	1
License:	GPL v2+ with GStreamer plugins exception
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sushi/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	3976f71b3970d4ec454fa7436efc9896
URL:		https://live.gnome.org/ThreePointOne/Features/FilePreviewing
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel >= 1.0.2
BuildRequires:	evince-devel >= 3.2.0
BuildRequires:	freetype-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.23.0
BuildRequires:	gjs-devel >= 1.38.0
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	gtk-webkit4-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	clutter >= 1.12.0
Requires:	clutter-gtk >= 1.0.2
Requires:	gdk-pixbuf2 >= 2.23.0
Requires:	gjs >= 1.38.0
Requires:	glib2 >= 1:2.30.0
Requires:	gtk+3 >= 3.14.0
Obsoletes:	sushi-devel < 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop file
manager.

%description -l pl.UTF-8
Sushi to szybki podgląd dla Nautilusa - zarządcy plików dla środowiska
GNOME.

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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/sushi
%attr(755,root,root) %{_libexecdir}/sushi-start
%dir %{_libdir}/sushi
%attr(755,root,root) %{_libdir}/sushi/libsushi-1.0.so
%dir %{_libdir}/sushi/girepository-1.0
%{_libdir}/sushi/girepository-1.0/Sushi-1.0.typelib
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
