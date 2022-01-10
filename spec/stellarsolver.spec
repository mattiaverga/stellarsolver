%define __cmake_in_source_build %{_vpath_builddir}

Name: stellarsolver
Version: 1.6.git
Release: %(date -u +%%Y%%m%%d%%H%%M%%S)%{?dist}
Summary: The Cross Platform Sextractor and Astrometry.net-Based Internal Astrometric Solver

License: LGPLv3

URL: https://github.com/rlancaste/stellarsolver
Source0: https://github.com/rlancaste/stellarsolver/archive/master.tar.gz

%global debug_package %{nil}
%define __find_requires %{nil}

Provides: stellarsolver.so(64-bit)
Provides: libstellarsolver.so.1()(64bit)
Provides: stellarsolver.so
Provides: stellarsolver.a

BuildRequires: cmake
BuildRequires: systemd
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(wcslib)
BuildRequires: pkgconfig(Qt5) >= 5.4


%description
An Astrometric Plate Solver for Mac, Linux, and Windows, built on Astrometry.net and SEP (sextractor)


%prep -v
%autosetup -v

%build
%cmake .
%make_build


%install
#find %buildroot -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +
%cmake_install
%ldconfig_scriptlets


%files
%{_libdir}/*
%{_includedir}/*

%license LICENSE

%changelog
* Thu Dec 29 2020 Rob Lancaster <rlancaste@gmail.com> 1.6.git
- Updating Spec file to latest version and Supporting additional ASTAP features
* Thu Oct 08 2020 Jim Howard <jh.xsnrg+fedora@gmail.com> 1.4.git
- introduction of spec file to build RPM packages from git
