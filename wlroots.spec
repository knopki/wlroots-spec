%global provider        github
%global provider_tld    com
%global project         swaywm
%global repo            wlroots
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          9383e1f76cdd9139c41304d9adefe3ab023077a3
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           wlroots
Version:        0.0.1
Release:        6.git%{shortcommit}%{?dist}
Summary:        Pluggable, composable, unopinionated modules for building a Wayland compositor
License:        MIT
URL:            https://%{provider_prefix}
# https://github.com/swaywm/wlroots/archive/9383e1f76cdd9139c41304d9adefe3ab023077a3/wlroots-9383e1f.tar.gz
Source:         https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Requires:       libcap
Requires:       libdrm
Requires:       libinput
Requires:       libwayland-cursor
Requires:       libwayland-egl
Requires:       libwayland-server
Requires:       libxkbcommon
Requires:       mesa-libEGL
Requires:       mesa-libgbm
Requires:       mesa-libGLES
Requires:       pixman
Requires:       systemd
Requires:       xcb-util-errors
Requires:       xcb-util-image
Requires:       xcb-util-wm
BuildRequires:  ctags-etags
BuildRequires:  gcc
BuildRequires:  libcap-devel
BuildRequires:  libdrm-devel
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  meson
BuildRequires:  pixman-devel
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  xcb-util-errors-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel

%description
%{summary}.

%prep
%setup -q -n %{repo}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md CONTRIBUTING.md docs/*
%license LICENSE
%{_libdir}/libwlroots.so.*

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       wlroots

%description devel
%{summary}.

%files devel
%{_libdir}/libwlroots.so
%{_libdir}/pkgconfig/wlroots.pc
%{_includedir}/wlr/*

%changelog
* Sun Oct 14 2018 Sergey Korolev <korolev.srg@gmail.com> - 0.0.1-6.git9383e1f
- Code update for sway 1.0-alpha.6 release

* Tue Aug 7 2018 Marcin Skarbek <rpm@skarbek.name> - 0.0.1-4.git28b0a40
- Code update for sway 1.0-alpha.5 release

* Tue Jul 17 2018 Marcin Skarbek <rpm@skarbek.name> - 0.0.1-3.git2a58d44
- Code update for sway 1.0-alpha.4 release

* Tue Jun 19 2018 Marcin Skarbek <rpm@skarbek.name> - 0.0.1-2.git9a1f0e2
- Code update for sway 1.0-alpha.3 release

* Wed May 23 2018 Marcin Skarbek <rpm@skarbek.name> - 0.0.1-1.git341af97
- Initial package
