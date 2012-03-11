%define version 0.10.23

%define release %mkrel 1
#gw for gsettings:
%define         _glib2          2.25
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
%define name %bname-plugins-bad
%define gst_required_version 0.10.33

%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%define build_experimental 0
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_amrwb 0
%define build_faac 0
%define build_faad 0
%define build_xvid 0
%define build_dts 0
%define build_dirac 1
%define build_gme 1
%define build_celt 1
%if %build_plf
%define distsuffix plf
%if %mdvver >= 201100
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%endif
%define build_amrwb 1
%define build_faac 1
%define build_faad 1
%define build_xvid 1
%define build_dts 1
%endif

%define libmajor 23
%define libnamephoto %mklibname gstphotography %major %libmajor
%define develnamephoto %mklibname -d gstphotography
%define libnamevdp %mklibname gstvdp %major %libmajor
%define libnamebase %mklibname gstbasevideo %major %libmajor
%define develnamebase %mklibname -d gstbasevideo

Summary: 	GStreamer Streaming-media framework plug-ins
Name: 		%name
Version: 	%version
Release: 	%release%{?extrarelsuffix}
License: 	LGPLv2+ and GPLv2+
Group: 		Sound
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
Patch0: gst-plugins-bad-0.10.7-wildmidi-timidity.cfg.patch
# gw: fix for bug #36437 (paths to realplayer codecs)
# prefer codecs from the RealPlayer package in restricted
Patch10: gst-plugins-bad-0.10.6-real-codecs-path.patch
URL:            http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 
#gw for the pixbuf plugin
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(glib-2.0) >= %_glib2 
BuildRequires: pkgconfig(libpng) >= 1.2.4-4mdk
BuildRequires: pkgconfig(libmodplug) >= 0.4.5
BuildRequires: pkgconfig(sdl)
BuildRequires: bzip2-devel
BuildRequires: pkgconfig(libmodplug)
BuildRequires: pkgconfig(libmusicbrainz)
BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(libssl)
%ifarch %ix86
BuildRequires: nasm => 0.90
%endif
BuildRequires: valgrind libcheck-devel
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10) >= %gst_required_version
BuildRequires: pkgconfig(libcdaudio)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(libmimic)
BuildRequires: pkgconfig(libass)
#gw for checks
BuildRequires: gstreamer0.10-plugins-base
BuildRequires: gstreamer0.10-plugins-good
BuildRequires: gstreamer0.10-tools
BuildRequires: fonts-ttf-dejavu
#gw for autoreconf
BuildRequires: gettext-devel
Provides:	%bname-audiosrc
Provides:	%bname-audiosink
Obsoletes:	gstreamer0.10-fluendo-mpegdemux <= 0.10.15
Provides:	gstreamer0.10-fluendo-mpegdemux
Conflicts: %bname-farsight <= 1:0.12.10
Requires:	%bname-voip >= %{version}-%{release}

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %build_plf
This package is in PLF as it violates some patents.
%endif


%package -n %libnamephoto
Summary: Libraries for GStreamer streaming-media framework
Group: System/Libraries

%description -n %libnamephoto
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %libnamevdp
Summary: Libraries for GStreamer streaming-media framework
Group: System/Libraries

%description -n %libnamevdp
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %develnamephoto
Summary: Libraries and include files for GStreamer streaming-media framework
Group: Development/C
Requires: %{libnamephoto} = %{version}
Requires: %{libnamevdp} = %{version}
Provides: libgstphotography-devel = %version-%release

%description -n %develnamephoto
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n %libnamebase
Summary: Libraries for GStreamer streaming-media framework
Group: System/Libraries

%description -n %libnamebase
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %develnamebase
Summary: Libraries and include files for GStreamer streaming-media framework
Group: Development/C
Requires: %{libnamebase} = %{version}
Provides: libgstbasevideo-devel = %version-%release

%description -n %develnamebase
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n %bname-curl
Summary: GStreamer Curl plugin
Group: Networking/Other
BuildRequires: libcurl-devel
%description -n %bname-curl
This is a HTTP plugin for GStreamer based on the curl library.

%files -n %bname-curl
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstcurl.so

