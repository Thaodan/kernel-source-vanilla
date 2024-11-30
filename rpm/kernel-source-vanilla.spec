Name: kernel-source-vanilla
Summary: The Linux Kernel Sources - Vanilla
Version:    6.11.10+initial_packaging.20241130181032.3066610
Release: 0
License: GPL-2.0-only
URL: https://kernel.org
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.rpmlintrc
BuildRequires: fdupes
BuildArch: noarch
AutoReqProv: off

%define patchversion 6.11.10
%define source_rel %release
# how the kernel release string (uname -r) should look like
%define kernelrelease %patchversion-%source_rel

%description
Vanilla Linux kernel sources without any changes except minor build fixes.

%prep
%setup -T -c

%build
%install
mkdir -p %{buildroot}%{_usrsrc}
pushd %{buildroot}%{_usrsrc}

tar -xf %{S:0}
mv %{name}-%{version}/upstream linux-%kernelrelease-vanilla
rm %{name}-%{version}/.gitmodules
rmdir %{name}-%{version}

find . -xtype l -delete -printf "deleted '%f'\n"
find . -name ".gitignore" -delete -printf "deleted '%f'\n"
%fdupes $PWD
popd

%files
%{_usrsrc}/linux-%kernelrelease-vanilla

%changelog
