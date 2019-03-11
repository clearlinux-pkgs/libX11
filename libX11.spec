Name     : libX11
Version  : 1.6.7
Release  : 412

Source0: https://xorg.freedesktop.org/releases/individual/lib/libX11-1.6.7.tar.gz

%global LIB10 libICE
Source10 : https://xorg.freedesktop.org/releases/individual/lib/libICE-1.0.9.tar.gz

%global LIB20 libSM
Source20 : https://xorg.freedesktop.org/releases/individual/lib/libSM-1.2.3.tar.gz

%global LIB30 libXau
Source30 : https://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.gz

%global LIB40 libXdmcp
Source40 : https://xorg.freedesktop.org/releases/individual/lib/libXdmcp-1.1.2.tar.gz

%global LIB50 libX11
Source50 : https://xorg.freedesktop.org/releases/individual/lib/libX11-1.6.7.tar.gz

%global LIB60 libXext
Source60 : https://xorg.freedesktop.org/releases/individual/lib/libXext-1.3.3.tar.gz

%global LIB70 libXinerama
Source70 : https://xorg.freedesktop.org/releases/individual/lib/libXinerama-1.1.4.tar.gz

%global LIB80 libXfixes
Source80 : https://xorg.freedesktop.org/releases/individual/lib/libXfixes-5.0.3.tar.gz

%global LIB90 libXdamage
Source90 : https://xorg.freedesktop.org/releases/individual/lib/libXdamage-1.1.4.tar.gz

%global LIB100 libXrender
Source100: https://xorg.freedesktop.org/releases/individual/lib/libXrender-0.9.10.tar.gz

%global LIB110 libXrandr
Source110: https://xorg.freedesktop.org/releases/individual/lib/libXrandr-1.5.1.tar.gz

%global LIB120 libXcomposite
Source120: https://xorg.freedesktop.org/releases/individual/lib/libXcomposite-0.4.4.tar.gz

%global LIB130 libXi
Source130: https://xorg.freedesktop.org/releases/individual/lib/libXi-1.7.9.tar.gz

%global LIB140 libXxf86vm
Source140: https://xorg.freedesktop.org/releases/individual/lib/libXxf86vm-1.1.4.tar.gz

%global LIB150 libxshmfence
Source150: https://xorg.freedesktop.org/releases/individual/lib/libxshmfence-1.3.tar.bz2

%global LIB200 libxcb
%global LIB200_EXTRA64 output/usr/lib64/libxcb-composite.a output/usr/lib64/libxcb-damage.a  output/usr/lib64/libxcb-dpms.a output/usr/lib64/libxcb-dri2.a output/usr/lib64/libxcb-dri3.a output/usr/lib64/libxcb-glx.a  output/usr/lib64/libxcb-present.a output/usr/lib64/libxcb-randr.a output/usr/lib64/libxcb-record.a output/usr/lib64/libxcb-render.a output/usr/lib64/libxcb-res.a output/usr/lib64/libxcb-screensaver.a output/usr/lib64/libxcb-shape.a output/usr/lib64/libxcb-shm.a output/usr/lib64/libxcb-sync.a output/usr/lib64/libxcb-xf86dri.a output/usr/lib64/libxcb-xfixes.a output/usr/lib64/libxcb-xinerama.a output/usr/lib64/libxcb-xinput.a output/usr/lib64/libxcb-xkb.a output/usr/lib64/libxcb-xtest.a output/usr/lib64/libxcb-xv.a output/usr/lib64/libxcb-xvmc.a output/usr/lib64/libX11-xcb.a
%global LIB200_EXTRA32 output/usr/lib32/libxcb-composite.a output/usr/lib32/libxcb-damage.a  output/usr/lib32/libxcb-dpms.a output/usr/lib32/libxcb-dri2.a output/usr/lib32/libxcb-dri3.a output/usr/lib32/libxcb-glx.a  output/usr/lib32/libxcb-present.a output/usr/lib32/libxcb-randr.a output/usr/lib32/libxcb-record.a output/usr/lib32/libxcb-render.a output/usr/lib32/libxcb-res.a output/usr/lib32/libxcb-screensaver.a output/usr/lib32/libxcb-shape.a output/usr/lib32/libxcb-shm.a output/usr/lib32/libxcb-sync.a output/usr/lib32/libxcb-xf86dri.a output/usr/lib32/libxcb-xfixes.a output/usr/lib32/libxcb-xinerama.a output/usr/lib32/libxcb-xinput.a output/usr/lib32/libxcb-xkb.a output/usr/lib32/libxcb-xtest.a output/usr/lib32/libxcb-xv.a output/usr/lib32/libxcb-xvmc.a output/usr/lib32/libX11-xcb.a

