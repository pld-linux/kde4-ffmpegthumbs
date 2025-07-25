%define		_state		stable
%define		orgname		ffmpegthumbs
%define		qtver		4.8.1

Summary:	Video thumbnail generator for KDE
Summary(pl.UTF-8):	Generator podglądów video dla KDE
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	4
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7a352e87112306df5a7edcd6bba37b67
Patch0:		ffmpeg3.patch
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdebase >= %{version}
Requires:	ffmpeg >= 0.8
Obsoletes:	kde4-kdemultimedia-ffmpegthumbs < 4.8.99-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FFMpegThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...) , now available also for KDE 4.

%prep
%setup -q -n %{orgname}-%{version}
%patch -P0 -p1

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/ffmpegthumbs.so
%{_datadir}/kde4/services/ffmpegthumbs.desktop
