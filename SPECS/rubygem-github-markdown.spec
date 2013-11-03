%global     gemdir %{gem_dir}
%global     gemname github-markdown
%global gem_name    %{gemname}
%global     geminstdir %{gem_instdir}

%if 0%{?fedora} < 19
%global rubyabi 1.9.1
%endif

Summary:        Self-contained Markdown parser for GitHub
Name:           rubygem-%{gemname}
Version:        0.6.1
Release:        1%{?dist}
Group:          Development/Languages
License:        MIT
URL:            rubygems.org/gems/github-markdown
Source0:        http://rubygems.org/gems/%{gemname}-%{version}.gem

%if 0%{?fedora} >= 19
Requires:   ruby(release)
BuildRequires:  ruby(release)
%else
Requires:   ruby(abi) = %{rubyabi}
Requires:   ruby 
BuildRequires:  ruby(abi) = %{rubyabi}
BuildRequires:  ruby 
%endif
BuildRequires:  ruby-devel
Requires:       rubygems >= 1.3.6
Requires:       rubygem(rubyforge) >= 2.0.4
Requires:       rubygem(rake)      >= 0.8.7
BuildRequires:  rubygems-devel >= 1.3.6
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(json_pure)
Provides:       rubygem(%{gemname}) = %{version}

%description
GitHub uses what we're calling "GitHub Flavored Markdown" (GFM) for messages, issues, and comments. It differs from standard Markdown (SM) in a few significant ways and adds some additional functionality.

%package    doc
Summary:    Documentation for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

pushd .%{geminstdir}

%_fixperms .

popd

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{_prefix}/* \
    %{buildroot}%{_prefix}/

chmod 0644 %{buildroot}%{gemdir}/cache/*gem

%files
%defattr(-, root, root, -)
%dir %{geminstdir}/
%{geminstdir}/bin/
%{geminstdir}/lib/
%{geminstdir}/ext/
%{geminstdir}/%{gemname}.gemspec
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%doc %{geminstdir}/[A-Z]*

%files  doc
%defattr(-,root,root,-)
%{geminstdir}/test/
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Sun Nov 3 2013 Keiran Smith <fedora@affix.me> - 0.6.1-1
- Initial Package
