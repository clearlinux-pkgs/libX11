Name     : libX11
Version  : 1.6.7
Release  : 400

Source0: https://xorg.freedesktop.org/releases/individual/lib/libX11-1.6.7.tar.gz

%global LIB10 libICE
%global VER10 1.0.9
Source10 : https://xorg.freedesktop.org/releases/individual/lib/libICE-1.0.9.tar.gz

%global LIB20 libSM
%global VER20 1.2.3
Source20 : https://xorg.freedesktop.org/releases/individual/lib/libSM-1.2.3.tar.gz

%global LIB30 libXau
%global VER30 1.0.8
Source30 : https://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.gz

%global LIB40 libXdmcp
%global VER40 1.1.2
Source40 : https://xorg.freedesktop.org/releases/individual/lib/libXdmcp-1.1.2.tar.gz

%global LIB50 libX11
%global VER50 1.6.7
Source50 : https://xorg.freedesktop.org/releases/individual/lib/libX11-1.6.7.tar.gz

%global LIB60 libXext
%global VER60 1.3.3
Source60 : https://xorg.freedesktop.org/releases/individual/lib/libXext-1.3.3.tar.gz

%global LIB70 libXinerama
%global VER70 1.1.4
Source70 : https://xorg.freedesktop.org/releases/individual/lib/libXinerama-1.1.4.tar.gz

%global LIB80 libXfixes
%global VER80 5.0.3
Source80 : https://xorg.freedesktop.org/releases/individual/lib/libXfixes-5.0.3.tar.gz

%global LIB90 libXdamage
%global VER90 1.1.4
Source90 : https://xorg.freedesktop.org/releases/individual/lib/libXdamage-1.1.4.tar.gz

%global LIB100 libXrender
%global VER100 0.9.10
Source100: https://xorg.freedesktop.org/releases/individual/lib/libXrender-0.9.10.tar.gz

%global LIB110 libXrandr
%global VER110 1.5.1
Source110: https://xorg.freedesktop.org/releases/individual/lib/libXrandr-1.5.1.tar.gz

%global LIB120 libXcomposite
%global VER120 0.4.4
Source120: https://xorg.freedesktop.org/releases/individual/lib/libXcomposite-0.4.4.tar.gz

%global LIB130 libXi
%global VER130 1.7.9
Source130: https://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.9.tar.gz

%global LIB140 libXxf86vm
%global VER140 1.1.4
Source140: https://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-1.1.4.tar.gz

%global LIB200 libxcb
%global VER200 1.13.1
%global LIB200_EXTRA64 output/usr/lib64/libxcb-composite.a output/usr/lib64/libxcb-damage.a  output/usr/lib64/libxcb-dpms.a output/usr/lib64/libxcb-dri2.a output/usr/lib64/libxcb-dri3.a output/usr/lib64/libxcb-glx.a  output/usr/lib64/libxcb-present.a output/usr/lib64/libxcb-randr.a output/usr/lib64/libxcb-record.a output/usr/lib64/libxcb-render.a output/usr/lib64/libxcb-res.a output/usr/lib64/libxcb-screensaver.a output/usr/lib64/libxcb-shape.a output/usr/lib64/libxcb-shm.a output/usr/lib64/libxcb-sync.a output/usr/lib64/libxcb-xf86dri.a output/usr/lib64/libxcb-xfixes.a output/usr/lib64/libxcb-xinerama.a output/usr/lib64/libxcb-xinput.a output/usr/lib64/libxcb-xkb.a output/usr/lib64/libxcb-xtest.a output/usr/lib64/libxcb-xv.a output/usr/lib64/libxcb-xvmc.a output/usr/lib64/libX11-xcb.a
%global LIB200_EXTRA32 output/usr/lib32/libxcb-composite.a output/usr/lib32/libxcb-damage.a  output/usr/lib32/libxcb-dpms.a output/usr/lib32/libxcb-dri2.a output/usr/lib32/libxcb-dri3.a output/usr/lib32/libxcb-glx.a  output/usr/lib32/libxcb-present.a output/usr/lib32/libxcb-randr.a output/usr/lib32/libxcb-record.a output/usr/lib32/libxcb-render.a output/usr/lib32/libxcb-res.a output/usr/lib32/libxcb-screensaver.a output/usr/lib32/libxcb-shape.a output/usr/lib32/libxcb-shm.a output/usr/lib32/libxcb-sync.a output/usr/lib32/libxcb-xf86dri.a output/usr/lib32/libxcb-xfixes.a output/usr/lib32/libxcb-xinerama.a output/usr/lib32/libxcb-xinput.a output/usr/lib32/libxcb-xkb.a output/usr/lib32/libxcb-xtest.a output/usr/lib32/libxcb-xv.a output/usr/lib32/libxcb-xvmc.a output/usr/lib32/libX11-xcb.a

