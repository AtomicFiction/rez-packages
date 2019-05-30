CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(flann_version $ENV{REZ_BUILD_PROJECT_VERSION})

ExternalProject_add(
    flann
    PREFIX flann
    GIT_REPOSITORY https://github.com/mariusmuja/flann.git
    GIT_TAG ${flann_version}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
)

INSTALL(CODE "MESSAGE(STATUS Installing.)")
