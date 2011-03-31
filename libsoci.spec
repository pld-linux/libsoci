#
# Conditional build:
%bcond_with	oracle		# build Oracle backend
%bcond_without	mysql		# don't build MySQL backend
%bcond_without	postgresql	# don't build PostgreSQL backend
#
Summary:	The C++ Database Access Library
Summary(pl.UTF-8):	Biblioteka obsługi baz danych dla C++
Name:		libsoci
Version:	3.0.0
Release:	2
License:	Boost Software License
Group:		Libraries
Source0:	http://dl.sourceforge.net/soci/soci-%{version}.tar.gz
# Source0-md5:	1bf7dd244764e53557c1ecc01fdfac96
Patch0:		%{name}-gcc43.patch
Patch1:		%{name}-flags.patch
URL:		http://soci.sourceforge.net/
BuildRequires:	libstdc++-devel
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_postgresql:BuildRequires:	postgresql-devel}
BuildRequires:	tcl
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

%package mysql
Summary:	MySQL backend for soci
Summary(pl.UTF-8):	Backend MySQL-a dla soci
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
This package contains library with the MySQL binding for soci.

%description mysql -l pl.UTF-8
Ten pakiet zawiera bibliotekę do połączenia bazy MySQL z soci.

%package mysql-static
Summary:	MySQL backend for soci (static version)
Summary(pl.UTF-8):	Backend MySQL-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description mysql-static
This package contains static library with the MySQL binding for soci.

%description mysql-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy MySQL z
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

%package oracle-static
Summary:	Oracle backend for soci (static version)
Summary(pl.UTF-8):	Backend Oracla dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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

%package postgresql-static
Summary:	PostgreSQL backend for soci (static version)
Summary(pl.UTF-8):	Backend PostgreSQL-a dla soci (wersja statyczna)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description postgresql-static
This package contains static library with the PostgreSQL binding for
soci.

%description postgresql-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę do połączenia bazy PostgreSQL z
soci.

%prep
%setup -q -n soci-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure \
	--include-prefix=$RPM_BUILD_ROOT%{_includedir}/soci \
	--lib-prefix=$RPM_BUILD_ROOT%{_libdir} \
	--postgresql-include=%{_includedir} \
	--postgresql-lib=%{_libdir} \
	--mysql-include=%{_includedir}/mysql \
	--mysql-lib=%{_libdir}

export CXXFLAGS="${CXXFLAGS:-%rpmcxxflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	mysql -p /sbin/ldconfig
%postun	mysql -p /sbin/ldconfig

%post	oracle -p /sbin/ldconfig
%postun	oracle -p /sbin/ldconfig

%post	postgresql -p /sbin/ldconfig
%postun	postgresql -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE_1_0.txt README
%attr(755,root,root) %{_libdir}/libsoci_core*.so

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_includedir}/soci

%files static
%defattr(644,root,root,755)
%{_libdir}/libsoci_core*.a

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_mysql*.so

%files mysql-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_mysql*.a
%endif

%if %{with oracle}
%files oracle
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_oracle*.so

%files oracle-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_oracle*.a
%endif

%if %{with postgresql}
%files postgresql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoci_postgresql*.so

%files postgresql-static
%defattr(644,root,root,755)
%{_libdir}/libsoci_postgresql*.a
%endif
