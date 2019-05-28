CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(eigen_version $ENV{REZ_BUILD_PROJECT_VERSION})

ExternalProject_add(
    eigen
    PREFIX eigen
    GIT_REPOSITORY https://github.com/eigenteam/eigen-git-mirror.git
    GIT_TAG ${eigen_version}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
)

INSTALL(CODE "MESSAGE(STATUS Installing.)")
