#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cscope
Version  : 15.8b
Release  : 3
URL      : http://downloads.sourceforge.net/cscope/cscope-15.8b.tar.gz
Source0  : http://downloads.sourceforge.net/cscope/cscope-15.8b.tar.gz
Summary  : cscope is an interactive, screen-oriented tool that allows the user to browse through C source files for specified elements of code.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: cscope-bin
Requires: cscope-doc
BuildRequires : bison
BuildRequires : flex
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(ncurses)

%description
cscope is an interactive, screen-oriented tool that allows the user to browse through C source files for specified elements of code.

%package bin
Summary: bin components for the cscope package.
Group: Binaries

%description bin
bin components for the cscope package.


%package doc
Summary: doc components for the cscope package.
Group: Documentation

%description doc
doc components for the cscope package.


%prep
%setup -q -n cscope-15.8b

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cscope
/usr/bin/ocs

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