Source200: https://xorg.freedesktop.org/releases/individual/xcb/libxcb-1.13.1.tar.gz

%global LIB210 libxcb-util
Source210: http://xcb.freedesktop.org/dist/xcb-util-0.4.0.tar.gz

# %global LIB220 libxcb-cursor
# xxxxx220: https://xcb.freedesktop.org/dist/xcb-util-cursor-0.1.3.tar.gz

%global LIB230 libxcb-image
Source230: https://xcb.freedesktop.org/dist/xcb-util-image-0.4.0.tar.bz2

%global LIB240 libxcb-keysyms
Source240: http://xcb.freedesktop.org/dist/xcb-util-keysyms-0.4.0.tar.gz

%global LIB250 libxcb-render-util
Source250: https://xcb.freedesktop.org/dist/xcb-util-renderutil-0.3.9.tar.gz

%global LIB260 libxcb-icccm
%global LIB260_EXTRA64 output/usr/lib64/libxcb-ewmh.a
%global LIB260_EXTRA32 output/usr/lib32/libxcb-ewmh.a
Source260: https://xcb.freedesktop.org/dist/xcb-util-wm-0.4.1.tar.bz2

# %global LIB270 libxcb-xrm
# xxxxx270: https://github.com/Airblader/xcb-util-xrm/releases/download/v1.3/xcb-util-xrm-1.3.tar.bz2

Group    : Development/Tools
License  : MIT
Requires: libX11-doc
Summary: superset xorg libraries
Requires: libX11-lib = %{version}-%{release}
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

%define provide() libX11%1 libICE%1 libSM%1 libXau%1 libXdmcp%1 libXext%1 libXinerama%1 libXfixes%1 libXdamage%1 libXrender%1 libXrandr%1 libXcomposite%1 libXi%1 libXxf86vm%1 libxshmfence%1 libxcb%1 xcb-util-image%1 xcb-util-keysyms%1 xcb-util-renderutil%1 xcb-util-wm%1 xcb-util%1
Provides: %provide %{nil}
Provides: %provide -- -data

%description
libX11 is a grouping of various xorg small libraries into a master .so
for effciency reasons


%package lib
Summary: lib components for the libX11 package.
Group: Binaries
Provides: %provide -- -lib

%description lib
bin components for the libX11 package.

%package lib32
Summary: lib components for the libX11 package.
Group: Binaries
Provides: %provide -- -lib32

%description lib32
bin components for the libX11 package.

%package dev
Summary: dev components for the libX11 package.
Group: Binaries
Provides: %provide -- -dev
Requires: libX11-lib

%description dev
bin components for the libX11 package.

%package dev32
Summary: dev components for the libX11 package.
Group: Binaries
Requires: libX11-dev
Provides: %provide -- -dev32

%description dev32
bin components for the libX11 package.


%package doc
Summary: doc components for the libX11 package.
Group: Documentation

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
Provides: %provide -- -man

%description man
man components for the libX11 package.


%prep
%setup -q

%build

