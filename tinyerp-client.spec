# NOTE: NOT USABLE!
Summary:	Tiny ERP - free ERP and CRM software (client)
Summary(pl.UTF-8):   Tiny ERP - darmowe oprogramowanie ERP i CRM (klient)
Name:		tinyerp-client
Version:	3.2.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tinyerp.org/download/sources/%{name}-%{version}.tgz
# Source0-md5:	5e588d39d139f6b66c9f66e59e089d4c
Patch0:		%{name}-setup_py.patch
Patch1:		%{name}-start.patch
URL:		http://tinyerp.org/
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:  rpmbuild(macros) >= 1.219
Requires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny ERP is a complete ERP and CRM. The main features are accounting
(analytic and financial), stock management, sales and purchases
management, tasks automation, marketing campaigns, help desk, POS,
etc. Technical features include a distributed server, flexible
workflows, an object database, a dynamic GUI, customizable reports,
and SOAP and XML-RPC interfaces.

%description -l pl.UTF-8
Tiny ERP to pełny ERP i CRM. Główne możliwości to rozliczenia
(analityczne i finansowe), zarządzanie magazynem, zarządzanie
sprzedażą i zakupami, automatyzacja zadań, kampanie reklamowe, help
desk, POS itp. Techniczne możliwości obejmują serwer rozproszony,
elastyczne przepływy prac, obiektową bazę danych, dynamiczne GUI,
konfigurowalne raporty oraz interfejsy SOAP i XML-RPC.

%prep
%setup -q -n client
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--prefix=/usr \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/{CREDITS,INSTALL,README*}
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/tinyerp-client
%{_pixmapsdir}/*
%{_datadir}/tinyerp-client
%{_mandir}/man?/*
