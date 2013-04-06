#gw for gsettings:
%define _glib2 2.25
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10

%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%define build_experimental 0
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_amrwb 0
%define build_voaac 0
%define build_faac 0
%define build_faad 0
%define build_xvid 0
%define build_dts 0
%define build_dirac 1
%define build_gme 1
%define build_celt 1

###############################
# Hardcore PLF build
%define build_plf 0
###############################

%if %{build_plf}
%define distsuffix plf
%define extrarelsuffix plf
%define build_amrwb 1
%define build_voaac 1
%define build_faac 1
%define build_faad 1
%define build_xvid 1
%define build_dts 1
%endif

%define libmajor 23
%define libnamephoto %mklibname gstphotography %{major} %{libmajor}
%define develnamephoto %mklibname -d gstphotography
%define libnamevdp %mklibname gstvdp %{major} %{libmajor}
%define libnamebase %mklibname gstbasevideo %{major} %{libmajor}
%define develnamebase %mklibname -d gstbasevideo

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-bad
Version:	0.10.23
Release:	4%{?extrarelsuffix}
License:	LGPLv2+ and GPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.bz2
Patch0:		gst-plugins-bad-0.10.7-wildmidi-timidity.cfg.patch
Patch1:		gst-plugins-bad-0.10.23-h264.patch
# With new directfb we get macro expanded to
#  __attribute__((__attribute__((no_instrument_function))))
# See http://permalink.gmane.org/gmane.comp.graphics.directfb.devel/3679
Patch2:		gst-plugins-bad-0.10.23-attribute.patch
# gw: fix for bug #36437 (paths to realplayer codecs)
# prefer codecs from the RealPlayer package in restricted
Patch10:	gst-plugins-bad-0.10.6-real-codecs-path.patch
#gw for the pixbuf plugin
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(openssl)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	valgrind
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10) >= 0.10.33
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libmimic)
BuildRequires:	pkgconfig(libass)
#gw for checks
BuildRequires:	gstreamer0.10-plugins-good
BuildRequires:	fonts-ttf-dejavu
#gw for autoreconf
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(opus)
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink
Obsoletes:	gstreamer0.10-fluendo-mpegdemux <= 0.10.15
Provides:	gstreamer0.10-fluendo-mpegdemux
Conflicts:	%{bname}-farsight <= 1:0.12.10
Requires:	%{bname}-voip >= %{version}-%{release}

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

%if %{build_plf}
This package is in restricted as it violates some patents.
%endif

%package -n %{libnamephoto}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libnamephoto}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%files -n %{libnamephoto}
%{_libdir}/libgstcodecparsers-%{majorminor}.so.%{libmajor}*
%{_libdir}/libgstphotography-%{majorminor}.so.%{libmajor}*
%{_libdir}/libgstsignalprocessor-%{majorminor}.so.%{libmajor}*

%package -n %{libnamevdp}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libnamevdp}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%files -n %{libnamevdp}
%{_libdir}/libgstvdp-%{majorminor}.so.%{libmajor}*

%package -n %{develnamephoto}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libnamephoto} = %{version}
Requires:	%{libnamevdp} = %{version}
Provides:	libgstphotography-devel = %{version}-%{release}

%description -n %{develnamephoto}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%files -n %{develnamephoto}
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgstsignalprocessor-%{majorminor}.so
%{_libdir}/libgstvdp-%{majorminor}.so
%{_includedir}/gstreamer-0.10/gst/codecparsers
%{_includedir}/gstreamer-0.10/gst/interfaces/photography*
%{_includedir}/gstreamer-0.10/gst/signalprocessor/gstsignalprocessor.h
%{_includedir}/gstreamer-0.10/gst/vdpau/
%{_includedir}/gstreamer-0.10/gst/video/
%exclude %{_includedir}/gstreamer-0.10/gst/video/gstbasevideo*
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc

