#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libX11
Version  : 1.6.3
Release  : 7
URL      : http://xorg.freedesktop.org/releases/individual/lib/libX11-1.6.3.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libX11-1.6.3.tar.gz
Summary  : X Library XCB interface
Group    : Development/Tools
License  : MIT
Requires: libX11-lib
Requires: libX11-data
Requires: libX11-doc
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(kbproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xf86bigfontproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xtrans)
BuildRequires : xmlto

%description
libX11 - Core X11 protocol client library
Documentation for this library can be found in the included man pages,
and in the Xlib spec from the specs subdirectory, also available at:

%package data
Summary: data components for the libX11 package.
Group: Data

%description data
data components for the libX11 package.


%package dev
Summary: dev components for the libX11 package.
Group: Development
Requires: libX11-lib
Requires: libX11-data
Provides: libX11-devel

%description dev
dev components for the libX11 package.


%package doc
Summary: doc components for the libX11 package.
Group: Documentation

%description doc
doc components for the libX11 package.


%package lib
Summary: lib components for the libX11 package.
Group: Libraries
Requires: libX11-data

%description lib
lib components for the libX11 package.


%prep
%setup -q -n libX11-1.6.3

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 -flto "
export FCFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 -flto "
export FFLAGS="$CFLAGS -fno-semantic-interposition -falign-functions=32 -O3 -flto "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -falign-functions=32 -O3 -flto "
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

