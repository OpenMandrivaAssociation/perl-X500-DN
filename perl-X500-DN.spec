%define module	X500-DN
%define name	perl-%{module}
%define version 0.29
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Parser and formatter for RFC 2253 style DN strings
License: 	Artistic
Group: 		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/X500/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module provides a pure perl parser and formatter for RFC 2253
style DN strings.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

# cleanup
rm -f %{buildroot}%{perl_vendorlib}/X500/*.pod

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/X500
%{_mandir}/*/*
