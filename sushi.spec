Summary:	A quick previewer for Nautilus
Summary(pl.UTF-8):	Szybki podgląd dla Nautilusa
Name:		sushi
Version:	44.2
Release:	2
License:	GPL v2+ with GStreamer plugins exception
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/sushi/44/%{name}-%{version}.tar.xz
# Source0-md5:	ca61517e2f7878eb37e111b64b4001c3
URL:		https://wiki.gnome.org/ThreePointOne/Features/FilePreviewing
BuildRequires:	evince-devel >= 3.2.0
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdk-pixbuf2-devel >= 2.23.0
# gjs/gjs-console program
BuildRequires:	gjs >= 1.38.0
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	gtk-webkit4.1-devel
BuildRequires:	gtksourceview4-devel >= 4.0.3
BuildRequires:	harfbuzz-devel >= 0.9.9
BuildRequires:	libepoxy-devel
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gdk-pixbuf2 >= 2.23.0
Requires:	gjs >= 1.38.0
Requires:	glib2 >= 1:2.30.0
Requires:	gtk+3 >= 3.22.0
Requires:	gtk-webkit4.1
Requires:	gtksourceview4 >= 4.0.3
Requires:	harfbuzz >= 0.9.9
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
# COPYING contains exception text
%doc AUTHORS COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/sushi
%attr(755,root,root) %{_libexecdir}/org.gnome.NautilusPreviewer
%dir %{_libdir}/sushi
%attr(755,root,root) %{_libdir}/sushi/libsushi-1.0.so
%dir %{_libdir}/sushi/girepository-1.0
%{_libdir}/sushi/girepository-1.0/Sushi-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.NautilusPreviewer.service
%{_datadir}/metainfo/org.gnome.NautilusPreviewer.appdata.xml
%{_datadir}/sushi
