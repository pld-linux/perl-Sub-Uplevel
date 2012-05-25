#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sub
%define		pnam	Uplevel
Summary:	Sub::Uplevel - apparently run a function in a higher stack frame
Summary(pl.UTF-8):	Sub::Uplevel - pozorne uruchomienie funkcji w wyższej ramce stosu
Name:		perl-Sub-Uplevel
Version:	0.24
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bea4037e8b2a0df563e25e6e44cb2e73
URL:		http://search.cpan.org/dist/Sub-Uplevel/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.47}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sub::Uplevel Perl module is for apparent running a function in a
higher stack frame.  Like Tcl's uplevel() function, but not quite so
dangerous.

%description -l pl.UTF-8
Moduł Perla Sub::Uplevel umożliwia pozorne uruchomienie funkcji w
wyższej ramce stosu. Działa podobnie do funkcji uplevel() Tcl-a, lecz
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
%doc Changes
%{perl_vendorlib}/Sub/Uplevel.pm
%{_mandir}/man3/Sub::Uplevel.3pm*
