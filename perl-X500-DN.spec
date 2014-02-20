%define upstream_name       X500-DN
%define upstream_version    0.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Parser and formatter for RFC 2253 style DN strings
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
Patch:		X500-DN-0.29-fix-parse-recdescent-version-check.patch

BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch

%description
This module provides a pure perl parser and formatter for RFC 2253
style DN strings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 
%patch -p 1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

# cleanup
rm -f %{buildroot}%{perl_vendorlib}/X500/*.pod

%files
%doc Changes README
%{perl_vendorlib}/X500
%{_mandir}/*/*

