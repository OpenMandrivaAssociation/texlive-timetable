Name:		texlive-timetable
Version:	15878
Release:	2
Summary:	Generate timetables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/timetable/timetable.tex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/timetable.r%{version}.tar.xz
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
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