BuildOne() {
	echo Building $1 $2
	n=$1
	tar -axf $n
	d=${n##*/}
	d=${d/.tar*}
	shift
	mv $d $d-avx2
	pushd $d-avx2
		CFLAGS="$CFLAGS64 -march=haswell" LDFLAGS="$LDFLAGS64" PKG_CONFIG_LIB="$PKG_CONFIG_LIB64" PKG_CONFIG_PATH="$PKG_CONFIG_PATH64"	 %configure --enable-static --cache-file=${CACHEFILE}-avx2 "$@"
		LD_LIBRARY_PATH=/builddir/build/BUILD/output/usr/lib64 \
			make %{?_smp_mflags}
		%make_install DESTDIR=/builddir/build/BUILD/output-avx2
	popd
	tar -axf $n
	mv $d $d-64
	pushd $d-64
		CFLAGS="$CFLAGS64" LDFLAGS="$LDFLAGS64" PKG_CONFIG_LIB="$PKG_CONFIG_LIB64" PKG_CONFIG_PATH="$PKG_CONFIG_PATH64"	 %configure --enable-static --cache-file=${CACHEFILE}64 "$@"
		LD_LIBRARY_PATH=/builddir/build/BUILD/output/usr/lib64 \
			make %{?_smp_mflags}
		%make_install DESTDIR=/builddir/build/BUILD/output
		make VERBOSE=1 V=1 check || :
	popd
	tar -axf $n
	mv $d $d-32
	pushd $d-32
		CFLAGS="$CFLAGS32" LDFLAGS="$LDFLAGS32" PKG_CONFIG_LIB="$PKG_CONFIG_LIB32" PKG_CONFIG_PATH="$PKG_CONFIG_PATH32" %configure --enable-static --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu  --cache-file=${CACHEFILE}32 "$@"
		LD_LIBRARY_PATH=/builddir/build/BUILD/output/usr/lib32 \
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
export SOURCE_DATE_EPOCH=1547586456
export CFLAGS32="$CFLAGS -ffat-lto-objects -flto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -L/builddir/build/BUILD/output/usr/lib32 -I/builddir/build/BUILD/output/usr/include -m32"
export CFLAGS64="$CFLAGS -O3 -ffat-lto-objects -flto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -mzero-caller-saved-regs=used -L/builddir/build/BUILD/output/usr/lib64 -I/builddir/build/BUILD/output/usr/include"
export LDFLAGS32="$LDFLAGS -m32"
export LDFLAGS64="$LDFLAGS -m64"
export PKG_CONFIG_PATH64="/usr/lib64/pkgconfig:/builddir/build/BUILD/output/usr/lib64/pkgconfig"
export PKG_CONFIG_PATH32="/usr/lib32/pkgconfig:/builddir/build/BUILD/output/usr/lib32/pkgconfig"
export PKG_CONFIG_LIBDIR64="/usr/lib64/pkgconfig:/builddir/build/BUILD/output/usr/lib64/pkgconfig"
export PKG_CONFIG_LIBDIR32="/usr/lib32/pkgconfig:/builddir/build/BUILD/output/usr/lib32/pkgconfig"


mkdir -p output output-avx2
touch cachefile-avx2 cachefile64 cachefile32
CACHEFILE=$PWD/cachefile


BuildOne %{SOURCE10} --disable-tcp-transport
BuildOne %{SOURCE20}
BuildOne %{SOURCE30}
BuildOne %{SOURCE40}

# xcb round one to bootstrap
BuildOne %{SOURCE200} --disable-dri3 --with-queue-size=32768 PYTHON=/usr/bin/python2 


BuildOne %{SOURCE50}
BuildOne %{SOURCE60}
BuildOne %{SOURCE70}
BuildOne %{SOURCE80}
BuildOne %{SOURCE90}
BuildOne %{SOURCE100}
BuildOne %{SOURCE110}
BuildOne %{SOURCE120}
BuildOne %{SOURCE130}
BuildOne %{SOURCE140}
BuildOne %{SOURCE150}


# xcb
BuildOne %{SOURCE200} --enable-dri3 --with-queue-size=32768 PYTHON=/usr/bin/python2

# xcb util libs
BuildOne %{SOURCE210}
BuildOne %{SOURCE230}
BuildOne %{SOURCE240}
BuildOne %{SOURCE250}
BuildOne %{SOURCE260}

# Put the haswell files in place
mkdir output/usr/lib64/haswell
mv output-avx2/usr/lib64/*.so* output-avx2/usr/lib64/*.a output/usr/lib64/haswell

# Now link the libraries
mkdir -p 64/haswell
libs="output/usr/lib64/%{LIB10}.a \
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
	output/usr/lib64/%{LIB150}.a \
	output/usr/lib64/%{LIB200}.a %{LIB200_EXTRA64} \
	output/usr/lib64/%{LIB210}.a \
	output/usr/lib64/%{LIB230}.a \
	output/usr/lib64/%{LIB240}.a \
	output/usr/lib64/%{LIB250}.a \
	output/usr/lib64/%{LIB260}.a %{LIB260_EXTRA64}"

gcc $CFLAGS $LDFLAGS -m64 -o 64/libX11.so.6.3.0 -Wl,--no-undefined -Wl,-soname,libX11.so.6 -flto=`getconf _NPROCESSORS_ONLN` -Wl,--whole-archive $libs -Wl,--no-whole-archive -shared	-ldl
gcc $CFLAGS $LDFLAGS -march=haswell -m64 -o 64/haswell/libX11.so.6.3.0 -Wl,--no-undefined -Wl,-soname,libX11.so.6 -flto=`getconf _NPROCESSORS_ONLN` -Wl,--whole-archive ${libs//64/64/haswell} -Wl,--no-whole-archive -shared	-ldl

ln -s libX11.so.6.3.0 64/libX11.so
ln -s libX11.so.6.3.0 64/libX11.so.6
ln -s libX11.so.6.3.0 64/haswell/libX11.so
ln -s libX11.so.6.3.0 64/haswell/libX11.so.6

mkdir 32/
gcc $CFLAGS $LDFLAGS -m32 -o 32/libX11.so.6.3.0 -Wl,--no-undefined -Wl,-soname,libX11.so.6 -flto=`getconf _NPROCESSORS_ONLN` -Wl,--whole-archive ${libs//64/32} -Wl,--no-whole-archive -shared	 -ldl

ln -s libX11.so.6.3.0 32/libX11.so
ln -s libX11.so.6.3.0 32/libX11.so.6
tar -axf %{SOURCE0}

popd

%install
export SOURCE_DATE_EPOCH=1552311600 
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
find output/usr/lib64 -name 'lib*.so.?' -printf "%f\n" | \
    xargs -P`getconf _NPROCESSORS_ONLN` -rtI@ \
	gcc $CFLAGS $LDFLAGS -o %{buildroot}/usr/lib64/@  -Wl,--no-as-needed -Wl,--no-undefined  -Wl,-soname,@  -L64/ -lX11 -shared

find output/usr/lib32 -name 'lib*.so.?'  -printf "%f\n" | \
    xargs -P`getconf _NPROCESSORS_ONLN` -rtI@ \
	gcc $CFLAGS $LDFLAGS -m32 -o %{buildroot}/usr/lib32/@  -Wl,--no-as-needed -Wl,--no-undefined  -Wl,-soname,@  -L32/ -lX11 -shared

# for each of the sub library .so files, create a linker script
echo "INPUT(libX11.so.6)" | tee > /dev/null \
	`find output/usr/lib64/*.so  -printf "%{buildroot}/usr/lib64/%f\n"` \
	`find output/usr/lib32/*.so  -printf "%{buildroot}/usr/lib32/%f\n"`

cp -a 64/libX11.so* 64/haswell  %{buildroot}/usr/lib64
cp -a 32/libX11.so*  %{buildroot}/usr/lib32

popd

%check
pushd ..

# for each of the sub library .so.X files, verify its symbols are
# present in the master library
for abi in 64 64/haswell 32; do
    nm -D --defined $abi/libX11.so | \
        cut -d' ' -f2- | sort > output/usr/lib$abi/symlist.master
    find output/usr/lib$abi -name 'lib*.so.*' -type f | xargs -n1 nm -D --defined | \
        cut -d' ' -f2- | sort -u > output/usr/lib$abi/symlist.sub
    comm -23 output/usr/lib$abi/symlist.{master,sub} > symdiff
    if [ -s symdiff ]; then
        echo "Symbols found in sub-library but not in master library:" >&2
        cat symdiff >&2
        exit 1
    fi
done

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
/usr/lib64/haswell/*.so
/usr/lib64/pkgconfig/*

%files dev32
%defattr(-,root,root,-)
/usr/lib32/*.so
/usr/lib32/pkgconfig/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/haswell/*.so.*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/*.so.*

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/*
%doc /usr/share/man/
