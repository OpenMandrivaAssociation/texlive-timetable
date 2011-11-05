# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/timetable/timetable.tex
# catalog-date 2008-09-11 15:08:12 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-timetable
Version:	20080911
Release:	1
Summary:	Generate timetables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/timetable/timetable.tex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timetable.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
A highly-configurable package, with nice output and simple
input. The macros use a radix sort mechanism so that the order
of input is not critical.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/timetable/timetable.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
