CMAKE_MINIMUM_REQUIRED(VERSION 3.1)
cmake_policy(SET CMP0037 OLD)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(opencolorio_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_opencolorio opencolorio/opencolorio-${opencolorio_version}.tar.gz
    http://github.com/imageworks/OpenColorIO/tarball/v${opencolorio_version}
)

set(BOOST_ROOT $ENV{REZ_BOOST_ROOT})

find_package(Boost)

ExternalProject_add(
    opencolorio
    PREFIX opencolorio
    URL ${url_opencolorio}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
               -DVERBOSE=ON
               -DOCIO_USE_BOOST_PTR=ON
               -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
               -DCMAKE_CXX_FLAGS=-I${Boost_INCLUDE_DIR}
               -DCMAKE_POSITION_INDEPENDENT_CODE=ON
               -DCMAKE_SKIP_BUILD_RPATH=OFF
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_BOOST_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)

