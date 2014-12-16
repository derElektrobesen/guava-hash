%define __autobuild__ 0

%if %{__autobuild__}
%define release 1
%else
%define release PKG_RELEASE
%endif

Summary: Consistent hash from Google's guava library
Name: libguava
Version: 1.0
Release: 1
Group: Development/Libraries
URL: https://github.com/derElektrobesen/guava-hash
License: BSD
%if %{__autobuild__}
Packager: BUILD_USER
Source0: guava-hash-GIT_TAG.tar.bz2
%else
Packager: Pavel Berezhnoy <p.berezhnoy@corp.mail.ru>
Source: libguava-1.0.tar.gz
%endif

%description
Consistent hash from Google's guava library.

See http://en.wikipedia.org/wiki/Consistent_hashing for more information.
%{lua:
if rpm.expand("%{__autobuild__}") == '1'
then
print("From tag: GIT_TAG\n")
print("Git hash: GITHASH\n")
print("Build by: BUILD_USER\n")
end}

%prep
%if %{__autobuild__}
%setup -q -n guava-hash
%else
%setup -q
%endif

%build
make %{?_smp_mflags} CFLAGS='%{optflags}' so

%install
install -d %{buildroot}/%{_libdir}
install -m 755 libguava.so %{buildroot}/%{_libdir}

%files
/%{_libdir}/libguava.so
