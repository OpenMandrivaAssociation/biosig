%define major 3
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	I/O library for biomedical data
Name:		biosig
Version:	2.6.1
Release:	1
License:	GPLv3+
Group:		Sciences/Biology
URL:		https://biosig.sourceforge.io/
Source0:	https://downloads.sourceforge.net/biosig/%{name}-%{version}.src.tar.xz
BuildRequires:	libb64-devel
BuildRequires:	dcmtk-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	pkgconfig(tinyxml)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	suitesparse-devel

%description
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as the
electroencephalogram (EEG), electrocorticogram (ECoG), electrocardiogram
(ECG), electrooculogram (EOG), electromyogram (EMG), respiration, and so on.
Major application areas are: Neuroinformatics, brain-computer interfaces,
neurophysiology, psychology, cardiovascular systems and sleep research.
The aim of the BioSig project is to foster research in biomedical signal
processing by providing open source software tools for many different
applications. Generally, many concerns have to be addressed in this scientific
field. BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

%files
%{_bindir}/*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	I/O library for biomedical data
Group:		System/Libraries

%description -n %{libname}
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as the
electroencephalogram (EEG), electrocorticogram (ECoG), electrocardiogram
(ECG), electrooculogram (EOG), electromyogram (EMG), respiration, and so on.
Major application areas are: Neuroinformatics, brain-computer interfaces,
neurophysiology, psychology, cardiovascular systems and sleep research.
The aim of the BioSig project is to foster research in biomedical signal
processing by providing open source software tools for many different
applications. Generally, many concerns have to be addressed in this scientific
field. BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

%files -n %{libname}
%license COPYING
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	I/O library for biomedical data
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Headers and development files for %{name}.

%files -n %{devname}
%license COPYING
%doc CITATION README RELEASE-NOTES
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_mandir}/man1/*.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# remove static
rm -fr %{buildroot}%{_libdir}/lib*.a

# remove octave
rm -fr %{buildroot}%{_libdir}/octave
rm -fr %{buildroot}%{_datadir}/octave
rm -fr %{buildroot}%{_datadir}/%{name}/matlab

