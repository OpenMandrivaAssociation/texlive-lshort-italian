# revision 15878
# category Package
# catalog-ctan /info/lshort/italian
# catalog-date 2007-01-01 00:42:16 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-lshort-italian
Version:	20070101
Release:	1
Summary:	Introduction to LaTeX in Italian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/italian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-italian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-italian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is the Italian translation of the Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-italian/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-italian/MANIFEST
%doc %{_texmfdistdir}/doc/latex/lshort-italian/Makefile
%doc %{_texmfdistdir}/doc/latex/lshort-italian/README
%doc %{_texmfdistdir}/doc/latex/lshort-italian/TRANSLATIONS
%doc %{_texmfdistdir}/doc/latex/lshort-italian/fixdate.pl
%doc %{_texmfdistdir}/doc/latex/lshort-italian/itlshort.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-italian/src.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