%package -n %bname-dc1394
Summary: GStreamer DC1394 plugin
Group: System/Libraries
BuildRequires: libdc1394-devel

%description -n %bname-dc1394
This is a IEEE 1394 (Firewire) support plugin for GStreamer.

%files -n %bname-dc1394
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstdc1394.so

%package -n %bname-ofa
Summary: GStreamer OFA plugin
Group: Sound
BuildRequires: libofa-devel
%description -n %bname-ofa
This is a metadata support plugin for GStreamer based on the Open
Fingerprint Architecture library.

%files -n %bname-ofa
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstofa.so

%package -n %bname-opencv
Summary: GStreamer opencv plugin
Group: Video
BuildRequires: opencv-devel
%description -n %bname-opencv
This adds support for OpenCV (Open Source Computer Vision) to GStreamer.

%files -n %bname-opencv
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstopencv.so

%package -n %bname-teletext
Summary: GStreamer teletext decoder plugin
Group: Video
BuildRequires: zvbi-devel
%description -n %bname-teletext
This adds support for teletext decoding based on zvbi.

%files -n %bname-teletext
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstteletextdec.so

%package -n %bname-wildmidi
Summary: GStreamer wildmidi plugin
Group: Sound
BuildRequires: wildmidi-devel
Requires: timidity-instruments

%description -n %bname-wildmidi
This is a MIDI plugin for GStreamer based on the wildmidi library.

%files -n %bname-wildmidi
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstwildmidi.so

%package -n %bname-mpeg2enc
Summary:       GStreamer mjpegtools plug-in
Group:         Video
BuildRequires: libmjpegtools-devel

%description -n %bname-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %bname-mpeg2enc
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%_libdir/gstreamer-%majorminor/libgstmplex.so

%if %build_gme
%package -n %bname-gme
Summary:       GStreamer Game Music plug-in
Group:         Sound
BuildRequires: libgme-devel

%description -n %bname-gme
Game Music decoding plug-in.

%files -n %bname-gme
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%endif


%if %build_dirac
%package -n %bname-dirac
Summary:       GStreamer dirac plug-in
Group:         Video
BuildRequires: libdirac-devel >= 0.9

%description -n %bname-dirac
Dirac encoding and decoding plug-in.

%files -n %bname-dirac
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdirac.so
%endif

%package -n %bname-schroedinger
Summary:       GStreamer dirac plug-in based on Schroedinger
Group:         Video
BuildRequires: libschroedinger-devel
Epoch: 1

%description -n %bname-schroedinger
Dirac encoding and decoding plug-in based on Schroedinger.

%files -n %bname-schroedinger
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstschro.so

%package -n %bname-vp8
Summary:       GStreamer VP8 plug-in
Group:         Video
BuildRequires: libvpx-devel

%description -n %bname-vp8
VP8 encoding and decoding plug-in.

%files -n %bname-vp8
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstvp8.so
%_libdir/gstreamer-%majorminor/libgstrtpvp8.so


### LADSPA ###
%package -n %bname-ladspa
Summary: Gstreamer wrapper for LADSPA plug-ins
Group: Sound
Requires:      ladspa
BuildRequires: ladspa-devel

%description -n %bname-ladspa
Plug-in which wraps LADSPA plug-ins for use by GStreamer applications.
We suggest you also get the cmt package of ladspa plug-ins
and steve harris's swh-plugins package.

%files -n %bname-ladspa
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so

%if %build_dts
%package -n %bname-dts
Summary:GStreamer plug-ins for DTS audio playback
Group:         Sound
BuildRequires: dtsdec-devel

%description -n %bname-dts
Plug-ins for decoding DTS audio.

%files -n %bname-dts
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%endif

%if %build_xvid
%package -n %bname-xvid
Summary:GStreamer plug-ins for XVID video encoding and decoding
Group:         Video
BuildRequires: xvid-devel >= 1.1
 
%description -n %bname-xvid
Plug-ins for encoding and decoding XVID video.
 
This package is in PLF as it violates some patents.
%files -n %bname-xvid
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstxvid.so
%endif

