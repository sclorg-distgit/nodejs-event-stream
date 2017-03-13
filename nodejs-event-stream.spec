%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
# Disabled as  some modules are not in fedora
%global enable_tests 0

%global module_name event-stream

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        3.3.2
Release:        6%{?dist}
Summary:        Construct pipes of streams of events

License:        MIT
URL:            https://github.com/dominictarr/event-stream
Source0:        https://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tape)
BuildRequires:  %{?scl_prefix}npm(it-is)
BuildRequires:  %{?scl_prefix}npm(asynct)
BuildRequires:  %{?scl_prefix}npm(stream-spec)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep map-stream ">=0.1.0"
%nodejs_fixdep split ">=0.3"
%nodejs_fixdep stream-combiner ">=0.0.4"

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps
%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
set -e; for t in test/*.js; do node $t; done
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.markdown examples
%license LICENCE
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.3.2-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.3.2-5
- Rebuilt with updated metapackage

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 3.3.2-3
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.2.2-1
- update to 3.2.2 upstream release

* Thu Jan 08 2015 Parag Nemade <pnemade AT redhat DOT com> - 3.2.1-1
- Update to 3.2.1

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.1.7-1
- Initial packaging
