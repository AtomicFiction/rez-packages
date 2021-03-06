CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(sip_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_sip sip/sip-${sip_version}.tar.gz
    http://iweb.dl.sourceforge.net/project/pyqt/sip/sip-${sip_version}/sip-${sip_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    sip_build
    URL ${url_sip}
    PREFIX sip
    CONFIGURE_COMMAND python ./configure.py --static --sysroot=${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND ${install_cmd}
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make ${make_args}
)

install(CODE "message(STATUS Installing...)")
