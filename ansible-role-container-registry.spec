%global srcname ansible_role_container_registry
%global rolename ansible-role-container-registry

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Ansible role to deploy a container registry.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-container-registry
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3dist(ansible)


%description

Ansible role to deploy a container registry

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Thu May 21 2020 RDO <dev@lists.rdoproject.org> 1.2.0-1
- Update to 1.2.0


