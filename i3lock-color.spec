%define debug_package %{nil}
%global commit ef8a7c6424b78e99e41fbe5f91c55460187376dd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		i3lock-color
Version:	2.git%{shortcommit}
Release:	2
Source0:	https://github.com/Raymo111/i3lock-color/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Summary:	The world's most popular non-default computer lockscreen.
URL:		https://github.com/Raymo111/i3lock-color
License:	BSD-2-Clause
Group:		Windows Manager/I3

BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xkbcommon-x11)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	giflib-devel
BuildRequires:  libev-devel
BuildRequires:  pam-devel

Conflicts: i3lock

Recommends: imagemagick

%description
A modern version of i3lock with color functionality and other features.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
autoreconf -fi
./configure --prefix=/usr \
            --sysconfdir=/etc \
            --enable-debug=no \
            --disable-sanitizers \
            CPPFLAGS="-I/usr/include/libev"
awk '!/all-configured/' Makefile > Makefile.new
mv Makefile.new Makefile
make

%install
%make_install DESTDIR="%{buildroot}"
install -Dm644 LICENSE "%{buildroot}%{_datadir}/licenses/%{name}/LICENSE"
install -Dm644 i3lock-bash "%{buildroot}%{_datadir}/bash-completion/completions/i3lock"
install -Dm644 i3lock-zsh "%{buildroot}%{_datadir}/zsh/vendor-completions/_i3lock"

%files
%doc CHANGELOG README*
%license LICENSE
%{_sysconfdir}/pam.d/i3lock
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1.zst
%{_datadir}/zsh/vendor-completions/_i3lock
%{_datadir}/bash-completion/completions/i3lock
