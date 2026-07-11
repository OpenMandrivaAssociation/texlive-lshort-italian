%global tl_name lshort-italian
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.2
Release:	%{tl_revision}.1
Summary:	Introduction to LaTeX in Italian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/italian
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-italian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-italian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the Italian translation of the Short Introduction to LaTeX2e.

