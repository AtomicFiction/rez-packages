name = "vtk"

version = "8.2.0"

authors = [
    "KitWare"
]

description = \
    """
    """

private_build_requires = [
    "gcc-4.8.3+",
    "cmake-3.3+",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "1cb4f0ec-3141-47b0-84d0-1886a63637a3"

#def commands():
    #if building:
        #env.CMAKE_MODULE_PATH.append('{this.root}/share/eigen3/cmake')
        #env.PKG_CONFIG_PATH.append('{this.root}/share/pkgconfig')
