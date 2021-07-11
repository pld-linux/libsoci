# TODO: db2
#
# Conditional build:
%bcond_without	firebird	# Firebird backend
%bcond_without	mysql		# MySQL backend
%bcond_without	odbc		# ODBC backend
%bcond_with	oci		# Oracle backend
%bcond_without	pgsql		# PostgreSQL backend
%bcond_without	sqlite3		# SQLite3 backend
%bcond_without	instantclient	# Oracle backend build against oracle-instantclient package
#
Summary:	The C++ Database Access Library
Summary(pl.UTF-8):	Biblioteka obsługi baz danych dla C++
Name:		libsoci
Version:	4.0.2
Release:	1
License:	Boost Software License
Group:		Libraries
Source0:	http://downloads.sourceforge.net/soci/soci-%{version}.tar.gz
# Source0-md5:	c35e654558e0c0b344960d5888e5d39e
URL:		http://soci.sourceforge.net/
%{?with_firebird:BuildRequires:	Firebird-devel}
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel >= 1:4.7
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_oci:%{?with_instantclient:BuildRequires:	oracle-instantclient-devel >= 10}}
%{?with_pgsql:BuildRequires:	postgresql-devel >= 7}
BuildRequires:	rpm-build >= 4.6
%{?with_sqlite3:BuildRequires:	sqlite3-devel >= 3}
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The C++ Database Access Library.

%description -l pl.UTF-8
Biblioteka obsługi baz danych dla języka C++.

%package devel
Summary:	Header files for soci library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for soci library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci.

%package static
Summary:	Static soci library
Summary(pl.UTF-8):	Statyczna biblioteka soci
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static soci library.

%description static -l pl.UTF-8
Statyczna biblioteka soci.

%package firebird
Summary:	Firebird backend for soci
Summary(pl.UTF-8):	Backend Firebird-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description firebird
This package contains library with the Firebird binding for soci.

%description firebird -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy Firebird z soci.

%package firebird-devel
Summary:	Header files for soci Firebird backend
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci Firebird
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-firebird = %{version}-%{release}

%description firebird-devel
Header files for soci Firebird backend.

%description firebird-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci Firebird.

%package firebird-static
Summary:	Firebird backend for soci (static version)
Summary(pl.UTF-8):	Backend Firebird-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-firebird-devel = %{version}-%{release}

%description firebird-static
This package contains static library with the Firebird binding for
soci.

%description firebird-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy Firebird z
soci.

%package mysql
Summary:	MySQL backend for soci
Summary(pl.UTF-8):	Backend MySQL-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
This package contains library with the MySQL binding for soci.

%description mysql -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy MySQL z soci.

%package mysql-devel
Summary:	Header files for soci MySQL backend
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci MySQL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mysql = %{version}-%{release}

%description mysql-devel
Header files for soci MySQL backend.

%description mysql-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci MySQL.

%package mysql-static
Summary:	MySQL backend for soci (static version)
Summary(pl.UTF-8):	Backend MySQL-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-mysql-devel = %{version}-%{release}

%description mysql-static
This package contains static library with the MySQL binding for soci.

%description mysql-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy MySQL z
soci.

%package odbc
Summary:	ODBC backend for soci
Summary(pl.UTF-8):	Backend ODBC-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description odbc
This package contains library with the ODBC binding for soci.

%description odbc -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy ODBC z soci.

%package odbc-devel
Summary:	Header files for soci ODBC backend
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci ODBC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-odbc = %{version}-%{release}

%description odbc-devel
Header files for soci ODBC backend.

%description odbc-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci ODBC.

%package odbc-static
Summary:	ODBC backend for soci (static version)
Summary(pl.UTF-8):	Backend ODBC-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-odbc-devel = %{version}-%{release}

%description odbc-static
This package contains static library with the ODBC binding for soci.

%description odbc-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy ODBC z
soci.

%package oracle
Summary:	Oracle backend for soci
Summary(pl.UTF-8):	Backend Oracla dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description oracle
This package contains library with the Oracle binding for soci.

%description oracle -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy Oracle z soci.

%package oracle-devel
Summary:	Header files for soci Oracle backend
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci Oracle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-oracle = %{version}-%{release}

%description oracle-devel
Header files for soci Oracle backend.

%description oracle-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci Oracle.

%package oracle-static
Summary:	Oracle backend for soci (static version)
Summary(pl.UTF-8):	Backend Oracla dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-oracle-devel = %{version}-%{release}

%description oracle-static
This package contains static library with the Oracle binding for soci.

%description oracle-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy Oracle z
soci.

%package postgresql
Summary:	PostgreSQL backend for soci
Summary(pl.UTF-8):	Backend PostgreSQL-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description postgresql
This package contains library with the PostgreSQL binding for soci.

%description postgresql -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy PostgreSQL z soci.

%package postgresql-devel
Summary:	Header files for soci PostgreSQL backend
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci PostgreSQL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-postgresql = %{version}-%{release}

