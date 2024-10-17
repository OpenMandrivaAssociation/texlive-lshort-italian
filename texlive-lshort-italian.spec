Name:		texlive-lshort-italian
Version:	57038
Release:	2
Summary:	Introduction to LaTeX in Italian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/italian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-italian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-italian.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Italian translation of the Short Introduction to
LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-italian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
