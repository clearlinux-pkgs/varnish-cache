#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : varnish-cache
Version  : 6.1.1
Release  : 3
URL      : https://github.com/varnishcache/varnish-cache/archive/varnish-6.1.1.tar.gz
Source0  : https://github.com/varnishcache/varnish-cache/archive/varnish-6.1.1.tar.gz
Summary  : Varnish API
Group    : Development/Tools
License  : BSD-2-Clause
Requires: varnish-cache-bin = %{version}-%{release}
Requires: varnish-cache-data = %{version}-%{release}
Requires: varnish-cache-lib = %{version}-%{release}
Requires: varnish-cache-license = %{version}-%{release}
Requires: varnish-cache-man = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : docutils
BuildRequires : graphviz
BuildRequires : jemalloc-dev
BuildRequires : ncurses-dev
BuildRequires : nghttp2-dev
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : readline-dev

%description
This is a modified version of the ZLIB 1.2.8 data compression library.
ZLIB DATA COMPRESSION LIBRARY

%package bin
Summary: bin components for the varnish-cache package.
Group: Binaries
Requires: varnish-cache-data = %{version}-%{release}
Requires: varnish-cache-license = %{version}-%{release}
Requires: varnish-cache-man = %{version}-%{release}

%description bin
bin components for the varnish-cache package.


%package data
Summary: data components for the varnish-cache package.
Group: Data

%description data
data components for the varnish-cache package.


%package dev
Summary: dev components for the varnish-cache package.
Group: Development
Requires: varnish-cache-lib = %{version}-%{release}
Requires: varnish-cache-bin = %{version}-%{release}
Requires: varnish-cache-data = %{version}-%{release}
Provides: varnish-cache-devel = %{version}-%{release}

%description dev
dev components for the varnish-cache package.


%package doc
Summary: doc components for the varnish-cache package.
Group: Documentation
Requires: varnish-cache-man = %{version}-%{release}

%description doc
doc components for the varnish-cache package.


%package lib
Summary: lib components for the varnish-cache package.
Group: Libraries
Requires: varnish-cache-data = %{version}-%{release}
Requires: varnish-cache-license = %{version}-%{release}

%description lib
lib components for the varnish-cache package.


%package license
Summary: license components for the varnish-cache package.
Group: Default

%description license
license components for the varnish-cache package.


%package man
Summary: man components for the varnish-cache package.
Group: Default

%description man
man components for the varnish-cache package.


%prep
%setup -q -n varnish-cache-varnish-6.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545943776
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1545943776
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/varnish-cache
cp LICENSE %{buildroot}/usr/share/package-licenses/varnish-cache/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/varnishadm
/usr/bin/varnishd
/usr/bin/varnishhist
/usr/bin/varnishlog
/usr/bin/varnishncsa
/usr/bin/varnishstat
/usr/bin/varnishtest
/usr/bin/varnishtop

%files data
%defattr(-,root,root,-)
/usr/share/varnish/vcl/devicedetect.vcl
/usr/share/varnish/vmodtool.py
/usr/share/varnish/vsctool.py

