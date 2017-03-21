Summary: The elbuilds repository for Enterprise Linux
Name: elbuilds-release
Version: 1.1
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Base
URL: https://github.com/elbuilds/elbuilds-release
BuildArch: noarch
Source0: %{name}.tar.gz

# Only for Enterprise Linux >= 7
Requires: glibc >= 2.17

%description
This package contains the elbuilds repository for Enterprise Linux, as well as the public GPG keys used to sign packages.

%prep
%setup -qn %{name}

%build
# Do nothing

%install
%{__install} -Dpm 0644 elbuilds.repo %{buildroot}%{_sysconfdir}/yum.repos.d/elbuilds.repo
%{__install} -Dpm 0644 RPM-GPG-KEY-elbuilds %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-elbuilds

%clean
# Do nothing

%files
%defattr(-, root, root, 0755)
%license LICENSE
%pubkey RPM-GPG-KEY-elbuilds
%dir %{_sysconfdir}/yum.repos.d/
%config(noreplace) %{_sysconfdir}/yum.repos.d/elbuilds.repo
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-elbuilds

%changelog
* Tue Mar 21 2017 Qin Fandong <shell_way@foxmail.com> - 1.1-1
- Change RPM-GPG-KEY-elbuilds

* Tue Jan 17 2017 Qin Fandong <shell_way@foxmail.com> - 1.0-1
- Initial package.