%package -n %bname-musepack
Summary:GStreamer plug-in Musepack playback
Group:         Sound
BuildRequires: libmpcdec-devel
 
%description -n %bname-musepack
This plugin for GStreamer can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes mpc, mp+ or mpp.

%files -n %bname-musepack
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstmusepack.so

%package -n %bname-mms
Summary:       GStreamer plug-in for mms streams
Group:         System/Libraries
Requires:      %bname-plugins = %{version}
BuildRequires: libmms-devel

%description -n %bname-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %bname-mms
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so

%package -n %bname-rtmp
Summary:       GStreamer plug-in for rtmp streams
Group:         System/Libraries
Requires:      %bname-plugins = %{version}
BuildRequires: librtmp-devel

%description -n %bname-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %bname-rtmp
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp.so

%package -n %bname-directfb
Summary:       GStreamer plug-in for DirectFB output
Group: Video
Requires:      %bname-plugins = %{version}
BuildRequires: libdirectfb-devel

%description -n %bname-directfb
Plug-in supporting the video output to DirectFB.

%files -n %bname-directfb
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdfbvideosink.so

%package -n %bname-soundtouch
Summary:       GStreamer plug-in for SoundTouch support
Group: Sound
Requires:      %bname-plugins = %{version}
BuildRequires: libsoundtouch-devel

%description -n %bname-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %bname-soundtouch
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstsoundtouch.so

%package -n %bname-kate
Summary: GStreamer Karaoke and text plugin
Group: Video
BuildRequires: libtiger-devel >= 0.3.2

%description -n %bname-kate
This is a Karaoke and text plugin for GStreamer based on libkate and libtiger.

%files -n %bname-kate
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstkate.so

%package -n %bname-libass
Summary: GStreamer subtitles plugin
Group: Video
BuildRequires: libass-devel

%description -n %bname-libass
This is a subtitle plugin for GStreamer based on libass.

%files -n %bname-libass
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstassrender.so

%package -n %bname-resindvd
Summary: GStreamer DVD menu plugin
Group: Video
BuildRequires: libdvdnav-devel

%description -n %bname-resindvd
This is a DVD playback plugin for GStreamer with menu support.

%files -n %bname-resindvd
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libresindvd.so

%package -n %bname-voip
Summary: GStreamer voip plugins
Group: Sound
Conflicts: gstreamer0.10-plugins-bad < 0.10.14-3mdv
 
%description -n %bname-voip
This is a collection of VoIP plugins for GStreamer.

%files -n %bname-voip
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstrtpmux.so
%_libdir/gstreamer-%majorminor/libgstliveadder.so
%_libdir/gstreamer-%majorminor/libgstdtmf.so

%package -n %bname-cog
Summary: GStreamer COG plugin
Group: Video
BuildRequires: liborc-devel
 
%description -n %bname-cog
This is a signal processing plugin for GStreamer based on Orc.

%files -n %bname-cog
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstcog.so

%package doc
Group: Books/Computer books
Summary: GStreamer application library

%description doc
This is the documentation of %name.


%prep
%setup -q -n gst-plugins-bad-%{version}
%apply_patches
#gw broken configure in 0.10.19.2
#autoreconf -fi

%build
#work around broken mjpegtools headers including config.h:
export CPPFLAGS="-I."
%configure2_5x --disable-dependency-tracking \
%if %build_plf
  --with-package-name='PLF %name package' \
  --with-package-origin='http://plf.zarb.org/' \
%else
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \
%endif
%if ! %build_celt
	--disable-celt \
%endif
%if ! %build_faac
	--disable-faac \
%endif
%if ! %build_faad
	--disable-faad \
%endif
%if ! %build_dirac
        --disable-dirac \
%endif
%if %build_experimental
	--enable-experimental
%endif

make

%check
cd tests/check
make check

%install
rm -rf %buildroot gst-plugins-base-%majorminor.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang gst-plugins-bad-%majorminor
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libnamephoto -p /sbin/ldconfig
%postun -n %libnamephoto -p /sbin/ldconfig
%post -n %libnamebase -p /sbin/ldconfig
%postun -n %libnamebase -p /sbin/ldconfig
%endif

