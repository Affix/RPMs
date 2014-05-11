Name:	fragrouter	
Version:	1.6
Release:	1%{?dist}
Summary:	A simple network intrusion detection evasion toolkit

Group:		System
License:	GPL
URL:		http://packetstormsecurity.com/files/download/15917/fragrouter-1.6.tar.gz
Source0:	fragrouter-1.6.tar.gz

BuildRequires:	libpcap-devel libnet-devel
Requires:	libpcap libnet

%description
A network intrusion toolkit

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install install_prefix=%{buildroot}


%files
/usr/sbin/fragrouter

%doc
/usr/share/man/man8/fragrouter.8.gz


%changelog
* Sun May 11 2014 Keiran Smith <fedora@affix.me> 1.6-1
- Initial RPM release
