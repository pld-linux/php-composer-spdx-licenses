%define		pkgname	spdx-licenses
Summary:	SPDX licenses list and validation library
Name:		php-composer-%{pkgname}
Version:	1.1.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/composer/spdx-licenses/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3491a325766b3d04f92a1d4567b2abf8
Patch0:		res.patch
URL:		https://github.com/composer/spdx-licenses
Requires:	php(core) >= 5.3.2
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPDX licenses list and validation library.

Originally written as part of composer/composer, now extracted and
made available as a stand-alone library.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Composer/Spdx
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Composer/Spdx
cp -a res $RPM_BUILD_ROOT%{php_data_dir}/Composer/Spdx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.md LICENSE
# NOTE: dir shared with composer
%dir %{php_data_dir}/Composer
%{php_data_dir}/Composer/Spdx
