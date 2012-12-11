Name:         rspfd
License:      GPL
Group:        Communications
Version:      1.1
Release:      1
Summary:      Routing Daemon for Use Over Amateur Radio Links
Source0:      http://rspf.sourceforge.net/rspf/rspfd-%{version}.tar.gz
URL:          http://rspf.sourceforge.net/

%description
RSPFd is a routing daemon specifically designed to be used over amateur
radio links.  This implementation adheres as closely as possible to
RSPF v2.2. Most other implementations (part of *NOS programs) follow
RSPF v2.0 somewhat.



Authors:
--------
    Craig Small <csmall@small.dropbear.id.au>

%prep
%setup -q

%build
%configure2_5x
%make

%install
#make install DESTDIR=$RPM_BUILD_ROOT
%makeinstall_std

%files
%doc AUTHORS README
%{_mandir}/man5/*.xz
%{_mandir}/man8/*.xz
%{_sbindir}/*


%changelog
* Thu May 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 798047
- imported package rspfd

