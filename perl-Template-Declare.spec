%define upstream_name    Template-Declare
%define upstream_version 0.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Template::Declare TAG set for Mozilla's em-rdf
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::ISA)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Lint)
BuildRequires: perl(String::BufferStack)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'Template::Declare' is a pure-Perl declarative HTML/XUL/RDF/XML templating
system.

Yes. Another one. There are many others like it, but this one is ours.

A few key features and buzzwords:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/Template/


