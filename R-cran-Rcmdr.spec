%define modulename Rcmdr
%define realver 1.5-4
%define r_library %{_libdir}/R/library

Summary:	A platform-independent basic-statistics GUI for R
Name:		R-cran-%{modulename}
Version:	%(echo %realver|tr '-' '.')
Release:	%mkrel 2
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/src/contrib/Descriptions/Rcmdr.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
Requires:	R-base
Requires:	R-cran-car
Suggests:	R-cran-rgl
Suggests:	R-cran-relimp
Suggests:	R-cran-multcomp
Suggests:	R-cran-lmtest
Suggests:	R-cran-effects
Suggests:	R-cran-leaps
Suggests:	R-cran-aplpack
Suggests:	R-cran-Hmisc
Suggests:	R-cran-abind
Obsoletes:	rcmdr
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A platform-independent basic-statistics GUI for R language,
based on the tcltk package.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/R/library/%{modulename}
