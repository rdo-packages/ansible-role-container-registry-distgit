%{!?upstream_version: %global upstream_version %{commit}}
%global commit d6a749ace464ad77684874d9e4216d9a3ef280e2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git
# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%global srcname ansible_role_container_registry
%global rolename ansible-role-container-registry

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.0.1
Release:        0.1%{?alphatag}%{?dist}
Summary:        Ansible role to deploy a container registry.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/ansible-role-container-registry
Source0:        https://github.com/openstack/%{rolename}/archive/%{commit}.tar.gz#/%{rolename}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-d2to1
Requires:       ansible
%else
BuildRequires:  python%{pyver}-d2to1
%if 0%{?rhel} > 7
Requires: ansible
%else
Requires: ansible-python3
%endif
%endif


%description

Ansible role to deploy a container registry

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 1.0.1-0.1.d6a749agit
- Update to pre-release 1.0.1 (d6a749ace464ad77684874d9e4216d9a3ef280e2)


