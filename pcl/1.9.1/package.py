name = "pcl"

version = "1.9.1"

authors = [
    ""
]

description = \
    """
    """

private_build_requires = [
    "gcc-4.8+<5",
    "cmake-3.1+<4",
    "flann-1.9.1",
    "vtk-5.6+<9",
]

requires = [
    "boost-1.55",
    "eigen-3",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "c867cfe7-52b2-4883-afbb-363ee2292eda"

def commands():
    env.PATH.append('{this.root}/bin')
    env.CMAKE_MODULE_PATH.append('{this.root}/share/pcl-1.9')

