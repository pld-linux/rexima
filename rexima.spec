Summary:	A curses-based (and command-line) mixer for Linux
Summary(pl):	Opartny na bibliotekach ncurses mixer konsolowy
Name:		rexima
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/sound/mixers/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rexima is a curses-based interactive mixer. It can also be used from
the command-line. It's a deliberately straightforward, `sensible'
implementation - my response to the other curses-based mixers, where
you can't see the sliders for the chrome. Also, it gives a numeric
level readout (as well as the sliders), unlike most interactive mixers
I've used. It should work on any terminal with a screen size of at
least 80x24.

%description -l pl
Rexima to oparty na ncursesach mixer. Mo�e by� u�ywany r�wnie� z lini
polece�.

%prep
%setup -q

%build
%{__make} CC="gcc %{rpmcflags} -Wall -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install rexima		$RPM_BUILD_ROOT%{_bindir}
install rexima.1	$RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf {COPYING,ChangeLog,NEWS,README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rexima
%{_mandir}/man?/*
%doc *.gz
