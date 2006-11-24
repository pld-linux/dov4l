Summary:	Utility for setting V4L parameters
Summary(pl):	Narzêdzia do ustawiania parametrów V4L
Name:		dov4l
Version:	0.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/dov4l/%{name}-%{version}.tgz
# Source0-md5:	b4cdeb5c7ba2769eb3b63a086117cee5
Patch0:		%{name}-Makefile.patch
URL:		http://www.vanheusden.com/dov4l/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This console-tool sets parameters of a Video4Linux device. You can set
things like picture size, brightness, contrast, tuner frequency, etc.
etc. You can also retrieve a complete list of all current settings.

%description -l pl
To narzêdzie konsolowe ustawia parametry urz±dzenia Video4Linux.
Pozwala ustawiæ parametry takie jak rozmiar obrazu, jasno¶æ, kontrast,
czêstotliwo¶æ tunera itp. Mo¿na tak¿e odczytaæ pe³n± listê bie¿±cych
ustawieñ.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dov4l $RPM_BUILD_ROOT%{_bindir}
install dov4l.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dov4l
%{_mandir}/man1/dov4l.1*
