Name:           perl-DBIx-Array-Connect
Version:        0.08
Release:        1%{?dist}
Summary:        Database Connections from an INI Configuration File
License:        GPLv2
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBIx-Array-Connect/
Source0:        http://www.cpan.org/modules/by-module/DBIx/DBIx-Array-Connect-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(DBIx::Array) >= 0.14
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Package::New)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Sys::Path)
BuildRequires:  perl(Test::Simple) >= 0.44

#runtime requirements
Requires:       perl(DBIx::Array) >= 0.14
Requires:       perl(Sys::Path)

#base requirement not found by rpmbuild
Requires:       perl(Package::New)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Provides an easy way to construct database objects and connect to
databases while providing an easy way to centralize management of database
connection strings.

%prep
%setup -q -n DBIx-Array-Connect-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
*Sun Jan 05 2025 Michael R. Davis (mrdvt92@yahoo.com) 0.08-1
-Updated for 0.08
