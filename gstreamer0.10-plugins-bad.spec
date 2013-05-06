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

%define oname	gst-plugins-bad
%define bname	gstreamer%{api}
%define api	0.10
%define major	23
%define libgstbasevideo		%mklibname gstbasevideo %{api} %{major}
%define libgstbasecamerabinsrc	%mklibname gstbasecamerabinsrc %{api} %{major}
%define libgstcodecparsers	%mklibname gstcodecparsers %{api} %{major}
%define libgstphotography	%mklibname gstphotography %{api} %{major}
%define libgstsignalprocessor	%mklibname gstsignalprocessor %{api} %{major}
%define libgstvdp 		%mklibname gstvdp %{api} %{major}
%define devname 		%mklibname %{oname} -d %{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-bad
Version:	0.10.23
Release:	5%{?extrarelsuffix}
License:	LGPLv2+ and GPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{oname}-%{version}.tar.bz2
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

BuildRequires:	fonts-ttf-dejavu
#gw for checks
BuildRequires:	gstreamer%{api}-plugins-good
BuildRequires:	bzip2-devel
#gw for autoreconf
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api}) >= 0.10.33
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	pkgconfig(libmimic)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sndfile)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
BuildRequires:	valgrind
%endif
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink
Provides:	%{bname}-fluendo-mpegdemux
Requires:	%{bname}-voip >= %{version}-%{release}
Conflicts:	%{bname}-farsight <= 1:0.12.10

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

%package -n %{libgstbasevideo}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgstbasevideo}
This package contains a shared library for %{name}.

%package -n %{libgstbasecamerabinsrc}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%{_lib}gstbasevideo0.10_23 < 0.10.23-5

%description -n %{libgstbasecamerabinsrc}
This package contains a shared library for %{name}.

%package -n %{libgstcodecparsers}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%{_lib}gstphotography0.10_23 < 0.10.23-5

%description -n %{libgstcodecparsers}
This package contains a shared library for %{name}.

%package -n %{libgstphotography}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgstphotography}
This package contains a shared library for %{name}.

%package -n %{libgstsignalprocessor}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%{_lib}gstphotography0.10_23 < 0.10.23-5

%description -n %{libgstsignalprocessor}
This package contains a shared library for %{name}.

%package -n %{libgstvdp}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgstvdp}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Development libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libgstbasevideo} = %{version}-%{release}
Requires:	%{libgstbasecamerabinsrc} = %{version}-%{release}
Requires:	%{libgstcodecparsers} = %{version}-%{release}
Requires:	%{libgstphotography} = %{version}-%{release}
Requires:	%{libgstsignalprocessor} = %{version}-%{release}
Requires:	%{libgstvdp} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gstphotography-devel < 0.10.23-5
Obsoletes:	%{_lib}gstbasevideo-devel < 0.10.23-5

%description -n %{devname}
This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n %{bname}-curl
Summary:	GStreamer Curl plugin
Group:		Networking/Other
BuildRequires:	pkgconfig(libcurl)

%description -n %{bname}-curl
This is a HTTP plugin for GStreamer based on the curl library.

%files -n %{bname}-curl
%{_libdir}/gstreamer-%{api}/libgstcurl.so

%package -n %{bname}-dc1394
Summary:	GStreamer DC1394 plugin
Group:		System/Libraries
BuildRequires:	pkgconfig(libdc1394-2)

%description -n %{bname}-dc1394
This is a IEEE 1394 (Firewire) support plugin for GStreamer.

%files -n %{bname}-dc1394
%{_libdir}/gstreamer-%{api}/libgstdc1394.so

%package -n %{bname}-ofa
Summary:	GStreamer OFA plugin
Group:		Sound
BuildRequires:	pkgconfig(libofa)

%description -n %{bname}-ofa
This is a metadata support plugin for GStreamer based on the Open
Fingerprint Architecture library.

