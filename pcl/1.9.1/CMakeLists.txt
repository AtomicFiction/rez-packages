CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(pcl_version $ENV{REZ_BUILD_PROJECT_VERSION})

set(link=static --toolset=gcc cflags=-fPIC cxxflags=-fPIC -j$ENV{REZ_BUILD_THREAD_COUNT})

ExternalProject_add(
    pcl
    PREFIX pcl
    GIT_REPOSITORY https://github.com/PointCloudLibrary/pcl.git
    GIT_TAG pcl-${pcl_version}
    CMAKE_ARGS
	-DCMAKE_BUILD_TYPE=Release
        -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
        -DFLANN_ROOT=$ENV{REZ_FLANN_ROOT}
        -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
        -DCMAKE_SKIP_BUILD_RPATH=FALSE
        -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE
        -DCMAKE_INSTALL_RPATH=$ENV{REZ_BOOST_ROOT}/lib:${CMAKE_INSTALL_PREFIX}/lib
)

INSTALL(CODE "MESSAGE(STATUS Installing.)")
