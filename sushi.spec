Summary:	A quick previewer for Nautilus
Name:		sushi
Version:	0.1.90
Release:	1
License:	GPLv2+ with exceptions
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/sushi/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	68b6955eda9983f84b0c6f58ee059901
URL:		https://live.gnome.org/ThreePointOne/Features/FilePreviewing
BuildRequires:	clutter-devel
BuildRequires:	clutter-gst-devel
BuildRequires:	clutter-gtk-devel >= 1.0.2
BuildRequires:	evince-devel
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	intltool
BuildRequires:	libmusicbrainz3-devel

#Description from upstream's README.
%description
This is sushi,
a quick previewer for Nautilus,
the GNOME desktop file manager.

%package        devel
Summary:	Development files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure \
	--disable-static
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

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
%{_datadir}/dbus-1/services/*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libsushi-1.0.so
%{_datadir}/gir-1.0/*.gir

%clean
rm -rf $RPM_BUILD_ROOT
