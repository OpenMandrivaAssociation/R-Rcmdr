%global packname  Rcmdr
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.8_3
Release:          2
Summary:          R Commander
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.8-3.tar.gz
Requires:         R-tcltk R-grDevices R-utils R-car
Requires:         R-abind R-aplpack R-colorspace R-effects R-e1071
Requires:         R-foreign R-grid R-Hmisc R-lattice R-leaps R-lmtest
Requires:         R-MASS R-mgcv R-multcomp R-nlme R-nnet R-relimp R-rgl
Requires:         R-RODBC R-sem
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-tcltk R-grDevices R-utils R-car
BuildRequires:    R-abind R-aplpack R-colorspace R-effects R-e1071
BuildRequires:    R-foreign R-grid R-Hmisc R-lattice R-leaps R-lmtest
BuildRequires:    R-MASS R-mgcv R-multcomp R-nlme R-nnet R-relimp R-rgl
BuildRequires:    R-RODBC R-sem

%description
A platform-independent basic-statistics GUI (graphical user interface) for
R, based on the tcltk package.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
if [ x$DISPLAY != x ];	then %{_bindir}/R CMD check %{packname}
else			true
fi

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/po
