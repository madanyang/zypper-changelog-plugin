#
# spec file for package zypper-changelog
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           zypper-changelog-plugin
Version:        0.1 
Release:        1%{?dist}
Summary:        Changelog listing tool
License:        GPL-2.0 
Group:          System/Packages
Supplements:    zypper
URL:            https://github.com/bzoltan1/zypper-changelog-plugin.git
Source:         zypper-changelog-plugin-0.1.tar.gz
Requires:       python3
BuildArch:      noarch

%description
This tool is to show the changelog of packages in the repository
%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 755 zypper-changelog %{buildroot}%{_bindir}/zypper-changelog
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8
install -m 644 zypper-changelog.8 %{buildroot}/%{_mandir}/man8/

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/zypper-changelog
%{_mandir}/man8/*

%changelog