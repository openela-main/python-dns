%global with_python3 0

Name:           python-dns
Version:        1.15.0
Release:        10%{?dist}
Summary:        DNS toolkit for Python

Group:          Development/Languages
License:        MIT
URL:            http://www.dnspython.org/

Source0: http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz

BuildArch:      noarch
Patch0:         test_fails_on_missing_file.patch

Provides:       python2-dns = %{version}-%{release}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%package -n python2-dns
Summary:        DNS toolkit for Python 2
Group:          Development/Languages
%{?python_provide:%python_provide python2-dns}

%description -n python2-dns
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%if 0%{?with_python3}
%package     -n python%{python3_pkgversion}-dns
Summary:        DNS toolkit for Python 3
Group:          Development/Languages
%{?python_provide:%python_provide python%{python3_pkgversion}-dns}

%description -n python%{python3_pkgversion}-dns
dnspython3 is a DNS toolkit for Python 3. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython3 provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.
%endif

%prep
%setup -q -n dnspython-%{version}
%patch0 -p1

# strip exec permissions so that we don't pick up dependencies from docs
find examples -type f | xargs chmod a-x

%build
%py2_build

%if 0%{?with_python3}
  %py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
  %py3_install
%endif

%check
%{__python2} setup.py test

%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-dns
%defattr(-,root,root,-)
# Add README.* when it is included with the source (commit a906279)
%doc {ChangeLog,LICENSE,examples}
%{python2_sitelib}/*egg-info
%{python2_sitelib}/dns

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-dns
%defattr(-,root,root,-)
# Add README.* when it is included with the source (commit a906279)
%doc {ChangeLog,LICENSE,examples}
%{python3_sitelib}/*egg-info
%{python3_sitelib}/dns
%endif

%changelog
* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.15.0-10
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.15.0-9
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Wed Jul 18 2018 Lumír Balhar <lbalhar@redhat.com> - 1.15.0-8
- First version for python27 module
