%global tl_name pst-cox
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.98.Beta
Release:	%{tl_revision}.1
Summary:	Drawing regular complex polytopes with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-cox
License:	lgpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pst-cox is a PSTricks package for drawing 2-dimensional projections of
complex regular polytopes (after the work of Coxeter). The package
consists of a macro library for drawing the projections. The complex
polytopes appear in the study of the root systems and play a crucial
role in many domains related to mathematics and physics. These polytopes
have been completely described by Coxeter in his book "Regular Complex
Polytopes". There exist only a finite numbers of exceptional regular
complex polytopes (for example the icosahedron) and some infinite series
(for example, one can construct a multi-dimensional analogue of the
hypercube in any finite dimension). The library contains two packages.
The first, pst-coxcoor, is devoted to the exceptional complex regular
polytopes whose coordinates have been pre-computed. The second, pst-
coxeterp, is devoted to the infinite series.