%files -n %{bname}-ofa
%{_libdir}/gstreamer-%{api}/libgstofa.so

%package -n %{bname}-wildmidi
Summary:	GStreamer wildmidi plugin
Group:		Sound
BuildRequires:	wildmidi-devel
Requires:	timidity-instruments

%description -n %{bname}-wildmidi
This is a MIDI plugin for GStreamer based on the wildmidi library.

%files -n %{bname}-wildmidi
%{_libdir}/gstreamer-%{api}/libgstwildmidi.so

%package -n %{bname}-mpeg2enc
Summary:	GStreamer mjpegtools plug-in
Group:		Video
BuildRequires:	pkgconfig(mjpegtools)

%description -n %{bname}-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %{bname}-mpeg2enc
%{_libdir}/gstreamer-%{api}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{api}/libgstmplex.so

%if %{build_gme}
%package -n %{bname}-gme
Summary:	GStreamer Game Music plug-in
Group:		Sound
BuildRequires:	libgme-devel

%description -n %{bname}-gme
Game Music decoding plug-in.

%files -n %{bname}-gme
%{_libdir}/gstreamer-%{api}/libgstgme.so
%endif

%if %{build_dirac}
%package -n %{bname}-dirac
Summary:	GStreamer dirac plug-in
Group:		Video
BuildRequires:	pkgconfig(dirac)

%description -n %{bname}-dirac
Dirac encoding and decoding plug-in.

%files -n %{bname}-dirac
%{_libdir}/gstreamer-%{api}/libgstdirac.so
%endif

%package -n %{bname}-schroedinger
Summary:	GStreamer dirac plug-in based on Schroedinger
Group:		Video
BuildRequires:	pkgconfig(schroedinger-1.0)
Epoch:		1

%description -n %{bname}-schroedinger
Dirac encoding and decoding plug-in based on Schroedinger.

%files -n %{bname}-schroedinger
%{_libdir}/gstreamer-%{api}/libgstschro.so

%package -n %{bname}-vp8
Summary:	GStreamer VP8 plug-in
Group:		Video
BuildRequires:	pkgconfig(vpx)

%description -n %{bname}-vp8
VP8 encoding and decoding plug-in.

%files -n %{bname}-vp8
%{_libdir}/gstreamer-%{api}/libgstvp8.so
%{_libdir}/gstreamer-%{api}/libgstrtpvp8.so

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
%{_libdir}/gstreamer-%{api}/libgstladspa.so

%if %{build_dts}
%package -n %{bname}-dts
Summary:	GStreamer plug-ins for DTS audio playback
Group:		Sound
BuildRequires:	pkgconfig(libdts)

%description -n %{bname}-dts
Plug-ins for decoding DTS audio.

%files -n %{bname}-dts
%{_libdir}/gstreamer-%{api}/libgstdtsdec.so
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
%{_libdir}/gstreamer-%{api}/libgstxvid.so
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
%{_libdir}/gstreamer-%{api}/libgstmusepack.so

%package -n %{bname}-mms
Summary:	GStreamer plug-in for mms streams
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libmms)

%description -n %{bname}-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %{bname}-mms
%{_libdir}/gstreamer-%{api}/libgstmms.so

%package -n %{bname}-rtmp
Summary:	GStreamer plug-in for rtmp streams
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(librtmp)

%description -n %{bname}-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %{bname}-rtmp
%{_libdir}/gstreamer-%{api}/libgstrtmp.so

%package -n %{bname}-directfb
Summary:	GStreamer plug-in for DirectFB output
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(directfb)

%description -n %{bname}-directfb
Plug-in supporting the video output to DirectFB.

%files -n %{bname}-directfb
%{_libdir}/gstreamer-%{api}/libgstdfbvideosink.so

%package -n %{bname}-soundtouch
Summary:	GStreamer plug-in for SoundTouch support
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(soundtouch)

%description -n %{bname}-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %{bname}-soundtouch
%{_libdir}/gstreamer-%{api}/libgstsoundtouch.so

