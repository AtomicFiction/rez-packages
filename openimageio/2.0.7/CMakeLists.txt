CMAKE_MINIMUM_REQUIRED(VERSION 3.1)
cmake_policy(SET CMP0037 OLD)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(openimageio_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    openimageio
    GIT_REPOSITORY https://github.com/OpenImageIO/oiio.git
    GIT_TAG Release-${openimageio_version}
    PREFIX openimageio
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
               -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON
               -DVERBOSE=TRUE
               -DCMAKE_CXX_STANDARD=11
               #-DCMAKE_CXX_FLAGS="-fext-numeric-literals"
               -DCMAKE_CXX_FLAGS=-DBOOST_HAS_INT128=1
               -DBUILDSTATIC=ON
               -DUSE_PYTHON=ON
               -DUSE_fPIC=ON
               -DTIFF_INCLUDE_DIR=/Volumes/af/tools/thirdparty/darwin/tiff/4.0.6/include
               -DTIFF_LIBRARY=/Volumes/af/tools/thirdparty/darwin/tiff/4.0.6/lib/libtiff.dylib
               -DJPEG_INCLUDE_DIR=$ENV{REZ_LIBJPEG_ROOT}/include
               -DJPEG_LIBRARY=$ENV{REZ_LIBJPEG_ROOT}/lib/libjpeg.dylib
               -DOIIO_BUILD_TESTS=OFF
               -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
               -DBoost_NO_SYSTEM_PATHS=ON
               -DILMBASE_ROOT_DIR=$ENV{REZ_ILMBASE_ROOT}
               -DOPENEXR_ROOT_DIR=$ENV{REZ_OPENEXR_ROOT}
               -DUSE_OCIO=ON
               -DOCIO_PATH=$ENV{REZ_OPENCOLORIO_ROOT}
               -DCMAKE_SKIP_BUILD_RPATH=FALSE
               -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
               -DCMAKE_INSTALL_RPATH=$ENV{REZ_BOOST_ROOT}/lib:$ENV{REZ_PTEX_ROOT}/lib64:$ENV{REZ_ILMBASE_ROOT}/lib:$ENV{REZ_OPENEXR_ROOT}/lib:$ENV{REZ_OPENCOLORIO_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib64
)
