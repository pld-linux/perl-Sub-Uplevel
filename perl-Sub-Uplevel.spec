#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sub
%define	pnam	Uplevel
Summary:	Sub::Uplevel - apparently run a function in a higher stack frame
Summary(pl):	Sub::Uplevel - pozorne uruchomienie funkcji w wy¿szej ramce stosu
Name:		perl-%{pdir}-%{pnam}
Version:	0.08
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee9f20f8a45f92672a95681446dce9bd
BuildRequires:	perl-devel >= 5.005
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sub::Uplevel Perl module is for apparent running a function in a
higher stack frame.  Like Tcl's uplevel() function, but not quite so
dangerous.

%description -l pl
Modu³ Perla Sub::Uplevel umo¿liwia pozorne uruchomienie funkcji w
wy¿szej ramce stosu. Dzia³a podobnie do funkcji uplevel() Tcl-a, lecz
nie jest tak niebezpieczny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*.3pm*
