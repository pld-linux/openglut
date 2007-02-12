Summary:	An open source evolution of the GLUT API
Summary(pl.UTF-8):	Oparta na otwartych źródłach ewolucja API biblioteki GLUT
Name:		openglut
Version:	0.6.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/openglut/%{name}-%{version}.tar.bz2
# Source0-md5:	9075d37d995d9f7dbb06a2e5fd9ffe20
Patch0:		%{name}-DESTDIR.patch
URL:		http://openglut.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGLUT is a fork of the old freeglut package. With freeglut aiming
for almost bug-for-bug compatibility with old GLUT, OpenGLUT is at
liberty to pursue improvements that do not fit into the freeglut
charter: OpenGLUT plans to extend the GLUT API in some ways, and to
deprecate - and eventually delete - GLUT features that are felt to be
poor fits.

%description -l pl.UTF-8
OpenGLUT to odgałęzienie starego pakietu freeglut. O ile celem
freegluta jest prawie pełna zgodność, nawet co do błędów, z biblioteką
GLUT, OpenGLUT ma swobodę dodawania ulepszeń nie pasujących do
freegluta: planuje rozszerzyć API GLUT-a na pewne sposoby, a traktować
jako niepożądane (i ewentualnie usunąć) pewnie źle pasujące opcje
GLUT-a.

%package devel
Summary:	Header files for openglut library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki openglut
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXxf86vm-devel

%description devel
Header files for openglut library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openglut.

%package static
Summary:	Static openglut library
Summary(pl.UTF-8):	Statyczna biblioteka openglut
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static openglut library.

%description static -l pl.UTF-8
Statyczna biblioteka openglut.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{__make} -C doc man-ascii

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libopenglut.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenglut.so
%{_libdir}/libopenglut.la
%{_includedir}/GL/openglut*.h
%{_mandir}/man3/glut*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenglut.a
