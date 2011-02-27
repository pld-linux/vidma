Summary:	Virtual Disks Manipulator
Name:		vidma
Version:	0.0.3
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://download.przemoc.net/%{name}-%{version}.tar.gz
# Source0-md5:	c74713d778fb0af6520bdee0cce04a8e
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

sed -i 's/^VIDMA_VERSION/#VIDMA_VERSION/' Makefile

%build
%{__make} \
	VIDMA_VERSION="%{version}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D vidma $RPM_BUILD_ROOT%{_bindir}/vidma

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/vidma
