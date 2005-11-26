Summary:	Tiny ERP - free ERP and CRM software (client)
Summary(pl):	Tiny ERP - darmowe oprogramowanie ERP i CRM (klient)
Name:		tinyerp-client
Version:	3.1.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tinyerp.org/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	c2c36a43704b470190e771b478f3f771
Patch0:		%{name}-setup_py.patch
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

%description -l pl
Tiny ERP to pe�ny ERP i CRM. G��wne mo�liwo�ci to rozliczenia
(analityczne i finansowe), zarz�dzanie magazynem, zarz�dzanie
sprzeda�� i zakupami, automatyzacja zada�, kampanie reklamowe, help
desk, POS itp. Techniczne mo�liwo�ci obejmuj� serwer rozproszony,
elastyczne przep�ywy prac, obiektow� baz� danych, dynamiczne GUI,
konfigurowalne raporty oraz interfejsy SOAP i XML-RPC.

%prep
%setup -q
%patch0 -p1

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
