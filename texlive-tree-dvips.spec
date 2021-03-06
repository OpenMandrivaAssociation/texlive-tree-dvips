# revision 21751
# category Package
# catalog-ctan /macros/latex209/contrib/trees/tree-dvips
# catalog-date 2011-03-14 14:09:23 +0100
# catalog-license lppl1
# catalog-version .91
Name:		texlive-tree-dvips
Version:	.91
Release:	11
Summary:	Trees and other linguists' macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/trees/tree-dvips
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tree-dvips.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tree-dvips.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a mechanism for specifying connected trees
that uses a tabular environment to generate node positions. The
package uses PostScript code, loaded by dvips, so output can
only be generated by use of dvips. The package lingmacros.sty
defines a few macros for linguists: \enumsentence for
enumerating sentence examples, simple tabular-based non-
connected tree macros, and gloss macros.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/tree-dvips/tree-dvips91.pro
%{_texmfdistdir}/tex/latex/tree-dvips/lingmacros.sty
%{_texmfdistdir}/tex/latex/tree-dvips/tree-dvips.sty
%doc %{_texmfdistdir}/doc/latex/tree-dvips/Makefile
%doc %{_texmfdistdir}/doc/latex/tree-dvips/README
%doc %{_texmfdistdir}/doc/latex/tree-dvips/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/tree-dvips/lingmacros-manual.pdf
%doc %{_texmfdistdir}/doc/latex/tree-dvips/lingmacros-manual.tex
%doc %{_texmfdistdir}/doc/latex/tree-dvips/tree-dvips91.script
%doc %{_texmfdistdir}/doc/latex/tree-dvips/tree-manual.pdf
%doc %{_texmfdistdir}/doc/latex/tree-dvips/tree-manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> .91-2
+ Revision: 757087
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> .91-1
+ Revision: 719803
- texlive-tree-dvips
- texlive-tree-dvips
- texlive-tree-dvips

