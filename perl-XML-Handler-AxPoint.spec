#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Handler-AxPoint
Summary:	XML::Handler::AxPoint Perl module - allows to create presentations in XML and PDF
Summary(pl):	Modu³ Perla XML::Handler::AxPoint - pozwala tworzyæ prezentacje w XML i PDF
Name:		perl-XML-Handler-AxPoint
Version:	1.30
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://axpoint.axkit.org/
BuildRequires:	perl >= 5.6
BuildRequires:	perl-PDFLib >= 0.11
BuildRequires:	perl-XML-SAX >= 0.09
BuildRequires:	perl-XML-SAX-Writer >= 0.39
BuildRequires:	rpm-perlprov >= 4.0.2-104
Requires:	perl-XML-SAX >= 0.09
Requires:	perl-XML-SAX-Writer >= 0.39
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a port of the original AxKit presentation tool AxPoint.
It allows you to write presentations in a very simple XML format, yet
create PDF results with slide transitions, bookmarks, images, etc.

%description -l pl
Ten modu³ jest portem oryginalnego narzêdzia AxPoint z zestawu AxKit.
Pozwala na pisywanie prezentacji w bardzo prostym formacie XML, a
nastêpnie tworzyæ wynikowe pliki PDF z przej¶ciami slajdów,
zak³adkami, obrazkami itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/axpoint
%{perl_sitelib}/XML/Handler/AxPoint.pm
%{_mandir}/man3/*
