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
Version:	0.2002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	509aedd3b680aea2c7a2fc67b9d5b007
URL:		http://search.cpan.org/dist/Sub-Uplevel/
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
%{_mandir}/man3/*.3pm*
