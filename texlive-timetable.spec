# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/timetable/timetable.tex
# catalog-date 2008-09-11 15:08:12 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-timetable
Version:	20080911
Release:	10
Summary:	Generate timetables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/timetable/timetable.tex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timetable.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A highly-configurable package, with nice output and simple
input. The macros use a radix sort mechanism so that the order
of input is not critical.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/timetable/timetable.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080911-2
+ Revision: 756917
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080911-1
+ Revision: 719750
- texlive-timetable
- texlive-timetable
- texlive-timetable

