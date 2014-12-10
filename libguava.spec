Summary: Consistent hash from Google's guava library
Name: libguava
Version: 1.0
Release: 1
Group: Development/Libraries
URL: https://github.com/derElektrobesen/guava-hash
Packager: Pavel Berezhnoy <p.berezhnoy@corp.mail.ru>
License: BSD
Source: libguava-1.0.tar.gz

%description
Consistent hash from Google's guava library.

See http://en.wikipedia.org/wiki/Consistent_hashing for more information.

%build
tar -xzvf %{_sourcedir}/libguava-1.0.tar.gz
make %{?_smp_mflags} CFLAGS='%{optflags}'

%install
install -d %{buildroot}/%{_libdir}
install -m 755 libguava.so %{buildroot}/%{_libdir}

%files
/%{_libdir}/libguava.so