Source200: https://xorg.freedesktop.org/releases/individual/xcb/libxcb-1.13.1.tar.gz


Group    : Development/Tools
License  : MIT
Requires: libX11-bin
Requires: libX11-license
Requires: libX11-man
Summary: superset xorg libraries



BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32xf86bigfontproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(32xtrans)
BuildRequires : pkgconfig(xf86bigfontproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xtrans)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xcb-proto)
BuildRequires : xcb-proto
BuildRequires : asciidoc
BuildRequires : python-core
BuildRequires : libpthread-stubs-dev

BuildRequires : xmlto

%description
libX11 is a grouping of various xorg small libraries into a master .so
for effciency reasons


%package lib
Summary: lib components for the libX11 package.
Group: Binaries
Requires: libX11-license

%description lib
bin components for the libX11 package.

%package lib32
Summary: lib components for the libX11 package.
Group: Binaries
Requires: libX11-license

%description lib32
bin components for the libX11 package.

%package dev
Summary: dev components for the libX11 package.
Group: Binaries
Requires: libX11-license
Provides: libX11-dev libICE-dev libSM-dev libXau-dev libXdmcp-dev libXext-dev libXinerama-dev libXfixes-dev libXdamage-dev libXrender-dev libXrandr-dev libXcomposite-dev libXi-dev libXxf86vm-dev libxcb-dev

%description dev
bin components for the libX11 package.

%package dev32
Summary: dev components for the libX11 package.
Group: Binaries
Requires: libX11-license
Requires: libX11-dev
Provides: libX11-dev32 libICE-dev32 libSM-dev32 libXau-dev32 libXdmcp-dev32 libXext-dev32 libXinerama-dev32 libXfixes-dev32 libXdamage-dev32 libXrender-dev32 libXrandr-dev32 libXcomposite-dev32 libXi-dev32 libXxf86vm-dev32 libxcb-dev32

%description dev32
bin components for the libX11 package.


%package doc
Summary: doc components for the libX11 package.
Group: Documentation
Requires: libX11-man

%description doc
doc components for the libX11 package.


%package license
Summary: license components for the libX11 package
Group: Default

%description license
license components for the libX11 package.


%package man
Summary: man components for the libX11 package.
Group: Default

%description man
man components for the libX11 package.


%prep
%setup -q

%build


