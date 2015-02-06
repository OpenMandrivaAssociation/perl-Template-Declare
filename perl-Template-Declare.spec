%define upstream_name    Template-Declare
%define upstream_version 0.46

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.46
Release:	3

Summary:	Template::Declare TAG set for Mozilla's em-rdf
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/Template-Declare-0.46.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Lint)
BuildRequires:	perl(String::BufferStack)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildArch:	noarch

%description
'Template::Declare' is a pure-Perl declarative HTML/XUL/RDF/XML templating
system.

Yes. Another one. There are many others like it, but this one is ours.

A few key features and buzzwords:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/Template/

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.450.0-1mdv2011.0
+ Revision: 654377
- update to new version 0.45

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1mdv2011.0
+ Revision: 622948
- new version

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 541109
- import perl-Template-Declare


* Fri Apr 30 2010 cpan2dist 0.43-1mdv
- initial mdv release, generated with cpan2dist

