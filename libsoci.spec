#
# Conditional build:
%bcond_with	oracle		# build Oracle backend
%bcond_without	firebird	# don't build firebird backend
%bcond_without	mysql		# don't build MySQL backend
%bcond_without	postgresql	# don't build PostgreSQL backend
%bcond_without	sqlite3		# don't build sqlite3 backend
#
Summary:	The C++ Database Access Library
Summary(pl.UTF-8):   Biblioteka obsługi baz danych dla C++
Name:		libsoci
Version:	2.2.0
Release:	0.1
License:	Boost Software License
Group:		Libraries
Source0:	http://dl.sourceforge.net/soci/soci-%{version}.tar.bz2
# Source0-md5:	01c1baa50dff4c193cdb118b1190af51
URL:		http://soci.sourceforge.net/
BuildRequires:	libstdc++-devel
%{?with_firebird:BuildRequires:	Firebird-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_postgresql:BuildRequires:	postgresql-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The C++ Database Access Library.

%description -l pl.UTF-8
Biblioteka obsługi baz danych dla języka C++.

%package devel
Summary:	Header files for soci library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki soci
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for soci library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki soci.

%package static
Summary:	Static soci library
Summary(pl.UTF-8):   Statyczna biblioteka soci
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static soci library.

%description static -l pl.UTF-8
Statyczna biblioteka soci.

%package firebird
Summary:	Firebird backend for soci
Summary(pl.UTF-8):   Backend Firebirda dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description firebird
This package contains library with the Firebird binding for soci.

%description firebird -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy Firebird z soci.

%package firebird-static
Summary:	Firebird backend for soci (static version)
Summary(pl.UTF-8):   Backend Firebirda dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description firebird-static
This package contains static library with the Firebird binding for
soci.

%description firebird-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy Firebird z
soci.

%package mysql
Summary:	MySQL backend for soci
Summary(pl.UTF-8):   Backend MySQL-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
This package contains library with the MySQL binding for soci.

%description mysql -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy MySQL z soci.

%package mysql-static
Summary:	MySQL backend for soci (static version)
Summary(pl.UTF-8):   Backend MySQL-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description mysql-static
This package contains static library with the MySQL binding for soci.

%description mysql-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy MySQL z
soci.

%package oracle
Summary:	Oracle backend for soci
Summary(pl.UTF-8):   Backend Oracla dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description oracle
This package contains library with the Oracle binding for soci.

%description oracle -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy Oracle z soci.

%package oracle-static
Summary:	Oracle backend for soci (static version)
Summary(pl.UTF-8):   Backend Oracla dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description oracle-static
This package contains static library with the Oracle binding for soci.

%description oracle-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy Oracle z
soci.

%package postgresql
Summary:	PostgreSQL backend for soci
Summary(pl.UTF-8):   Backend PostgreSQL-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description postgresql
This package contains library with the PostgreSQL binding for soci.

%description postgresql -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy PostgreSQL z soci.

%package postgresql-static
Summary:	PostgreSQL backend for soci (static version)
Summary(pl.UTF-8):   Backend PostgreSQL-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description postgresql-static
This package contains static library with the PostgreSQL binding for
soci.

%description postgresql-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy PostgreSQL z
soci.

%package sqlite3
Summary:	sqlite3 backend for soci
Summary(pl.UTF-8):   Backend sqlite3 dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sqlite3
This package contains library with the sqlite3 binding for soci.

%description sqlite3 -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy sqlite3 z soci.

%package sqlite3-static
Summary:	sqlite3 backend for soci (static version)
Summary(pl.UTF-8):   Backend sqlite3-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description sqlite3-static
This package contains static library with the sqlite3 binding for
soci.

%description sqlite3-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy sqlite3 z
soci.

%prep
%setup -q -n soci-%{version}

%build
%configure \
	%{?debug:--enable-debug} \
	%{?with_firebird:--enable-backend-firebird} \
	%{?with_mysql:--enable-backend-mysql} \
	%{?with_oracle:--enable-backend-oracle} \
	%{?with_postgresql:--enable-backend-postgresql} \
	%{?with_sqlite3:--enable-backend-sqlite3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	firebird -p /sbin/ldconfig
%postun	firebird -p /sbin/ldconfig

%post	mysql -p /sbin/ldconfig
%postun	mysql -p /sbin/ldconfig

%post	oracle -p /sbin/ldconfig
%postun	oracle -p /sbin/ldconfig

%post	postgresql -p /sbin/ldconfig
%postun	postgresql -p /sbin/ldconfig

%post	sqlite3 -p /sbin/ldconfig
%postun	sqlite3 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE_1_0.txt README
%attr(755,root,root) %{_libdir}/libsoci_core*.so

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/libsoci_core*.la
%{_includedir}/soci

%files static
%defattr(644,root,root,755)
%{_libdir}/libsoci_core*.a

%if %{with firebird}
%files firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_firebird*.so
%{_libdir}/libsoci_firebird*.la

%files firebird-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_firebird*.a
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_mysql*.so
%{_libdir}/libsoci_mysql*.la

%files mysql-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_mysql*.a
%endif

%if %{with oracle}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_oracle*.so
%{_libdir}/libsoci_oracle*.la

%files oracle-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_oracle*.a
%endif

%if %{with postgresql}
%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_postgresql*.so
%{_libdir}/libsoci_postgresql*.la

%files postgresql-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_postgresql*.a
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_sqlite3*.so
%{_libdir}/libsoci_sqlite3*.la

%files sqlite3-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_sqlite3*.a
%endif