%files doc
%defattr(-, root, root)
%doc docs/plugins/html

%files -f gst-plugins-bad-%majorminor.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS 
%_datadir/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml
%_libdir/gstreamer-%majorminor/libgstadpcmdec.so
%_libdir/gstreamer-%majorminor/libgstadpcmenc.so
%_libdir/gstreamer-%majorminor/libgstaiff.so
%_libdir/gstreamer-%majorminor/libgstapexsink.so
%_libdir/gstreamer-%majorminor/libgstasfmux.so
%_libdir/gstreamer-%majorminor/libgstaudiovisualizers.so
%_libdir/gstreamer-%majorminor/libgstautoconvert.so
%_libdir/gstreamer-%majorminor/libgstbayer.so
%_libdir/gstreamer-%majorminor/libgstcamerabin.so
%_libdir/gstreamer-%majorminor/libgstcamerabin2.so
%_libdir/gstreamer-%majorminor/libgstcoloreffects.so
%_libdir/gstreamer-%majorminor/libgstcolorspace.so
%_libdir/gstreamer-%majorminor/libgstdccp.so
%_libdir/gstreamer-%majorminor/libgstdataurisrc.so
%_libdir/gstreamer-%majorminor/libgstdebugutilsbad.so
%_libdir/gstreamer-%majorminor/libgstdvb.so
%_libdir/gstreamer-%majorminor/libgstdvbsuboverlay.so
%_libdir/gstreamer-%majorminor/libgstdvdspu.so
%_libdir/gstreamer-%majorminor/libgstfaceoverlay.so
%_libdir/gstreamer-%majorminor/libgstfbdevsink.so
%_libdir/gstreamer-%majorminor/libgstfestival.so
%_libdir/gstreamer-%majorminor/libgstfrei0r.so
%_libdir/gstreamer-%majorminor/libgstfreeverb.so
%_libdir/gstreamer-%majorminor/libgstgaudieffects.so
%_libdir/gstreamer-%majorminor/libgstgeometrictransform.so
%_libdir/gstreamer-%majorminor/libgstgsettingselements.so
%_libdir/gstreamer-%majorminor/libgsthdvparse.so
%_libdir/gstreamer-%majorminor/libgstid3tag.so
%_libdir/gstreamer-%majorminor/libgstinterlace.so
%_libdir/gstreamer-%majorminor/libgstinter.so
%_libdir/gstreamer-%majorminor/libgstivfparse.so
%_libdir/gstreamer-%majorminor/libgstjpegformat.so
%_libdir/gstreamer-%majorminor/libgstlegacyresample.so
%_libdir/gstreamer-%majorminor/libgstmpegdemux.so
%_libdir/gstreamer-%majorminor/libgstmpegpsmux.so
%_libdir/gstreamer-%majorminor/libgstmpegtsmux.so
%_libdir/gstreamer-%majorminor/libgstmpegvideoparse.so
%_libdir/gstreamer-%majorminor/libgstmve.so
%_libdir/gstreamer-%majorminor/libgstmimic.so
%_libdir/gstreamer-%majorminor/libgstmxf.so
%_libdir/gstreamer-%majorminor/libgstpcapparse.so
%_libdir/gstreamer-%majorminor/libgstpnm.so
%_libdir/gstreamer-%majorminor/libgstremovesilence.so
%_libdir/gstreamer-%majorminor/libgstsmooth.so
%_libdir/gstreamer-%majorminor/libgstscaletempoplugin.so
%_libdir/gstreamer-%majorminor/libgstrawparse.so
%_libdir/gstreamer-%majorminor/libgstreal.so
%_libdir/gstreamer-%majorminor/libgstsdpelem.so
%_libdir/gstreamer-%majorminor/libgstsegmentclip.so
%_libdir/gstreamer-%majorminor/libgstshm.so
%_libdir/gstreamer-%majorminor/libgstsiren.so
%_libdir/gstreamer-%majorminor/libgstsndfile.so
%_libdir/gstreamer-%majorminor/libgststereo.so
%_libdir/gstreamer-%majorminor/libgstsubenc.so
%_libdir/gstreamer-%majorminor/libgstvcdsrc.so
%_libdir/gstreamer-%majorminor/libgstvideomaxrate.so
%_libdir/gstreamer-%majorminor/libgstvideomeasure.so
%_libdir/gstreamer-%majorminor/libgstvideosignal.so
%_libdir/gstreamer-%majorminor/libgstvmnc.so
%_libdir/gstreamer-%majorminor/libgstbz2.so
%_libdir/gstreamer-%majorminor/libgstcdaudio.so
%_libdir/gstreamer-%majorminor/libgstcdxaparse.so
%_libdir/gstreamer-%majorminor/libgstdecklink.so
%_libdir/gstreamer-%majorminor/libgstfieldanalysis.so
%_libdir/gstreamer-%majorminor/libgstfragmented.so
%_libdir/gstreamer-%majorminor/libgstlinsys.so
%_libdir/gstreamer-%majorminor/libgstmpegtsdemux.so
%_libdir/gstreamer-%majorminor/libgstpatchdetect.so
%_libdir/gstreamer-%majorminor/libgstsdi.so
%_libdir/gstreamer-%majorminor/libgstvideofiltersbad.so
%_libdir/gstreamer-%majorminor/libgstvideoparsersbad.so
%if %build_experimental
#%_libdir/gstreamer-%majorminor/libgstdeinterlace2.so
%endif
%_libdir/gstreamer-%majorminor/libgstfreeze.so
%_libdir/gstreamer-%majorminor/libgsth264parse.so
%_libdir/gstreamer-%majorminor/libgstmodplug.so
%_libdir/gstreamer-%majorminor/libgstnsf.so
%_libdir/gstreamer-%majorminor/libgstnuvdemux.so
%_libdir/gstreamer-%majorminor/libgstrfbsrc.so
%_libdir/gstreamer-%majorminor/libgstsdl.so
%_libdir/gstreamer-%majorminor/libgstspeed.so
%_libdir/gstreamer-%majorminor/libgsttrm.so
%_libdir/gstreamer-%majorminor/libgsttta.so
%_libdir/gstreamer-%majorminor/libgsty4mdec.so