%files dev
%defattr(-,root,root,-)
/usr/include/varnish/cache/cache.h
/usr/include/varnish/cache/cache_backend.h
/usr/include/varnish/cache/cache_director.h
/usr/include/varnish/cache/cache_filter.h
/usr/include/varnish/cache/cache_varnishd.h
/usr/include/varnish/common/common_param.h
/usr/include/varnish/miniobj.h
/usr/include/varnish/tbl/acct_fields_bereq.h
/usr/include/varnish/tbl/acct_fields_req.h
/usr/include/varnish/tbl/backend_poll.h
/usr/include/varnish/tbl/ban_vars.h
/usr/include/varnish/tbl/bo_flags.h
/usr/include/varnish/tbl/boc_state.h
/usr/include/varnish/tbl/body_status.h
/usr/include/varnish/tbl/cli_cmds.h
/usr/include/varnish/tbl/debug_bits.h
/usr/include/varnish/tbl/feature_bits.h
/usr/include/varnish/tbl/h2_error.h
/usr/include/varnish/tbl/h2_frames.h
/usr/include/varnish/tbl/h2_settings.h
/usr/include/varnish/tbl/h2_stream.h
/usr/include/varnish/tbl/htc.h
/usr/include/varnish/tbl/http_headers.h
/usr/include/varnish/tbl/http_response.h
/usr/include/varnish/tbl/locks.h
/usr/include/varnish/tbl/obj_attr.h
/usr/include/varnish/tbl/oc_exp_flags.h
/usr/include/varnish/tbl/oc_flags.h
/usr/include/varnish/tbl/params.h
/usr/include/varnish/tbl/req_body.h
/usr/include/varnish/tbl/req_flags.h
/usr/include/varnish/tbl/sess_attr.h
/usr/include/varnish/tbl/sess_close.h
/usr/include/varnish/tbl/steps.h
/usr/include/varnish/tbl/symbol_kind.h
/usr/include/varnish/tbl/vcc_types.h
/usr/include/varnish/tbl/vcl_returns.h
/usr/include/varnish/tbl/vhd_fsm.h
/usr/include/varnish/tbl/vhd_fsm_funcs.h
/usr/include/varnish/tbl/vhd_return.h
/usr/include/varnish/tbl/vhp_huffman.h
/usr/include/varnish/tbl/vhp_static.h
/usr/include/varnish/tbl/vrt_stv_var.h
/usr/include/varnish/tbl/vsc_levels.h
/usr/include/varnish/tbl/vsl_tags.h
/usr/include/varnish/tbl/vsl_tags_http.h
/usr/include/varnish/tbl/waiters.h
/usr/include/varnish/vapi/vapi_options.h
/usr/include/varnish/vapi/voptget.h
/usr/include/varnish/vapi/vsc.h
/usr/include/varnish/vapi/vsl.h
/usr/include/varnish/vapi/vsl_int.h
/usr/include/varnish/vapi/vsm.h
/usr/include/varnish/vas.h
/usr/include/varnish/vav.h
/usr/include/varnish/vbm.h
/usr/include/varnish/vcl.h
/usr/include/varnish/vcli.h
/usr/include/varnish/vcs.h
/usr/include/varnish/vdef.h
/usr/include/varnish/vmod_abi.h
/usr/include/varnish/vqueue.h
/usr/include/varnish/vre.h
/usr/include/varnish/vrnd.h
/usr/include/varnish/vrt.h
/usr/include/varnish/vrt_obj.h
/usr/include/varnish/vsa.h
/usr/include/varnish/vsb.h
/usr/include/varnish/vsha256.h
/usr/include/varnish/vtcp.h
/usr/include/varnish/vtim.h
/usr/include/varnish/vut.h
/usr/include/varnish/vut_options.h
/usr/include/varnish/waiter/waiter.h
/usr/lib64/libvarnishapi.so
/usr/lib64/pkgconfig/varnishapi.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/vmod_blob.3
/usr/share/man/man3/vmod_directors.3
/usr/share/man/man3/vmod_proxy.3
/usr/share/man/man3/vmod_purge.3
/usr/share/man/man3/vmod_std.3
/usr/share/man/man3/vmod_unix.3
/usr/share/man/man3/vmod_vtc.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/varnish/builtin.vcl
/usr/share/doc/varnish/example.vcl

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvarnishapi.so.2
/usr/lib64/libvarnishapi.so.2.0.0
/usr/lib64/varnish/vmods/libvmod_blob.so
/usr/lib64/varnish/vmods/libvmod_directors.so
/usr/lib64/varnish/vmods/libvmod_proxy.so
/usr/lib64/varnish/vmods/libvmod_purge.so
/usr/lib64/varnish/vmods/libvmod_std.so
/usr/lib64/varnish/vmods/libvmod_unix.so
/usr/lib64/varnish/vmods/libvmod_vtc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/varnish-cache/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/varnishadm.1
/usr/share/man/man1/varnishd.1
/usr/share/man/man1/varnishhist.1
/usr/share/man/man1/varnishlog.1
/usr/share/man/man1/varnishncsa.1
/usr/share/man/man1/varnishstat.1
/usr/share/man/man1/varnishtest.1
/usr/share/man/man1/varnishtop.1
/usr/share/man/man7/varnish-cli.7
/usr/share/man/man7/varnish-counters.7
/usr/share/man/man7/vcl.7
/usr/share/man/man7/vsl-query.7
/usr/share/man/man7/vsl.7
/usr/share/man/man7/vtc.7
