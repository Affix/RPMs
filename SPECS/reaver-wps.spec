Name:		reaver	
Version:	1.4
Release:	1%{?dist}
Summary:	reaver-wps is a Brute force attack against Wifi Protected Setup

Group:		applications/security
License:	GNU GPL V2
URL:		http://code.google.com/p/reaver-wps
Source0:	http://reaver-wps.googlecode.com/files/reaver-1.4.tar.gz

BuildRequires:	libpcap-devel
BuildRequires:	libsqlite3x-devel
Requires:	libpcap
Requires:	libpcap-devel

patch1: reaver-1.4-spec.patch

%description
Reaver implements a brute force attack against Wifi Protected Setup (WPS) registrar PINs in order to recover WPA/WPA2 passphrases, as described in http://sviehb.files.wordpress.com/2011/12/viehboeck_wps.pdf.

Reaver has been designed to be a robust and practical attack against WPS, and has been tested against a wide variety of access points and WPS implementations.

On average Reaver will recover the target AP's plain text WPA/WPA2 passphrase in 4-10 hours, depending on the AP. In practice, it will generally take half this time to guess the correct WPS pin and recover the passphrase. 


%prep
%setup -q
cd src
%patch1 -p0

%build
cd src
%configure
make %{?_smp_mflags}


%install
cd src
mkdir -p %{buildroot}/usr/bin
make BINDIR=%{buildroot}/usr/bin CONFDIR=%{buildroot}/etc/reaver DESTDIR=%{buildroot} install


%files
%doc
/etc/reaver/reaver.db
/usr/bin/reaver
/usr/bin/wash



%changelog

* Sun Oct 20 2013 Keiran Smith <fedora@affix.me> - 1.4-1
- Initial Package Build
