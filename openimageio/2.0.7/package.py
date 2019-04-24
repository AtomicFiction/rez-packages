name = "openimageio"

version = "2.0.7"

authors = [
    "Larry Gritz"
]

description = \
    """
    OpenImageIO is a library for reading and writing images, and a bunch of
    related classes, utilities, and applications.
    """

build_requires = [
    'cmake-3.2.2+<4',
    "gcc-4.8.5"
]

requires = [
    'ptex-2.1.28+<3',
    'boost-1.55',
    "ilmbase-2.2",
    'openexr-2.2',
    'opencolorio-1.0.9',
    'python-2.7'
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"]
]

tools = [
    "iconvert",
    "idiff",
    "igrep",
    "iinfo",
    "maketx",
    "oiiotool"
]

uuid = "openimageio"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python/site-packages")
    env.OPENIMAGEIO_ROOT_DIR = "{root}"

    if building:
        env.CMAKE_MODULE_PATH.append('{root}/share/cmake/Modules')
