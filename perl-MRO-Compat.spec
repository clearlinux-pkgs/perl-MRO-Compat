#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MRO-Compat
Version  : 0.15
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/MRO-Compat-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/MRO-Compat-0.15.tar.gz
Summary  : 'mro::* interface compatibility for Perls < 5.9.5'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-MRO-Compat-license = %{version}-%{release}
Requires: perl-MRO-Compat-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
MRO::Compat - mro::* interface compatibility for Perls < 5.9.5
SYNOPSIS
package PPP;      use base qw/Exporter/;
package X;        use base qw/PPP/;
package Y;        use base qw/PPP/;
package Z;        use base qw/PPP/;

%package dev
Summary: dev components for the perl-MRO-Compat package.
Group: Development
Provides: perl-MRO-Compat-devel = %{version}-%{release}
Requires: perl-MRO-Compat = %{version}-%{release}

%description dev
dev components for the perl-MRO-Compat package.


%package license
Summary: license components for the perl-MRO-Compat package.
Group: Default

%description license
license components for the perl-MRO-Compat package.


%package perl
Summary: perl components for the perl-MRO-Compat package.
Group: Default
Requires: perl-MRO-Compat = %{version}-%{release}

%description perl
perl components for the perl-MRO-Compat package.


%prep
%setup -q -n MRO-Compat-0.15
cd %{_builddir}/MRO-Compat-0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MRO-Compat
cp %{_builddir}/MRO-Compat-0.15/LICENSE %{buildroot}/usr/share/package-licenses/perl-MRO-Compat/518f25cc48695460cd0f25f83e748663e6f77016
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MRO::Compat.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MRO-Compat/518f25cc48695460cd0f25f83e748663e6f77016

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