#%package examples
#Summary:GStreamer example applications
#Group: Video

#%description examples
#This contains example applications to test %{name}

#%files examples
#%defattr(-, root, root)

%package -n %bname-vdpau
Summary:GStreamer plug-in for playback using VDPAU
Group: Video
BuildRequires: vdpau-devel

%description -n %bname-vdpau
This plug-in adds video playback support to GStreamer based on VDPAU 
(Video Decode and Presentation API for Unix).

%files -n %bname-vdpau
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstvdpau.so

%if %build_faad
%package -n %bname-faad
Summary:GStreamer plug-in for AAC audio playback
Group:         Sound
Requires: %bname-plugins >= %version
BuildRequires: libfaad2-devel => 2.0
 
%description -n %bname-faad
Plug-ins for playing AAC audio
 
This package is in PLF as it violates some patents.
%files -n %bname-faad
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstfaad.so
%endif

%if %build_faac
%package -n %bname-faac
Summary:GStreamer plug-ins for AAC audio encoding
Group:         Sound
Requires: %bname-plugins >= %version
BuildRequires: libfaac-devel
 
%description -n %bname-faac
Plug-ins for encoding AAC audio
 
This package is in PLF as it violates some patents.
%files -n %bname-faac
%defattr(-, root, root)
%_libdir/gstreamer-%{majorminor}/libgstfaac.so
%endif

%package -n %bname-gsm
Summary: GStreamer plugin for GSM lossy audio format
Group: Sound
Requires: %bname-plugins >= %{version}
BuildRequires: gsm-devel >= 1.0.10

%description -n %bname-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%files -n %bname-gsm
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so

%if 0
### SWFDEC FLASH PLUGIN ###
%package -n %bname-swfdec
Summary:  GStreamer Flash rendering plug-in
Group:    System/Libraries
Requires: %bname-plugins = %{version}
BuildRequires: libswfdec-devel => 0.3.0

%description -n %bname-swfdec
Plug-in for rendering Flash animations using swfdec library

%files -n %bname-swfdec
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstswfdec.so
%endif

