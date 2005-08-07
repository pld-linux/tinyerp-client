Summary:	Tiny ERP - free ERP and CRM software (client)
#Summary(pl):	
Name:		tinyerp-client
Version:	2.1.3
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tinyerp.org/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	60c3e202f07be0ccac5abd6a733549f7
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
etc. Technical features include a distributed server, flexible workflows,
an object database, a dynamic GUI, customizable reports, and SOAP and
XML-RPC interfaces.

#%description -l pl
# TODO

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
%{py_sitescriptdir}/terp-client
%{_pixmapsdir}/*
%{_datadir}/terp-client
%{_mandir}/man?/*
