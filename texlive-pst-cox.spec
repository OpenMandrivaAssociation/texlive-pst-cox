Name:		texlive-pst-cox
Version:	15878
Release:	1
Summary:	Drawing regular complex polytopes with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-cox
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-cox is a PSTricks package for drawing 2-dimensional
projections of complex regular polytopes (after the work of
Coxeter). The package consists of a macro library for drawing
the projections. The complex polytopes appear in the study of
the root systems and play a crucial role in many domains
related to mathematics and physics. These polytopes have been
completely described by Coxeter in his book "Regular Complex
Polytopes". There exist only a finite numbers of exceptional
regular complex polytopes (for example the icosahedron) and
some infinite series (for example, one can construct a multi-
dimensional analogue of the hypercube in any finite dimension).
The library contains two packages. The first, pst-coxcoor, is
devoted to the exceptional complex regular polytopes whose
coordinates have been pre-computed. The second, pst-coxeterp,
is devoted to the infinite series.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-cox/pst-coxeter.pro
%{_texmfdistdir}/tex/generic/pst-cox/pst-coxcoor.tex
%{_texmfdistdir}/tex/generic/pst-cox/pst-coxeterp.tex
%{_texmfdistdir}/tex/latex/pst-cox/pst-coxcoor.sty
%{_texmfdistdir}/tex/latex/pst-cox/pst-coxeterp.sty
%doc %{_texmfdistdir}/doc/generic/pst-cox/README
%doc %{_texmfdistdir}/doc/generic/pst-cox/gpl.txt
%doc %{_texmfdistdir}/doc/generic/pst-cox/lgpl.txt
%doc %{_texmfdistdir}/doc/generic/pst-cox/pst-coxcoor/Gallery.tex
%doc %{_texmfdistdir}/doc/generic/pst-cox/pst-coxcoor/pst-coxcoor_doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-cox/pst-coxcoor/pst-coxcoor_doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-cox/pst-coxeterp/Gallery.tex
%doc %{_texmfdistdir}/doc/generic/pst-cox/pst-coxeterp/pst-coxeterp_doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-cox/pst-coxeterp/pst-coxeterp_doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
