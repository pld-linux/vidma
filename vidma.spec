Summary:	Virtual Disks Manipulator
Name:		vidma
Version:	0.0.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://download.przemoc.net/%{name}-%{version}.tar.gz
# Source0-md5:	c7996cc1baea952023ec25ef52af1f64
URL:		https://github.com/przemoc/vidma
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vidma - Virtual Disks Manipulator

Utility for manipulating virtual disk images. Features:
- resizing fixed-size images
- operations can be done in-place

Supported formats:
- VDI - Virtual Disk Image, used mostly by VirtualBox

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D vidma	$RPM_BUILD_ROOT%{_bindir}/vidma
install -D vidma.1	$RPM_BUILD_ROOT%{_mandir}/man1/vidma.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/vidma
%{_mandir}/man1/*
