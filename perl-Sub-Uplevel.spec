#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sub
%define		pnam	Uplevel
Summary:	Sub::Uplevel - apparently run a function in a higher stack frame
Summary(pl):	Sub::Uplevel - pozorne uruchomienie funkcji w wy�szej ramce stosu
Name:		perl-Sub-Uplevel
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed0cbc3ef75df91a22fd0d0404336765
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

%description -l pl
Modu� Perla Sub::Uplevel umo�liwia pozorne uruchomienie funkcji w
wy�szej ramce stosu. Dzia�a podobnie do funkcji uplevel() Tcl-a, lecz
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
