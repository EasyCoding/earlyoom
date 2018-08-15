Name: earlyoom
Version: 1.1
Release: 1%{?dist}

License: MIT
URL: https://github.com/rfjakob/%{name}
Summary: Early OOM Daemon for Linux
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: gcc

%description
The oom-killer generally has a bad reputation among Linux users.
This may be part of the reason Linux invokes it only when it has
absolutely no other choice. It will swap out the desktop
environment, drop the whole page cache and empty every buffer
before it will ultimately kill a process. At least that's what
I think what it will do. I have yet to be patient enough to wait
for it, sitting in front of an unresponsive system.

%prep
%autosetup -p1
sed -e '/systemctl/d' -i Makefile

%build
%set_build_flags
%make_build

%install
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} SYSTEMDUNITDIR=%{_unitdir}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%config(noreplace) %{_sysconfdir}/default/%{name}

%post
%systemd_post earlyoom.service

%preun
%systemd_preun earlyoom.service

%postun
%systemd_postun_with_restart earlyoom.service

%changelog
* Wed Aug 15 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1
- Initial SPEC release.
