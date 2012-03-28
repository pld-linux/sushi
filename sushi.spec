Summary:	A quick previewer for Nautilus
Name:		sushi
Version:	0.4.0
Release:	1
License:	GPLv2+ with exceptions
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sushi/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	d8544340b18658c014ce2dbfaa9e34a4
URL:		https://live.gnome.org/ThreePointOne/Features/FilePreviewing
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel >= 1.0.2
BuildRequires:	evince-devel >= 3.2.0
BuildRequires:	gjs-devel >= 0.8
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libmusicbrainz3-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop file
manager.

%package devel
Summary:	Development files for sushi
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The sushi-devel package contains libraries and header files for
developing applications that use sushi.

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsushi-1.0.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/sushi
%attr(755,root,root) %{_libexecdir}/sushi-start
%attr(755,root,root) %{_libdir}/libsushi-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsushi-1.0.so.0
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
%{_libdir}/girepository-1.0/Sushi-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsushi-1.0.so
%{_datadir}/gir-1.0/Sushi-1.0.gir