%package -n %{bname}-kate
Summary:	GStreamer Karaoke and text plugin
Group:		Video
BuildRequires:	pkgconfig(tiger)

%description -n %{bname}-kate
This is a Karaoke and text plugin for GStreamer based on libkate and libtiger.

%files -n %{bname}-kate
%{_libdir}/gstreamer-%{api}/libgstkate.so

%package -n %{bname}-libass
Summary:	GStreamer subtitles plugin
Group:		Video
BuildRequires:	pkgconfig(libass)

%description -n %{bname}-libass
This is a subtitle plugin for GStreamer based on libass.

%files -n %{bname}-libass
%{_libdir}/gstreamer-%{api}/libgstassrender.so

%package -n %{bname}-resindvd
Summary:	GStreamer DVD menu plugin
Group:		Video
BuildRequires:	pkgconfig(dvdnav)

%description -n %{bname}-resindvd
This is a DVD playback plugin for GStreamer with menu support.

%files -n %{bname}-resindvd
%{_libdir}/gstreamer-%{api}/libresindvd.so

%package -n %{bname}-voip
Summary:	GStreamer voip plugins
Group:		Sound

%description -n %{bname}-voip
This is a collection of VoIP plugins for GStreamer.

%files -n %{bname}-voip
%{_libdir}/gstreamer-%{api}/libgstrtpmux.so
%{_libdir}/gstreamer-%{api}/libgstliveadder.so
%{_libdir}/gstreamer-%{api}/libgstdtmf.so

%package -n %{bname}-cog
Summary:	GStreamer COG plugin
Group:		Video
BuildRequires:	pkgconfig(orc-0.4)

%description -n %{bname}-cog
This is a signal processing plugin for GStreamer based on Orc.

%files -n %{bname}-cog
%{_libdir}/gstreamer-%{api}/libgstcog.so

%package -n %{bname}-vdpau
Summary:	GStreamer plug-in for playback using VDPAU
Group:		Video
BuildRequires:	vdpau-devel

%description -n %{bname}-vdpau
This plug-in adds video playback support to GStreamer based on VDPAU 
(Video Decode and Presentation API for Unix).

%files -n %{bname}-vdpau
%{_libdir}/gstreamer-%{api}/libgstvdpau.so

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
%{_libdir}/gstreamer-%{api}/libgstfaad.so
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
%{_libdir}/gstreamer-%{api}/libgstfaac.so
%endif

%package -n %{bname}-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	gsm-devel >= 1.0.10

%description -n %{bname}-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%files -n %{bname}-gsm
%{_libdir}/gstreamer-%{api}/libgstgsm.so

%package -n %{bname}-neon
Summary:	GStreamer HTTP plugin based on libneon
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(neon)

%description -n %{bname}-neon
Plug-in for HTTP access based on libneon.

%files -n %{bname}-neon
%{_libdir}/gstreamer-%{api}/libgstneonhttpsrc.so

%package -n %{bname}-nas
Summary:	Gstreamer output plugin for the NAS sound server
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	nas-devel

%description -n %{bname}-nas
Output plugin for GStreamer for use with the nas sound server.

%files -n %{bname}-nas
%{_libdir}/gstreamer-%{api}/libgstnassink.so

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
%{_datadir}/gstreamer-%{api}/presets/GstVoAmrwbEnc.prs
%{_libdir}/gstreamer-%{api}/libgstvoamrwbenc.so
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
%{_libdir}/gstreamer-%{api}/libgstvoaacenc.so
%endif

%package -n %{bname}-jp2k
Summary:	GStreamer plug-in for JPEG2000 support
Group:		Graphics
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(jasper)

%description -n %{bname}-jp2k
Plug-in for JPEG2000 support under GStreamer.

%files -n %{bname}-jp2k
%{_libdir}/gstreamer-%{api}/libgstjp2k.so
%{_libdir}/gstreamer-%{api}/libgstjp2kdecimator.so