%description postgresql-devel
Header files for soci PostgreSQL backend.

%description postgresql-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci PostgreSQL.

%package postgresql-static
Summary:	PostgreSQL backend for soci (static version)
Summary(pl.UTF-8):	Backend PostgreSQL-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-postgresql-devel = %{version}-%{release}

%description postgresql-static
This package contains static library with the PostgreSQL binding for
soci.

%description postgresql-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy PostgreSQL
z soci.

%package sqlite3
Summary:	SQLite3 backend for soci
Summary(pl.UTF-8):	Backend SQLite3-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sqlite3
This package contains library with the SQLite3 binding for soci.

%description sqlite3 -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy SQLite3 z soci.

%package sqlite3-devel
Summary:	Header files for soci SQLite3 backend
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki soci SQLite3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-sqlite3 = %{version}-%{release}

%description sqlite3-devel
Header files for soci SQLite3 backend.

%description sqlite3-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci SQLite3.

%package sqlite3-static
Summary:	SQLite3 backend for soci (static version)
Summary(pl.UTF-8):	Backend SQLite3-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-sqlite3-devel = %{version}-%{release}

%description sqlite3-static
This package contains static library with the SQLite3 binding for
soci.

%description sqlite3-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy SQLite3 z
soci.

%package apidocs
Summary:	Documentation for SOCI library
Summary(pl.UTF-8):	Dokumentacja biblioteki SOCI
Group:		Documentation
BuildArch:	noarch

%description apidocs
Documentation for SOCI library.

%description apidocs -l pl.UTF-8
Dokumentacja biblioteki SOCI.

%prep
%setup -q -n soci-%{version}

%build
install -d build
cd build
%{?with_oci:%{?with_instantclient:export ORACLE_HOME=%{_libdir}}}
%cmake .. \
	-DLIBDIR:PATH=%{_lib} \
	%{?with_instantclient:-DORACLE_INCLUDE_DIR=/usr/include/oracle/client} \
	-DWITH_DB2=OFF \
	%{!?with_firebird:-DWITH_FIREBIRD=OFF} \
	%{!?with_mysql:-DWITH_MYSQL=OFF} \
	%{!?with_odbc:-DWITH_ODBC=OFF} \
	%{!?with_oci:-DWITH_ORACLE=OFF} \
	%{!?with_pgsql:-DWITH_POSTGRESQL=OFF} \
	%{!?with_sqlite3:-DWITH_SQLITE3=OFF}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# disable completeness check incompatible with split packaging
%{__sed} -i -e '/^foreach(target .*IMPORT_CHECK_TARGETS/,/^endforeach/d; /^unset(_IMPORT_CHECK_TARGETS)/d' $RPM_BUILD_ROOT%{_libdir}/cmake/SOCI/SOCITargets.cmake

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	firebird -p /sbin/ldconfig
%postun	firebird -p /sbin/ldconfig

%post	mysql -p /sbin/ldconfig
%postun	mysql -p /sbin/ldconfig

%post	odbc -p /sbin/ldconfig
%postun	odbc -p /sbin/ldconfig

%post	oracle -p /sbin/ldconfig
%postun	oracle -p /sbin/ldconfig

%post	postgresql -p /sbin/ldconfig
%postun	postgresql -p /sbin/ldconfig

%post	sqlite3 -p /sbin/ldconfig
%postun	sqlite3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE_1_0.txt README.md
%attr(755,root,root) %{_libdir}/libsoci_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_core.so.4.0
%attr(755,root,root) %{_libdir}/libsoci_empty.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_empty.so.4.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_core.so
%attr(755,root,root) %{_libdir}/libsoci_empty.so
%dir %{_includedir}/soci
%{_includedir}/soci/*.h
%{_includedir}/soci/empty
%{_libdir}/cmake/SOCI

%files static
%defattr(644,root,root,755)
%{_libdir}/libsoci_core.a
%{_libdir}/libsoci_empty.a

%if %{with firebird}
%files firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_firebird.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_firebird.so.4.0

%files firebird-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_firebird.so
%{_includedir}/soci/firebird

%files firebird-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_firebird.a
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_mysql.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_mysql.so.4.0

%files mysql-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_mysql.so
%{_includedir}/soci/mysql

%files mysql-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_mysql.a
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_odbc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_odbc.so.4.0

%files odbc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_odbc.so
%{_includedir}/soci/odbc

%files odbc-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_odbc.a
%endif

%if %{with oci}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_oracle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_oracle.so.4.0

%files oracle-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_oracle.so
%{_includedir}/soci/oracle

%files oracle-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_oracle.a
%endif

%if %{with pgsql}
%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_postgresql.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_postgresql.so.4.0

%files postgresql-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_postgresql.so
%{_includedir}/soci/postgresql

%files postgresql-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_postgresql.a
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_sqlite3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsoci_sqlite3.so.4.0

%files sqlite3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_sqlite3.so
%{_includedir}/soci/sqlite3

%files sqlite3-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_sqlite3.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/*
