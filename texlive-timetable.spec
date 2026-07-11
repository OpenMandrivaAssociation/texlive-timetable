%global tl_name timetable
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Generate timetables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/timetable
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/timetable.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A highly-configurable package, with nice output and simple input. The
macros use a radix sort mechanism so that the order of input is not
critical.