%if %{build_celt}
%package -n %{bname}-celt
Summary:	GStreamer plug-in for CELT support
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(celt)

%description -n %{bname}-celt
Plug-in for CELT support under GStreamer.

%files -n %{bname}-celt
%{_libdir}/gstreamer-%{api}/libgstcelt.so
%endif

%package -n %{bname}-rsvg
Summary:	GStreamer plug-in for SVG support
Group:		Graphics
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(librsvg-2.0)

%description -n %{bname}-rsvg
Plug-in for SVG support under GStreamer.

%files -n %{bname}-rsvg
%{_libdir}/gstreamer-%{api}/libgstrsvg.so

%package doc
Group:		Books/Computer books
Summary:	GStreamer application library

%description doc
This is the documentation of %{name}.

%files doc
%doc docs/plugins/html
%{_datadir}/gtk-doc/html/*

%prep
%setup -qn %{oname}-%{version}
%apply_patches
#gw broken configure in 0.10.19.2
#autoreconf -fi

%build
#work around broken mjpegtools headers including config.h:
export CPPFLAGS="-I."
%configure2_5x \
	--disable-static \
	--disable-dependency-tracking \
	--with-package-name='%{distribution} %{name} package' \
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

%find_lang %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml
%{_libdir}/gstreamer-%{api}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{api}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{api}/libgstaiff.so
%{_libdir}/gstreamer-%{api}/libgstapexsink.so
%{_libdir}/gstreamer-%{api}/libgstasfmux.so
%{_libdir}/gstreamer-%{api}/libgstautoconvert.so
%{_libdir}/gstreamer-%{api}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{api}/libgstbayer.so
%{_libdir}/gstreamer-%{api}/libgstcamerabin.so
%{_libdir}/gstreamer-%{api}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{api}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{api}/libgstcolorspace.so
%{_libdir}/gstreamer-%{api}/libgstdccp.so
%{_libdir}/gstreamer-%{api}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{api}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{api}/libgstdvb.so
%{_libdir}/gstreamer-%{api}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{api}/libgstdvdspu.so
%{_libdir}/gstreamer-%{api}/libgstfaceoverlay.so
%{_libdir}/gstreamer-%{api}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{api}/libgstfestival.so
%{_libdir}/gstreamer-%{api}/libgstfrei0r.so
%{_libdir}/gstreamer-%{api}/libgstfreeverb.so
%{_libdir}/gstreamer-%{api}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{api}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{api}/libgstgsettingselements.so
%{_libdir}/gstreamer-%{api}/libgsthdvparse.so
%{_libdir}/gstreamer-%{api}/libgstid3tag.so
%{_libdir}/gstreamer-%{api}/libgstinter.so
%{_libdir}/gstreamer-%{api}/libgstinterlace.so
%{_libdir}/gstreamer-%{api}/libgstivfparse.so
%{_libdir}/gstreamer-%{api}/libgstjpegformat.so
%{_libdir}/gstreamer-%{api}/libgstlegacyresample.so
%{_libdir}/gstreamer-%{api}/libgstmpegdemux.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpegvideoparse.so
%{_libdir}/gstreamer-%{api}/libgstmve.so
%{_libdir}/gstreamer-%{api}/libgstmimic.so
%{_libdir}/gstreamer-%{api}/libgstmxf.so
%{_libdir}/gstreamer-%{api}/libgstopenal.so
# New version of opencv is not supported yet,
# uncomment when the plugin is built again
#{_libdir}/gstreamer-%{api}/libgstopencv.so
%{_libdir}/gstreamer-%{api}/libgstopus.so
%{_libdir}/gstreamer-%{api}/libgstpcapparse.so
%{_libdir}/gstreamer-%{api}/libgstpnm.so
%{_libdir}/gstreamer-%{api}/libgstrawparse.so
%{_libdir}/gstreamer-%{api}/libgstreal.so
%{_libdir}/gstreamer-%{api}/libgstremovesilence.so
%{_libdir}/gstreamer-%{api}/libgstscaletempoplugin.so
%{_libdir}/gstreamer-%{api}/libgstsdpelem.so
%{_libdir}/gstreamer-%{api}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{api}/libgstshm.so
%{_libdir}/gstreamer-%{api}/libgstsiren.so
%{_libdir}/gstreamer-%{api}/libgstsmooth.so
%{_libdir}/gstreamer-%{api}/libgstsndfile.so
%{_libdir}/gstreamer-%{api}/libgststereo.so
%{_libdir}/gstreamer-%{api}/libgstsubenc.so
%{_libdir}/gstreamer-%{api}/libgstvcdsrc.so
%{_libdir}/gstreamer-%{api}/libgstvideomaxrate.so
%{_libdir}/gstreamer-%{api}/libgstvideomeasure.so
%{_libdir}/gstreamer-%{api}/libgstvideosignal.so
%{_libdir}/gstreamer-%{api}/libgstvmnc.so
%{_libdir}/gstreamer-%{api}/libgstbz2.so
%{_libdir}/gstreamer-%{api}/libgstcdaudio.so
%{_libdir}/gstreamer-%{api}/libgstcdxaparse.so
%{_libdir}/gstreamer-%{api}/libgstdecklink.so
%{_libdir}/gstreamer-%{api}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{api}/libgstfragmented.so
%{_libdir}/gstreamer-%{api}/libgstlinsys.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{api}/libgstpatchdetect.so
%{_libdir}/gstreamer-%{api}/libgstsdi.so
%{_libdir}/gstreamer-%{api}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{api}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{api}/libgstfreeze.so
%{_libdir}/gstreamer-%{api}/libgsth264parse.so
%{_libdir}/gstreamer-%{api}/libgstmodplug.so
%{_libdir}/gstreamer-%{api}/libgstnsf.so
%{_libdir}/gstreamer-%{api}/libgstnuvdemux.so
%{_libdir}/gstreamer-%{api}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{api}/libgstsdl.so
%{_libdir}/gstreamer-%{api}/libgstspeed.so
%{_libdir}/gstreamer-%{api}/libgsttrm.so
%{_libdir}/gstreamer-%{api}/libgsttta.so
%{_libdir}/gstreamer-%{api}/libgsty4mdec.so

%files -n %{libgstbasevideo}
%{_libdir}/libgstbasevideo-%{api}.so.%{major}*

%files -n %{libgstbasecamerabinsrc}
%{_libdir}/libgstbasecamerabinsrc-%{api}.so.%{major}*

%files -n  %{libgstcodecparsers}
%{_libdir}/libgstcodecparsers-%{api}.so.%{major}*

%files -n %{libgstphotography}
%{_libdir}/libgstphotography-%{api}.so.%{major}*

%files -n %{libgstsignalprocessor}
%{_libdir}/libgstsignalprocessor-%{api}.so.%{major}*

%files -n %{libgstvdp}
%{_libdir}/libgstvdp-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libgstbasevideo-%{api}.so
%{_libdir}/libgstbasecamerabinsrc-%{api}.so
%{_libdir}/libgstcodecparsers-%{api}.so
%{_libdir}/libgstphotography-%{api}.so
%{_libdir}/libgstsignalprocessor-%{api}.so
%{_libdir}/libgstvdp-%{api}.so
%{_includedir}/gstreamer-%{api}/gst/basecamerabinsrc/*.h
%{_includedir}/gstreamer-%{api}/gst/codecparsers
%{_includedir}/gstreamer-%{api}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{api}/gst/signalprocessor/gstsignalprocessor.h
%{_includedir}/gstreamer-%{api}/gst/vdpau/
%{_includedir}/gstreamer-%{api}/gst/video/
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-basevideo-%{api}.pc

