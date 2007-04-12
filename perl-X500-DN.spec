Summary:	Parser and formatter for RFC 2253 style DN strings
Name: 		perl-X500-DN
Version: 	0.28
Release:	%mkrel 4
License: 	Artistic
Group: 		Development/Perl
URL:		http://www.cpan.org
Source:		X500-DN-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
This module provides a pure perl parser and formatter for RFC 2253
style DN strings.

%prep

%setup -n X500-DN-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
rm -f %{buildroot}%{perl_vendorlib}/X500/*.pod

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes MANIFEST README
%{perl_vendorlib}/X500/*.pm
%{_mandir}/*/*