%files data
%defattr(-,root,root,-)
/usr/share/X11/XErrorDB
/usr/share/X11/Xcms.txt
/usr/share/X11/locale/C/Compose
/usr/share/X11/locale/C/XI18N_OBJS
/usr/share/X11/locale/C/XLC_LOCALE
/usr/share/X11/locale/am_ET.UTF-8/Compose
/usr/share/X11/locale/am_ET.UTF-8/XI18N_OBJS
/usr/share/X11/locale/am_ET.UTF-8/XLC_LOCALE
/usr/share/X11/locale/armscii-8/Compose
/usr/share/X11/locale/armscii-8/XI18N_OBJS
/usr/share/X11/locale/armscii-8/XLC_LOCALE
/usr/share/X11/locale/compose.dir
/usr/share/X11/locale/cs_CZ.UTF-8/Compose
/usr/share/X11/locale/cs_CZ.UTF-8/XI18N_OBJS
/usr/share/X11/locale/cs_CZ.UTF-8/XLC_LOCALE
/usr/share/X11/locale/el_GR.UTF-8/Compose
/usr/share/X11/locale/el_GR.UTF-8/XI18N_OBJS
/usr/share/X11/locale/el_GR.UTF-8/XLC_LOCALE
/usr/share/X11/locale/en_US.UTF-8/Compose
/usr/share/X11/locale/en_US.UTF-8/XI18N_OBJS
/usr/share/X11/locale/en_US.UTF-8/XLC_LOCALE
/usr/share/X11/locale/fi_FI.UTF-8/Compose
/usr/share/X11/locale/fi_FI.UTF-8/XI18N_OBJS
/usr/share/X11/locale/fi_FI.UTF-8/XLC_LOCALE
/usr/share/X11/locale/georgian-academy/Compose
/usr/share/X11/locale/georgian-academy/XI18N_OBJS
/usr/share/X11/locale/georgian-academy/XLC_LOCALE
/usr/share/X11/locale/georgian-ps/Compose
/usr/share/X11/locale/georgian-ps/XI18N_OBJS
/usr/share/X11/locale/georgian-ps/XLC_LOCALE
/usr/share/X11/locale/ibm-cp1133/Compose
/usr/share/X11/locale/ibm-cp1133/XI18N_OBJS
/usr/share/X11/locale/ibm-cp1133/XLC_LOCALE
/usr/share/X11/locale/iscii-dev/Compose
/usr/share/X11/locale/iscii-dev/XI18N_OBJS
/usr/share/X11/locale/iscii-dev/XLC_LOCALE
/usr/share/X11/locale/isiri-3342/Compose
/usr/share/X11/locale/isiri-3342/XI18N_OBJS
/usr/share/X11/locale/isiri-3342/XLC_LOCALE
/usr/share/X11/locale/iso8859-1/Compose
/usr/share/X11/locale/iso8859-1/XI18N_OBJS
/usr/share/X11/locale/iso8859-1/XLC_LOCALE
/usr/share/X11/locale/iso8859-10/Compose
/usr/share/X11/locale/iso8859-10/XI18N_OBJS
/usr/share/X11/locale/iso8859-10/XLC_LOCALE
/usr/share/X11/locale/iso8859-11/Compose
/usr/share/X11/locale/iso8859-11/XI18N_OBJS
/usr/share/X11/locale/iso8859-11/XLC_LOCALE
/usr/share/X11/locale/iso8859-13/Compose
/usr/share/X11/locale/iso8859-13/XI18N_OBJS
/usr/share/X11/locale/iso8859-13/XLC_LOCALE
/usr/share/X11/locale/iso8859-14/Compose
/usr/share/X11/locale/iso8859-14/XI18N_OBJS
/usr/share/X11/locale/iso8859-14/XLC_LOCALE
/usr/share/X11/locale/iso8859-15/Compose
/usr/share/X11/locale/iso8859-15/XI18N_OBJS
/usr/share/X11/locale/iso8859-15/XLC_LOCALE
/usr/share/X11/locale/iso8859-2/Compose
/usr/share/X11/locale/iso8859-2/XI18N_OBJS
/usr/share/X11/locale/iso8859-2/XLC_LOCALE
/usr/share/X11/locale/iso8859-3/Compose
/usr/share/X11/locale/iso8859-3/XI18N_OBJS
/usr/share/X11/locale/iso8859-3/XLC_LOCALE
/usr/share/X11/locale/iso8859-4/Compose
/usr/share/X11/locale/iso8859-4/XI18N_OBJS
/usr/share/X11/locale/iso8859-4/XLC_LOCALE
/usr/share/X11/locale/iso8859-5/Compose
/usr/share/X11/locale/iso8859-5/XI18N_OBJS
/usr/share/X11/locale/iso8859-5/XLC_LOCALE
/usr/share/X11/locale/iso8859-6/Compose
/usr/share/X11/locale/iso8859-6/XI18N_OBJS
/usr/share/X11/locale/iso8859-6/XLC_LOCALE
/usr/share/X11/locale/iso8859-7/Compose
/usr/share/X11/locale/iso8859-7/XI18N_OBJS
/usr/share/X11/locale/iso8859-7/XLC_LOCALE
/usr/share/X11/locale/iso8859-8/Compose
/usr/share/X11/locale/iso8859-8/XI18N_OBJS
/usr/share/X11/locale/iso8859-8/XLC_LOCALE
/usr/share/X11/locale/iso8859-9/Compose
/usr/share/X11/locale/iso8859-9/XI18N_OBJS
/usr/share/X11/locale/iso8859-9/XLC_LOCALE
/usr/share/X11/locale/iso8859-9e/Compose
/usr/share/X11/locale/iso8859-9e/XI18N_OBJS
/usr/share/X11/locale/iso8859-9e/XLC_LOCALE
/usr/share/X11/locale/ja.JIS/Compose
/usr/share/X11/locale/ja.JIS/XI18N_OBJS
/usr/share/X11/locale/ja.JIS/XLC_LOCALE
/usr/share/X11/locale/ja.SJIS/Compose
/usr/share/X11/locale/ja.SJIS/XI18N_OBJS
/usr/share/X11/locale/ja.SJIS/XLC_LOCALE
/usr/share/X11/locale/ja/Compose
/usr/share/X11/locale/ja/XI18N_OBJS
/usr/share/X11/locale/ja/XLC_LOCALE
/usr/share/X11/locale/ja_JP.UTF-8/Compose
/usr/share/X11/locale/ja_JP.UTF-8/XI18N_OBJS
/usr/share/X11/locale/ja_JP.UTF-8/XLC_LOCALE
/usr/share/X11/locale/km_KH.UTF-8/Compose
/usr/share/X11/locale/km_KH.UTF-8/XI18N_OBJS
/usr/share/X11/locale/km_KH.UTF-8/XLC_LOCALE
/usr/share/X11/locale/ko/Compose
/usr/share/X11/locale/ko/XI18N_OBJS
/usr/share/X11/locale/ko/XLC_LOCALE
/usr/share/X11/locale/ko_KR.UTF-8/Compose
/usr/share/X11/locale/ko_KR.UTF-8/XI18N_OBJS
/usr/share/X11/locale/ko_KR.UTF-8/XLC_LOCALE
/usr/share/X11/locale/koi8-c/Compose
/usr/share/X11/locale/koi8-c/XI18N_OBJS
/usr/share/X11/locale/koi8-c/XLC_LOCALE
/usr/share/X11/locale/koi8-r/Compose
/usr/share/X11/locale/koi8-r/XI18N_OBJS
/usr/share/X11/locale/koi8-r/XLC_LOCALE
/usr/share/X11/locale/koi8-u/Compose
/usr/share/X11/locale/koi8-u/XI18N_OBJS
/usr/share/X11/locale/koi8-u/XLC_LOCALE
/usr/share/X11/locale/locale.alias
/usr/share/X11/locale/locale.dir
/usr/share/X11/locale/microsoft-cp1251/Compose
/usr/share/X11/locale/microsoft-cp1251/XI18N_OBJS
/usr/share/X11/locale/microsoft-cp1251/XLC_LOCALE
/usr/share/X11/locale/microsoft-cp1255/Compose
/usr/share/X11/locale/microsoft-cp1255/XI18N_OBJS
/usr/share/X11/locale/microsoft-cp1255/XLC_LOCALE
/usr/share/X11/locale/microsoft-cp1256/Compose
/usr/share/X11/locale/microsoft-cp1256/XI18N_OBJS
/usr/share/X11/locale/microsoft-cp1256/XLC_LOCALE
/usr/share/X11/locale/mulelao-1/Compose
/usr/share/X11/locale/mulelao-1/XI18N_OBJS
/usr/share/X11/locale/mulelao-1/XLC_LOCALE
/usr/share/X11/locale/nokhchi-1/Compose
/usr/share/X11/locale/nokhchi-1/XI18N_OBJS
/usr/share/X11/locale/nokhchi-1/XLC_LOCALE
/usr/share/X11/locale/pt_BR.UTF-8/Compose
/usr/share/X11/locale/pt_BR.UTF-8/XI18N_OBJS
/usr/share/X11/locale/pt_BR.UTF-8/XLC_LOCALE
/usr/share/X11/locale/ru_RU.UTF-8/Compose
/usr/share/X11/locale/ru_RU.UTF-8/XI18N_OBJS
/usr/share/X11/locale/ru_RU.UTF-8/XLC_LOCALE
/usr/share/X11/locale/sr_CS.UTF-8/Compose
/usr/share/X11/locale/sr_CS.UTF-8/XI18N_OBJS
/usr/share/X11/locale/sr_CS.UTF-8/XLC_LOCALE
/usr/share/X11/locale/tatar-cyr/Compose
/usr/share/X11/locale/tatar-cyr/XI18N_OBJS
/usr/share/X11/locale/tatar-cyr/XLC_LOCALE
/usr/share/X11/locale/th_TH.UTF-8/Compose
/usr/share/X11/locale/th_TH.UTF-8/XI18N_OBJS
/usr/share/X11/locale/th_TH.UTF-8/XLC_LOCALE
/usr/share/X11/locale/th_TH/Compose
/usr/share/X11/locale/th_TH/XI18N_OBJS
/usr/share/X11/locale/th_TH/XLC_LOCALE
/usr/share/X11/locale/tscii-0/Compose
/usr/share/X11/locale/tscii-0/XI18N_OBJS
/usr/share/X11/locale/tscii-0/XLC_LOCALE
/usr/share/X11/locale/vi_VN.tcvn/Compose
/usr/share/X11/locale/vi_VN.tcvn/XI18N_OBJS
/usr/share/X11/locale/vi_VN.tcvn/XLC_LOCALE
/usr/share/X11/locale/vi_VN.viscii/Compose
/usr/share/X11/locale/vi_VN.viscii/XI18N_OBJS
/usr/share/X11/locale/vi_VN.viscii/XLC_LOCALE
/usr/share/X11/locale/zh_CN.UTF-8/Compose
/usr/share/X11/locale/zh_CN.UTF-8/XI18N_OBJS
/usr/share/X11/locale/zh_CN.UTF-8/XLC_LOCALE
/usr/share/X11/locale/zh_CN.gb18030/Compose
/usr/share/X11/locale/zh_CN.gb18030/XI18N_OBJS
/usr/share/X11/locale/zh_CN.gb18030/XLC_LOCALE
/usr/share/X11/locale/zh_CN.gbk/Compose
/usr/share/X11/locale/zh_CN.gbk/XI18N_OBJS
/usr/share/X11/locale/zh_CN.gbk/XLC_LOCALE
/usr/share/X11/locale/zh_CN/Compose
/usr/share/X11/locale/zh_CN/XI18N_OBJS
/usr/share/X11/locale/zh_CN/XLC_LOCALE
/usr/share/X11/locale/zh_HK.UTF-8/Compose
/usr/share/X11/locale/zh_HK.UTF-8/XI18N_OBJS
/usr/share/X11/locale/zh_HK.UTF-8/XLC_LOCALE
/usr/share/X11/locale/zh_HK.big5/Compose
/usr/share/X11/locale/zh_HK.big5/XI18N_OBJS
/usr/share/X11/locale/zh_HK.big5/XLC_LOCALE
/usr/share/X11/locale/zh_HK.big5hkscs/Compose
/usr/share/X11/locale/zh_HK.big5hkscs/XI18N_OBJS
/usr/share/X11/locale/zh_HK.big5hkscs/XLC_LOCALE
/usr/share/X11/locale/zh_TW.UTF-8/Compose
/usr/share/X11/locale/zh_TW.UTF-8/XI18N_OBJS
/usr/share/X11/locale/zh_TW.UTF-8/XLC_LOCALE
/usr/share/X11/locale/zh_TW.big5/Compose
/usr/share/X11/locale/zh_TW.big5/XI18N_OBJS
/usr/share/X11/locale/zh_TW.big5/XLC_LOCALE
/usr/share/X11/locale/zh_TW/Compose
/usr/share/X11/locale/zh_TW/XI18N_OBJS
/usr/share/X11/locale/zh_TW/XLC_LOCALE

%files dev
%defattr(-,root,root,-)
/usr/include/X11/ImUtil.h
/usr/include/X11/XKBlib.h
/usr/include/X11/Xcms.h
/usr/include/X11/Xlib-xcb.h
/usr/include/X11/Xlib.h
/usr/include/X11/XlibConf.h
/usr/include/X11/Xlibint.h
/usr/include/X11/Xlocale.h
/usr/include/X11/Xregion.h
/usr/include/X11/Xresource.h
/usr/include/X11/Xutil.h
/usr/include/X11/cursorfont.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libX11/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
