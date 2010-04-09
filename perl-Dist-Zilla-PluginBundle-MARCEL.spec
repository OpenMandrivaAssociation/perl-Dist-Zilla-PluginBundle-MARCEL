%define upstream_name    Dist-Zilla-PluginBundle-MARCEL
%define upstream_version 1.100980

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Build and release a distribution like MARCEL
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::MOP)
BuildRequires: perl(Dist::Zilla::Plugin::AutoPrereq)
BuildRequires: perl(Dist::Zilla::Plugin::AutoVersion)
BuildRequires: perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires: perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires: perl(Dist::Zilla::Plugin::CriticTests)
BuildRequires: perl(Dist::Zilla::Plugin::ExtraTests)
BuildRequires: perl(Dist::Zilla::Plugin::License)
BuildRequires: perl(Dist::Zilla::Plugin::MakeMaker)
BuildRequires: perl(Dist::Zilla::Plugin::Manifest)
BuildRequires: perl(Dist::Zilla::Plugin::ManifestSkip)
BuildRequires: perl(Dist::Zilla::Plugin::MetaJSON)
BuildRequires: perl(Dist::Zilla::Plugin::MetaProvides::Package)
BuildRequires: perl(Dist::Zilla::Plugin::MetaTests)
BuildRequires: perl(Dist::Zilla::Plugin::MetaYAML)
BuildRequires: perl(Dist::Zilla::Plugin::NextRelease)
BuildRequires: perl(Dist::Zilla::Plugin::PkgVersion)
BuildRequires: perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::PruneCruft)
BuildRequires: perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires: perl(Dist::Zilla::Plugin::Repository)
BuildRequires: perl(Dist::Zilla::Plugin::TaskWeaver)
BuildRequires: perl(Dist::Zilla::Plugin::UploadToCPAN)
BuildRequires: perl(Dist::Zilla::PluginBundle::Git)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Test::More) >= 0.940.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a plugin bundle to load all plugins that I am using. It is
equivalent to:

    [AutoVersion]

    ; -- fetch & generate files
    [AllFiles]
    [CompileTests]
    [CriticTests]
    [MetaTests]
    [PodTests]

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%perl_vendorlib/*


