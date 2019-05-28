CMAKE_MINIMUM_REQUIRED(VERSION 3.3)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(vtk_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_vtk vtk/VTK-${vtk_version}.tar.gz
    https://github.com/Kitware/VTK/tree/v${vtk_version}
)

ExternalProject_add(
    vtk
    PREFIX vtk
    URL ${url_vtk}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
)

INSTALL(CODE "MESSAGE(STATUS Installing.)")
