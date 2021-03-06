CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(pyside_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_pyside pyside/PySide-${pyside_version}.tar.gz
    https://codeload.github.com/pyside/PySide/tar.gz/${pyside_version}
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    pyside
    URL ${url_pyside}
    PREFIX pyside
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DBUILDSTATIC=ON
               -DLINKSTATIC=ON
               -DCMAKE_SKIP_BUILD_RPATH=FALSE
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_QT_ROOT}/lib:$ENV{REZ_SHIBOKEN_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)

install(CODE "message(STATUS Installing...)")