%package -n %bname-neon
Summary:  GStreamer HTTP plugin based on libneon
Group:    System/Libraries
Requires: %bname-plugins = %{version}
BuildRequires: neon-devel

%description -n %bname-neon
Plug-in for HTTP access based on libneon.

%files -n %bname-neon
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so

%package -n %bname-nas
Summary:  Gstreamer output plugin for the NAS sound server
Group:    Sound
Requires: %bname-plugins = %{version}
BuildRequires: libnas-devel

%description -n %bname-nas
Output plugin for GStreamer for use with the nas sound server.

%files -n %bname-nas
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstnassink.so

%if %build_amrwb
%package -n %bname-amrwb
Summary: GStreamer plug-in for AMR-WB support
Group:  Sound
Requires: %bname-plugins >= %{version}
BuildRequires: libamrwb-devel

%description -n %bname-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in PLF as it violates some patents.
%files -n %bname-amrwb
%defattr(-, root, root)
%_datadir/gstreamer-%majorminor/presets/GstAmrwbEnc.prs
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbenc.so
%endif


%package -n %bname-jp2k
Summary: GStreamer plug-in for JPEG2000 support
Group:  Graphics
Requires: %bname-plugins >= %{version}
BuildRequires: libjasper-devel

%description -n %bname-jp2k
Plug-in for JPEG2000 support under GStreamer.

%files -n %bname-jp2k
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstjp2k.so
%_libdir/gstreamer-%majorminor/libgstjp2kdecimator.so

%if %build_celt
%package -n %bname-celt
Summary: GStreamer plug-in for CELT support
Group:  Video
Requires: %bname-plugins >= %{version}
BuildRequires: celt-devel >= 0.7.0

%description -n %bname-celt
Plug-in for CELT support under GStreamer.

%files -n %bname-celt
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstcelt.so
%endif


%package -n %bname-rsvg
Summary: GStreamer plug-in for SVG support
Group:  Graphics
Requires: %bname-plugins >= %{version}
BuildRequires: librsvg-devel

%description -n %bname-rsvg
Plug-in for SVG support under GStreamer.

%files -n %bname-rsvg
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstrsvg.so

%files -n %libnamephoto
%defattr(-, root, root)
%{_libdir}/libgstbasecamerabinsrc-%majorminor.so.%{libmajor}*
%{_libdir}/libgstcodecparsers-%majorminor.so.%{libmajor}*
%{_libdir}/libgstphotography-%majorminor.so.%{libmajor}*
%{_libdir}/libgstsignalprocessor-%majorminor.so.%{libmajor}*

%files -n %libnamevdp
%defattr(-, root, root)
%{_libdir}/libgstvdp-%majorminor.so.%{libmajor}*

%files -n %develnamephoto
%defattr(-, root, root)
%{_libdir}/libgstbasecamerabinsrc-%majorminor.so
%{_libdir}/libgstcodecparsers-%majorminor.so
%{_libdir}/libgstphotography-%majorminor.so
%{_libdir}/libgstsignalprocessor-%majorminor.so
%{_libdir}/libgstvdp-%majorminor.so
%_includedir/gstreamer-0.10/gst/basecamerabinsrc
%_includedir/gstreamer-0.10/gst/codecparsers
%_includedir/gstreamer-0.10/gst/interfaces/photography*
%_includedir/gstreamer-0.10/gst/signalprocessor/gstsignalprocessor.h
%_includedir/gstreamer-0.10/gst/vdpau/
%_libdir/pkgconfig/gstreamer-codecparsers-%majorminor.pc
%_libdir/pkgconfig/gstreamer-plugins-bad-%majorminor.pc
%_datadir/gtk-doc/html/gst-plugins-bad-libs-%majorminor

%files -n %libnamebase
%defattr(-, root, root)
%{_libdir}/libgstbasevideo-%majorminor.so.%{libmajor}*

%files -n %develnamebase
%defattr(-, root, root)
%{_libdir}/libgstbasevideo-%majorminor.so
%_includedir/gstreamer-0.10/gst/video/*
%_libdir/pkgconfig/gstreamer-basevideo-%majorminor.pc