%package -n %{libnamebase}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libnamebase}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%files -n %{libnamebase}
%{_libdir}/libgstbasevideo-%{majorminor}.so.%{libmajor}*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.%{libmajor}*

%package -n %{develnamebase}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libnamebase} = %{version}
Provides:	libgstbasevideo-devel = %{version}-%{release}

%description -n %{develnamebase}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%files -n %{develnamebase}
%{_libdir}/libgstbasevideo-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideo*
%{_includedir}/gstreamer-0.10/gst/basecamerabinsrc/*.h
%{_libdir}/pkgconfig/gstreamer-basevideo-%{majorminor}.pc

%package -n %{bname}-curl
Summary:	GStreamer Curl plugin
Group:		Networking/Other
BuildRequires:	pkgconfig(libcurl)

%description -n %{bname}-curl
This is a HTTP plugin for GStreamer based on the curl library.

%files -n %{bname}-curl
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so

%package -n %{bname}-dc1394
Summary:	GStreamer DC1394 plugin
Group:		System/Libraries
BuildRequires:	pkgconfig(libdc1394-2)

%description -n %{bname}-dc1394
This is a IEEE 1394 (Firewire) support plugin for GStreamer.

%files -n %{bname}-dc1394
%{_libdir}/gstreamer-%{majorminor}/libgstdc1394.so

%package -n %{bname}-ofa
Summary:	GStreamer OFA plugin
Group:		Sound
BuildRequires:	pkgconfig(libofa)

%description -n %{bname}-ofa
This is a metadata support plugin for GStreamer based on the Open
Fingerprint Architecture library.

%files -n %{bname}-ofa
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so

%package -n %{bname}-wildmidi
Summary:	GStreamer wildmidi plugin
Group:		Sound
BuildRequires:	wildmidi-devel
Requires:	timidity-instruments

%description -n %{bname}-wildmidi
This is a MIDI plugin for GStreamer based on the wildmidi library.

%files -n %{bname}-wildmidi
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so

%package -n %{bname}-mpeg2enc
Summary:	GStreamer mjpegtools plug-in
Group:		Video
BuildRequires:	pkgconfig(mjpegtools)

%description -n %{bname}-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %{bname}-mpeg2enc
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{majorminor}/libgstmplex.so

%if %{build_gme}
%package -n %{bname}-gme
Summary:	GStreamer Game Music plug-in
Group:		Sound
BuildRequires:	libgme-devel

%description -n %{bname}-gme
Game Music decoding plug-in.

%files -n %{bname}-gme
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%endif

%if %{build_dirac}
%package -n %{bname}-dirac
Summary:	GStreamer dirac plug-in
Group:		Video
BuildRequires:	pkgconfig(dirac)

%description -n %{bname}-dirac
Dirac encoding and decoding plug-in.

%files -n %{bname}-dirac
%{_libdir}/gstreamer-%{majorminor}/libgstdirac.so
%endif

%package -n %{bname}-schroedinger
Summary:	GStreamer dirac plug-in based on Schroedinger
Group:		Video
BuildRequires:	pkgconfig(schroedinger-1.0)
Epoch:		1

%description -n %{bname}-schroedinger
Dirac encoding and decoding plug-in based on Schroedinger.

%files -n %{bname}-schroedinger
%{_libdir}/gstreamer-%{majorminor}/libgstschro.so

%package -n %{bname}-vp8
Summary:	GStreamer VP8 plug-in
Group:		Video
BuildRequires:	pkgconfig(vpx)

%description -n %{bname}-vp8
VP8 encoding and decoding plug-in.

%files -n %{bname}-vp8
%{_libdir}/gstreamer-%{majorminor}/libgstvp8.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpvp8.so

### LADSPA ###
%package -n %{bname}-ladspa
Summary:	Gstreamer wrapper for LADSPA plug-ins
Group:		Sound
Requires:	ladspa
BuildRequires:	ladspa-devel

%description -n %{bname}-ladspa
Plug-in which wraps LADSPA plug-ins for use by GStreamer applications.
We suggest you also get the cmt package of ladspa plug-ins
and steve harris's swh-plugins package.

%files -n %{bname}-ladspa
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so

%if %{build_dts}
%package -n %{bname}-dts
Summary:	GStreamer plug-ins for DTS audio playback
Group:		Sound
BuildRequires:	dtsdec-devel

%description -n %{bname}-dts
Plug-ins for decoding DTS audio.

%files -n %{bname}-dts
%{_libdir}/gstreamer-%{majorminor}/libgstdtsdec.so
%endif

%if %{build_xvid}
%package -n %{bname}-xvid
Summary:	GStreamer plug-ins for XVID video encoding and decoding
Group:		Video
BuildRequires:	xvid-devel >= 1.1

%description -n %{bname}-xvid
Plug-ins for encoding and decoding XVID video.

This package is in restricted as it violates some patents.

%files -n %{bname}-xvid
%{_libdir}/gstreamer-%{majorminor}/libgstxvid.so
%endif

%package -n %{bname}-musepack
Summary:	GStreamer plug-in Musepack playback
Group:		Sound
BuildRequires:	libmpcdec-devel

%description -n %{bname}-musepack
This plugin for GStreamer can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes mpc, mp+ or mpp.

%files -n %{bname}-musepack
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so

%package -n %{bname}-mms
Summary:	GStreamer plug-in for mms streams
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libmms)

%description -n %{bname}-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %{bname}-mms
%{_libdir}/gstreamer-%{majorminor}/libgstmms.so

%package -n %{bname}-rtmp
Summary:	GStreamer plug-in for rtmp streams
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(librtmp)

%description -n %{bname}-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %{bname}-rtmp
%{_libdir}/gstreamer-%{majorminor}/libgstrtmp.so

%package -n %{bname}-directfb
Summary:	GStreamer plug-in for DirectFB output
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(directfb)

%description -n %{bname}-directfb
Plug-in supporting the video output to DirectFB.

%files -n %{bname}-directfb
%{_libdir}/gstreamer-%{majorminor}/libgstdfbvideosink.so

%package -n %{bname}-soundtouch
Summary:	GStreamer plug-in for SoundTouch support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(soundtouch)

%description -n %{bname}-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %{bname}-soundtouch
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so

%package -n %{bname}-kate
Summary:	GStreamer Karaoke and text plugin
Group:		Video
BuildRequires:	pkgconfig(tiger)

%description -n %{bname}-kate
This is a Karaoke and text plugin for GStreamer based on libkate and libtiger.

%files -n %{bname}-kate
%{_libdir}/gstreamer-%{majorminor}/libgstkate.so

%package -n %{bname}-libass
Summary:	GStreamer subtitles plugin
Group:		Video
BuildRequires:	pkgconfig(libass)

%description -n %{bname}-libass
This is a subtitle plugin for GStreamer based on libass.

%files -n %{bname}-libass
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so

%package -n %{bname}-resindvd
Summary:	GStreamer DVD menu plugin
Group:		Video
BuildRequires:	pkgconfig(dvdnav)

%description -n %{bname}-resindvd
This is a DVD playback plugin for GStreamer with menu support.

%files -n %{bname}-resindvd
%{_libdir}/gstreamer-%{majorminor}/libresindvd.so

%package -n %{bname}-voip
Summary:	GStreamer voip plugins
Group:		Sound

%description -n %{bname}-voip
This is a collection of VoIP plugins for GStreamer.

%files -n %{bname}-voip
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstliveadder.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtmf.so

%package -n %{bname}-cog
Summary:	GStreamer COG plugin
Group:		Video
BuildRequires:	pkgconfig(orc-0.4)

%description -n %{bname}-cog
This is a signal processing plugin for GStreamer based on Orc.

%files -n %{bname}-cog
%{_libdir}/gstreamer-%{majorminor}/libgstcog.so

%package -n %{bname}-vdpau
Summary:	GStreamer plug-in for playback using VDPAU
Group:		Video
BuildRequires:	vdpau-devel

%description -n %{bname}-vdpau
This plug-in adds video playback support to GStreamer based on VDPAU 
(Video Decode and Presentation API for Unix).

%files -n %{bname}-vdpau
%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so

%if %{build_faad}
%package -n %{bname}-faad
Summary:	GStreamer plug-in for AAC audio playback
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	libfaad2-devel => 2.0

%description -n %{bname}-faad
Plug-ins for playing AAC audio

This package is in restricted as it violates some patents.

%files -n %{bname}-faad
%{_libdir}/gstreamer-%{majorminor}/libgstfaad.so
%endif

%if %{build_faac}
%package -n %{bname}-faac
Summary:	GStreamer plug-ins for AAC audio encoding
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	libfaac-devel

%description -n %{bname}-faac
Plug-ins for encoding AAC audio

This package is in restricted as it violates some patents.

%files -n %{bname}-faac
%{_libdir}/gstreamer-%{majorminor}/libgstfaac.so
%endif

%package -n %{bname}-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	gsm-devel >= 1.0.10

%description -n %{bname}-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%files -n %{bname}-gsm
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so

%package -n %{bname}-neon
Summary:	GStreamer HTTP plugin based on libneon
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(neon)

%description -n %{bname}-neon
Plug-in for HTTP access based on libneon.

%files -n %{bname}-neon
%{_libdir}/gstreamer-%{majorminor}/libgstneonhttpsrc.so

%package -n %{bname}-nas
Summary:	Gstreamer output plugin for the NAS sound server
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	libnas-devel

%description -n %{bname}-nas
Output plugin for GStreamer for use with the nas sound server.

%files -n %{bname}-nas
%{_libdir}/gstreamer-%{majorminor}/libgstnassink.so

%if %{build_amrwb}
%package -n %{bname}-amrwb
Summary:	GStreamer plug-in for AMR-WB support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(vo-amrwbenc)

%description -n %{bname}-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in restricted as it violates some patents.

%files -n %{bname}-amrwb
%{_datadir}/gstreamer-%{majorminor}/presets/GstVoAmrwbEnc.prs
%{_libdir}/gstreamer-%{majorminor}/libgstvoamrwbenc.so
%endif

%if %{build_voaac}
%package -n %{bname}-vo-aac
Summary:	GStreamer plug-in for VisualOn AAC encoding
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(vo-aacenc)

%description -n %{bname}-vo-aac
Plug-in for encoding AAC under GStreamer based on VisualOn AAC library.

This package is in restricted as it violates some patents.

%files -n %{bname}-vo-aac
%{_libdir}/gstreamer-%{majorminor}/libgstvoaacenc.so
%endif

%package -n %{bname}-jp2k
Summary:	GStreamer plug-in for JPEG2000 support
Group:		Graphics
Requires:	%{bname}-plugins
BuildRequires:	jasper-devel

%description -n %{bname}-jp2k
Plug-in for JPEG2000 support under GStreamer.

%files -n %{bname}-jp2k
%{_libdir}/gstreamer-%{majorminor}/libgstjp2k.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so

%if %{build_celt}
%package -n %{bname}-celt
Summary:	GStreamer plug-in for CELT support
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	celt-devel >= 0.7.0

%description -n %{bname}-celt
Plug-in for CELT support under GStreamer.

%files -n %{bname}-celt
%{_libdir}/gstreamer-%{majorminor}/libgstcelt.so
%endif

%package -n %{bname}-rsvg
Summary:	GStreamer plug-in for SVG support
Group:		Graphics
Requires:	%{bname}-plugins
BuildRequires:	librsvg-devel

%description -n %{bname}-rsvg
Plug-in for SVG support under GStreamer.

%files -n %{bname}-rsvg
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so

%package doc
Group:		Books/Computer books
Summary:	GStreamer application library

%description doc
This is the documentation of %{name}.

%files doc
%doc docs/plugins/html
%{_datadir}/gtk-doc/html/*

%prep
%setup -q -n gst-plugins-bad-%{version}
%apply_patches
#gw broken configure in 0.10.19.2
#autoreconf -fi

%build
#work around broken mjpegtools headers including config.h:
export CPPFLAGS="-I."
%configure2_5x --disable-dependency-tracking \
  --with-package-name='%distribution %{name} package' \
  --with-package-origin='%{disturl}' \
%if ! %{build_celt}
	--disable-celt \
%endif
%if ! %{build_faac}
	--disable-faac \
%endif
%if ! %{build_faad}
	--disable-faad \
%endif
%if ! %{build_dirac}
	--disable-dirac \
%endif
%if %{build_experimental}
	--enable-experimental
%endif

%make

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang gst-plugins-bad-%{majorminor}

# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm %{buildroot}%{_libdir}/*.a

%files -f gst-plugins-bad-%{majorminor}.lang
%doc AUTHORS COPYING README NEWS
%{_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstapexsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstcolorspace.so
%{_libdir}/gstreamer-%{majorminor}/libgstdccp.so
%{_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdspu.so
%{_libdir}/gstreamer-%{majorminor}/libgstfaceoverlay.so
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsettingselements.so
%{_libdir}/gstreamer-%{majorminor}/libgsthdvparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstinter.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstlegacyresample.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegvideoparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmve.so
%{_libdir}/gstreamer-%{majorminor}/libgstmimic.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
# New version of opencv is not supported yet,
# uncomment when the plugin is built again
#{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopus.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstreal.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstscaletempoplugin.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstsiren.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomaxrate.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomeasure.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdxaparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstfragmented.so
%{_libdir}/gstreamer-%{majorminor}/libgstlinsys.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstpatchdetect.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdi.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeze.so
%{_libdir}/gstreamer-%{majorminor}/libgsth264parse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstnsf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnuvdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdl.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgsttrm.so
%{_libdir}/gstreamer-%{majorminor}/libgsttta.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so

%changelog
* Sat Jun 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.10.23-1
- New version 0.10.23
- New libmajor (0 -> 23)
- Upstream switched to vo-amrwbenc so add pkgconfig(vo-amrwbenc) to BuildRequires
- No longer requires libamrwb-devel to build
- Add subpackage vo-aac
- New plugin libgstaudiovisualizers.so
- New plugin libgstcamerabin2.so
- New plugin libgstfaceoverlay.so
- New plugin libgstfreeverb.so
- New plugin libgstinter.so
- New plugin libgstopenal.so
- New plugin libgstopencv.so
- New plugin libgstremovesilence.so
- New plugin libgstsmooth.so
- Update file list
- Update BuildRequires (add expat-devel)
- Disable checks

* Tue May 24 2011 Götz Waschk <waschk@mandriva.org> 0.10.22-4mdv2011.0
+ Revision: 678168
- fix build with new mjpegtools

* Wed May 11 2011 Götz Waschk <waschk@mandriva.org> 0.10.22-3
+ Revision: 673538
- add curl plugin

* Wed May 11 2011 Funda Wang <fwang@mandriva.org> 0.10.22-1
+ Revision: 673434
- update file list
- update file list
- new version 0.10.22

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.10.21-3
+ Revision: 640439
- rebuild to obsolete old packages

* Mon Feb 21 2011 Götz Waschk <waschk@mandriva.org> 0.10.21-2
+ Revision: 639085
- rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - plf: append "plf" to Release on cooker to make plf build have higher EVR
      again with the rpm5-style mkrel now in use

* Sat Jan 22 2011 Götz Waschk <waschk@mandriva.org> 0.10.21-1
+ Revision: 632338
- new version
- disable experimental elements
- remove jack, metadata, valve, selector
- bump gstreamer dep
- add colorspace, interlace, y4mdec, jp2kdecimator

* Fri Dec 17 2010 Funda Wang <fwang@mandriva.org> 0.10.20-4mdv2011.0
+ Revision: 622485
- rebuild for new directfb

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.10.20-3mdv2011.0
+ Revision: 593561
- rebuild for gstreamer provides

* Mon Sep 06 2010 Götz Waschk <waschk@mandriva.org> 0.10.20-2mdv2011.0
+ Revision: 576215
- rebuild for lost packages in i586 repo

* Fri Sep 03 2010 Götz Waschk <waschk@mandriva.org> 0.10.20-1mdv2011.0
+ Revision: 575673
- new version
- bump glib dep for gsettings
- drop patches 1,2,3,4,5
- depend on orc instead of liboil
- add gsettings support
- add these new elements:
 * rtmp, coloreffects, audieffects, geometrictransform, ivfparse, shm
 * videomaxrate
- remove examples subpackage

* Thu Jul 29 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-6mdv2011.0
+ Revision: 562992
- rebuild

* Tue Jul 20 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-5mdv2011.0
+ Revision: 555150
- update build deps
- add libass plugin
- update build deps
- build with new celt

* Mon Jul 12 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-4mdv2011.0
+ Revision: 551208
- add upstream patches to build with neww wildmidi

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-3mdv2011.0
+ Revision: 550650
- useless bump of the release
- rebuild for lost packages

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.10.19-1mdv2011.0
+ Revision: 550463
- new version
- drop patches 2,3,4
- add vp8, invtelecine, segmentclip elements
- remove oss4audio element (now in -good)

* Tue Apr 13 2010 Frederic Crozat <fcrozat@mandriva.com> 0.10.18-3mdv2010.1
+ Revision: 534356
- switch back to musicbrainz 2.x
- Patch2 (GIT): use crc for table duplication (GNOME bug #614479)
- Patch3 (GIT): fix usage of strings in dvb
- Patch4 (GIT): fix dvb uint handling (GNOME bug #614475)

  + Christophe Fergeau <cfergeau@mandriva.com>
    - use newer libmusicbrainz

* Wed Mar 10 2010 Götz Waschk <waschk@mandriva.org> 0.10.18-2mdv2010.1
+ Revision: 517360
- add cog plugin

* Sun Mar 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.18-1mdv2010.1
+ Revision: 515592
- new version
- bump deps
- add libgstvdp package
- drop patch 2
- add new elements: jpegformat, dataurisrc, audioparsersbad, adpcmenc
- remove elements: aacparse, amrparse, shapewipe

* Tue Feb 16 2010 Götz Waschk <waschk@mandriva.org> 0.10.17-5mdv2010.1
+ Revision: 506489
- build with neon0.27 (teuf)

* Fri Feb 05 2010 Götz Waschk <waschk@mandriva.org> 0.10.17-4mdv2010.1
+ Revision: 501104
- fix DVD seek crash (bug #55442)

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 0.10.17-3mdv2010.1
+ Revision: 497065
- rebuild for new celt

* Thu Jan 07 2010 Götz Waschk <waschk@mandriva.org> 0.10.17-2mdv2010.1
+ Revision: 487153
- add kate plugin

* Sat Nov 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.17-1mdv2010.1
+ Revision: 467803
- new version
- drop patch 2
- update file list

* Mon Nov 09 2009 Götz Waschk <waschk@mandriva.org> 0.10.16-3mdv2010.1
+ Revision: 463517
- rebuild for missing packages

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 0.10.16-2mdv2010.1
+ Revision: 463291
- rebuild for new dfb

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 0.10.16-1mdv2010.1
+ Revision: 461143
- patch for new celt
- new version
- add rsvg plugin
- update file list

* Thu Oct 01 2009 Götz Waschk <waschk@mandriva.org> 0.10.14-5mdv2010.0
+ Revision: 452287
- add epoch to schroedinger element

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 0.10.14-4mdv2010.0
+ Revision: 447474
- update build deps

  + Frederic Crozat <fcrozat@mandriva.com>
    - Merge valve and rtpdemux into a voip subpackage and move liveadder and dmtf plugins in it too

* Mon Sep 21 2009 Frederic Crozat <fcrozat@mandriva.com> 0.10.14-2mdv2010.0
+ Revision: 446794
- Split rtpdemux and valve plugins in subpackages, needed by empathy
- Fix buildrequires for neon plugin

* Sun Aug 30 2009 Götz Waschk <waschk@mandriva.org> 0.10.14-1mdv2010.0
+ Revision: 422432
- update build deps
- new version
- add new elements: gme, schroedinger, vdpau
- add new libraries

* Thu Jun 18 2009 Götz Waschk <waschk@mandriva.org> 0.10.13-1mdv2010.0
+ Revision: 386949
- new version
- update file list

* Tue Jun 09 2009 Götz Waschk <waschk@mandriva.org> 0.10.12-3mdv2010.0
+ Revision: 384230
- rebuild for new soundtouch

* Thu May 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.12-2mdv2010.0
+ Revision: 378539
- fix file list for x264 build

* Thu May 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.12-1mdv2010.0
+ Revision: 378317
- fix build deps
- new version
- enable celt element
- drop patches 2,3
- update file list

* Tue Mar 24 2009 Götz Waschk <waschk@mandriva.org> 0.10.11-3mdv2009.1
+ Revision: 360827
- fix hanging aacparse element

* Sat Mar 21 2009 Emmanuel Andry <eandry@mandriva.org> 0.10.11-2mdv2009.1
+ Revision: 359942
- BR libmimic-devel

* Sat Mar 21 2009 Götz Waschk <waschk@mandriva.org> 0.10.11-1mdv2009.1
+ Revision: 359798
- add conflict with farsight plugin
- fix deps
- new version
- drop patches 2,3
- update file list
- remove twolame package

* Fri Mar 06 2009 Götz Waschk <waschk@mandriva.org> 0.10.10-3mdv2009.1
+ Revision: 349851
- fix faad build
- fix crash in faad

* Wed Feb 11 2009 Götz Waschk <waschk@mandriva.org> 0.10.10-2mdv2009.1
+ Revision: 339351
- rebuild for new faad

* Tue Jan 20 2009 Götz Waschk <waschk@mandriva.org> 0.10.10-1mdv2009.1
+ Revision: 331734
- new version
- drop patch 3
- drop library package
- bump deps
- update file list

* Thu Dec 04 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.9-2mdv2009.1
+ Revision: 310004
- Obsolete / Provides gstreamer0.10-fluendo-mpegdemux, it has been merged in gst-plugins-bad

  + Frederik Himpe <fhimpe@mandriva.org>
    - Build against libneon0.27

  + Götz Waschk <waschk@mandriva.org>
    - add celt support

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 0.10.9-1mdv2009.1
+ Revision: 299408
- new version
- add twolame and jp2k packages
- reenable dirac
- drop patch 2
- update patch 3
- update file list
- update build deps

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-6mdv2009.1
+ Revision: 293625
- rebuild for broken build system
- fix build with new x264

* Tue Oct 14 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-4mdv2009.1
+ Revision: 293566
- enable experimental dvd menu plugin

* Sun Aug 17 2008 Funda Wang <fwang@mandriva.org> 0.10.8-3mdv2009.0
+ Revision: 272982
- rebuild for new dfb

* Thu Aug 07 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10.8-2mdv2009.0
+ Revision: 266439
- Patch2 : ensure translated strings are encoded in UTF-8 (GNOME bug #546822)

  + Götz Waschk <waschk@mandriva.org>
    - add experimental build option

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2009.0
+ Revision: 263013
- new version
- update file list
- update license

* Fri Jul 25 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-7mdv2009.0
+ Revision: 248833
- disable dirac

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 30 2008 Funda Wang <fwang@mandriva.org> 0.10.7-6mdv2009.0
+ Revision: 213504
- rebuild for new directfb

* Fri May 16 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-4mdv2009.0
+ Revision: 208185
- bump
- fix path to timidity.cfg
- make wildmidi plugin depend on instruments

* Mon May 12 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-2mdv2009.0
+ Revision: 206247
- add dc1394 and wildmidi plugins

* Fri May 09 2008 Götz Waschk <waschk@mandriva.org> 0.10.7-1mdv2009.0
+ Revision: 204902
- new version
- drop patches 0,2,3
- add ofa, mplex, dirac, oss4, and subenc elements
- remove soup element, now in -good

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.10.6-5mdv2008.1
+ Revision: 190004
- split doc (no need on live CDs)

* Thu Mar 13 2008 Götz Waschk <waschk@mandriva.org> 0.10.6-4mdv2008.1
+ Revision: 187335
- add Mandriva branding

* Tue Mar 11 2008 Götz Waschk <waschk@mandriva.org> 0.10.6-3mdv2008.1
+ Revision: 185942
- AAC header fix
- disable checks (b.g.o #521749)
- build with exempi support

* Fri Feb 22 2008 Götz Waschk <waschk@mandriva.org> 0.10.6-2mdv2008.1
+ Revision: 173868
- fix nas plugin build
- update patch 2 with a CVS version

* Thu Feb 21 2008 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2008.1
+ Revision: 173609
- new version
- drop patch 0
- update patch 1
- patch2: disable a failing test
- readd mpeg2enc plugin
- add soundtouch, soup and metadata packages
- update file list

* Sun Jan 20 2008 Götz Waschk <waschk@mandriva.org> 0.10.5-6mdv2008.1
+ Revision: 155298
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jan 02 2008 Götz Waschk <waschk@mandriva.org> 0.10.5-5mdv2008.1
+ Revision: 140383
- rebuild

* Tue Jan 01 2008 Anssi Hannula <anssi@mandriva.org> 0.10.5-4mdv2008.1
+ Revision: 140124
- fix typo in x86_64 real path

* Tue Jan 01 2008 Götz Waschk <waschk@mandriva.org> 0.10.5-3mdv2008.1
+ Revision: 140076
- fix paths to the real codecs (bug #36437)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 28 2007 Götz Waschk <waschk@mandriva.org> 0.10.5-2mdv2008.1
+ Revision: 93529
- fix faad playback problem (upstream bug #476370)

* Wed Jun 20 2007 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdv2008.0
+ Revision: 41853
- new version
- drop patch
- add x264, amrwb and nas packages
- add library package
- update file list

* Tue May 22 2007 Götz Waschk <waschk@mandriva.org> 0.10.4-2mdv2008.0
+ Revision: 29708
- disable mpeg2enc plugin
- disable checks


* Fri Feb 23 2007 Götz Waschk <waschk@mandriva.org> 0.10.4-2mdv2007.0
+ Revision: 124950
- rebuild for new libmpcdec
- disable swfdec plugin
- fix buildrequires and reenable checks

* Fri Dec 29 2006 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.1
+ Revision: 102531
- fix buildrequires
- disable checks, one doesn't work in iurt
- unpack patch
- build with neon 0.26
- new version
- unpack patch
- add new plugins
- add docs
- fix distsuffix

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-4mdv2007.1
+ Revision: 92217
- fix description
- Import gstreamer0.10-plugins-bad

* Fri Dec 08 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-4mdv2007.1
- enable checks

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-3mdv2007.0
- enable neon module

* Sun Jun 18 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-2mdv2007.0
- add missing file
- fix buildrequires

* Tue May 09 2006 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdk
- update buildrequires
- update file list
- update the patch
- New release 0.10.3

* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-2mdk
- update patch 0

* Wed Feb 22 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdk
- update file list
- New release 0.10.1

* Thu Feb 16 2006 Götz Waschk <waschk@mandriva.org> 0.10.0-3mdk
- add a patch

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-2mdk
- improve description
- fix buildrequires

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdk
- initial package

