#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Handler-AxPoint
Summary:	XML::Handler::AxPoint Perl module - allows to create presentations in XML and PDF
Summary(pl.UTF-8):	Moduł Perla XML::Handler::AxPoint - tworzenie prezentacji w XML-u i PDF
Name:		perl-XML-Handler-AxPoint
Version:	1.5
Release:	0.1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2e1eae47c8579189446eae331e4822dc
URL:		http://axpoint.axkit.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-PDFLib >= 0.14
#BuildRequires:	perl-Text-Iconv
BuildRequires:	perl-Time-Piece >= 1.08
%{?with_tests:BuildRequires:	perl-XML-Filter-XSLT}
BuildRequires:	perl-XML-SAX >= 0.09
BuildRequires:	perl-XML-SAX-Writer >= 0.39
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-SAX >= 0.09
Requires:	perl-XML-SAX-Writer >= 0.39
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a port of the original AxKit presentation tool AxPoint.
It allows you to write presentations in a very simple XML format, yet
create PDF results with slide transitions, bookmarks, images, etc.

%description -l pl.UTF-8
Ten moduł jest portem oryginalnego narzędzia AxPoint z zestawu AxKit.
Pozwala na pisywanie prezentacji w bardzo prostym formacie XML, a
następnie tworzyć wynikowe pliki PDF z przejściami slajdów,
zakładkami, obrazkami itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# missing file?
cp testfiles/{ax_logo,test}.png

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/axpoint
%{perl_vendorlib}/XML/Handler/AxPoint.pm
%{_mandir}/man3/*
