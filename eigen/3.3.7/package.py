name = "eigen"

version = "3.3.7"

authors = [
    "eigenteam"
]

description = \
    """
    Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.
    """

build_requires = [
    "gcc-4.8+<5",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "5d9a247d-7900-4830-a142-60ce1f730b98"

def commands():
    if building:
        env.CMAKE_MODULE_PATH.append('{this.root}/share/eigen3/cmake')
        env.PKG_CONFIG_PATH.append('{this.root}/share/pkgconfig')