BuildOne() {
	echo Building $1 $2 $3
	tar -axf $1
	mv $2 $2-64
	pushd $2-64
		CFLAGS="$CFLAGS64" LDFLAGS="$LDFLAGS64" PKG_CONFIG_LIB="$PKG_CONFIG_LIB64" PKG_CONFIG_PATH="$PKG_CONFIG_PATH64"  %configure --enable-static ${@:3}
		make %{?_smp_mflags}
		%make_install DESTDIR=/builddir/build/BUILD/output
		make VERBOSE=1 V=1 check || :
	popd
	tar -axf $1
	mv $2 $2-32
	pushd $2-32
		CFLAGS="$CFLAGS32" LDFLAGS="$LDFLAGS32" PKG_CONFIG_LIB="$PKG_CONFIG_LIB32" PKG_CONFIG_PATH="$PKG_CONFIG_PATH32" %configure --enable-static --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu   ${@:3}
		make %{?_smp_mflags}
		%make_install32 DESTDIR=/builddir/build/BUILD/output
	popd
	
	rm -f output/usr/lib64/*.la
	rm -f output/usr/lib32/*.la

	CFLAGS="$CFLAGS64"
	LDFLAGS="$LDFLAGS64"
	
}

pushd ..

export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=153420600
export CFLAGS32="$CFLAGS -ffat-lto-objects -flto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -L/builddir/build/BUILD/output/usr/lib32 -I/builddir/build/BUILD/output/usr/include -m32"
export CFLAGS64="$CFLAGS -Os -ffat-lto-objects -flto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -mzero-caller-saved-regs=used -L/builddir/build/BUILD/output/usr/lib64 -I/builddir/build/BUILD/output/usr/include"
export LDFLAGS32="$LDFLAGS -m32"
export LDFLAGS64="$LDFLAGS -m64"
export PKG_CONFIG_PATH64="/usr/lib64/pkgconfig:/builddir/build/BUILD/output/usr/lib64/pkgconfig"
export PKG_CONFIG_PATH32="/usr/lib32/pkgconfig:/builddir/build/BUILD/output/usr/lib32/pkgconfig"
export PKG_CONFIG_LIBDIR64="/usr/lib64/pkgconfig:/builddir/build/BUILD/output/usr/lib64/pkgconfig"
export PKG_CONFIG_LIBDIR32="/usr/lib32/pkgconfig:/builddir/build/BUILD/output/usr/lib32/pkgconfig"


mkdir -p output


BuildOne %{SOURCE10} %{LIB10}-%{VER10} --disable-tcp-transport
BuildOne %{SOURCE20} %{LIB20}-%{VER20}
BuildOne %{SOURCE30} %{LIB30}-%{VER30}
BuildOne %{SOURCE40} %{LIB40}-%{VER40}

# xcb round one to bootstrap
BuildOne %{SOURCE200} %{LIB200}-%{VER200} --disable-dri3 --with-queue-size=32768 PYTHON=/usr/bin/python2 


BuildOne %{SOURCE50} %{LIB50}-%{VER50}
BuildOne %{SOURCE60} %{LIB60}-%{VER60}
BuildOne %{SOURCE70} %{LIB70}-%{VER70}
BuildOne %{SOURCE80} %{LIB80}-%{VER80}
BuildOne %{SOURCE90} %{LIB90}-%{VER90}
BuildOne %{SOURCE100} %{LIB100}-%{VER100}
BuildOne %{SOURCE110} %{LIB110}-%{VER110}
BuildOne %{SOURCE120} %{LIB120}-%{VER120}
BuildOne %{SOURCE130} %{LIB130}-%{VER130}
BuildOne %{SOURCE140} %{LIB140}-%{VER140}


# xcb
BuildOne %{SOURCE200} %{LIB200}-%{VER200} --enable-dri3 --with-queue-size=32768 PYTHON=/usr/bin/python2


mkdir 64/
gcc $CFLAGS $LDFLAGS -m64 -o 64/libX11.so.6.3.0  -Wl,--no-undefined  -Wl,-soname,libX11.so.6 -Wl,--whole-archive  \
	output/usr/lib64/%{LIB10}.a \
	output/usr/lib64/%{LIB20}.a \
	output/usr/lib64/%{LIB30}.a \
	output/usr/lib64/%{LIB40}.a \
	output/usr/lib64/%{LIB50}.a \
	output/usr/lib64/%{LIB60}.a \
	output/usr/lib64/%{LIB70}.a \
	output/usr/lib64/%{LIB80}.a \
	output/usr/lib64/%{LIB90}.a \
	output/usr/lib64/%{LIB100}.a \
	output/usr/lib64/%{LIB110}.a \
	output/usr/lib64/%{LIB120}.a \
	output/usr/lib64/%{LIB130}.a \
	output/usr/lib64/%{LIB140}.a \
	output/usr/lib64/%{LIB200}.a %{LIB200_EXTRA64} \
	-Wl,--no-whole-archive -shared  -ldl
	
ln -s libX11.so.6.3.0 64/libX11.so
ln -s libX11.so.6.3.0 64/libX11.so.6




mkdir 32/
gcc $CFLAGS $LDFLAGS -m32 -o 32/libX11.so.6.3.0  -Wl,--no-undefined  -Wl,-soname,libX11.so.6 -Wl,--whole-archive  \
	output/usr/lib32/%{LIB10}.a \
	output/usr/lib32/%{LIB20}.a \
	output/usr/lib32/%{LIB30}.a \
	output/usr/lib32/%{LIB40}.a \
	output/usr/lib32/%{LIB50}.a \
	output/usr/lib32/%{LIB60}.a \
	output/usr/lib32/%{LIB70}.a \
	output/usr/lib32/%{LIB80}.a \
	output/usr/lib32/%{LIB90}.a \
	output/usr/lib32/%{LIB100}.a \
	output/usr/lib32/%{LIB110}.a \
	output/usr/lib32/%{LIB120}.a \
	output/usr/lib32/%{LIB130}.a \
	output/usr/lib32/%{LIB140}.a \
	output/usr/lib32/%{LIB200}.a %{LIB200_EXTRA32} \
	-Wl,--no-whole-archive -shared   -ldl

ln -s libX11.so.6.3.0 32/libX11.so
ln -s libX11.so.6.3.0 32/libX11.so.6
tar -axf %{SOURCE0}

popd

%install
export SOURCE_DATE_EPOCH=153420600
rm -rf %{buildroot}

pushd ..

mkdir -p %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/lib32

cp -a output/usr/lib64/pkgconfig %{buildroot}/usr/lib64
cp -a output/usr/lib32/pkgconfig %{buildroot}/usr/lib32

cp -a output/usr/share %{buildroot}/usr
cp -a output/usr/include %{buildroot}/usr


# create the 32 bit pkgconfig helper links
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi

# for each of the sub library .so.X files, create a small wrapper
for i in `find output/usr/lib64/*.so.?  -printf "%f\n"` ; do
	gcc $CFLAGS $LDFLAGS -o %{buildroot}/usr/lib64/$i  -Wl,--no-as-needed -Wl,--no-undefined  -Wl,-soname,$i -Wl,--whole-archive -Wl,--no-whole-archive  -L64/ -lX11 -shared 
	gcc $CFLAGS $LDFLAGS -m32 -o %{buildroot}/usr/lib32/$i  -Wl,--no-as-needed -Wl,--no-undefined  -Wl,-soname,$i -Wl,--whole-archive -Wl,--no-whole-archive  -L32/ -lX11 -shared 
done

# for each of the sub library .so files, create a linker script
for i in `find output/usr/lib64/*.so  -printf "%f\n"` ; do
	echo "INPUT(libX11.so.6)" > %{buildroot}/usr/lib64/$i
	echo "INPUT(libX11.so.6)" > %{buildroot}/usr/lib32/$i
done

cp -a 64/libX11.so*  %{buildroot}/usr/lib64
cp -a 32/libX11.so*  %{buildroot}/usr/lib32

popd


%files
%defattr(-,root,root,-)
/usr/share/X11/locale/
/usr/share/X11/XErrorDB
/usr/share/X11/Xcms.txt

%files dev
%defattr(-,root,root,-)
/usr/include
/usr/lib64/*.so
/usr/lib64/pkgconfig/*

%files dev32
%defattr(-,root,root,-)
/usr/lib32/*.so
/usr/lib32/pkgconfig/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/*.so.*

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/*
%doc /usr/share/man/