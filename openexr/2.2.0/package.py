name = "openexr"

version = "2.2.0"

authors = [
    "ILM"
]

description = \
    """
    ILM's high dynamic-range (HDR) image file format library.
    """

private_build_requires = [
    #"gcc-4.8.2+"
    'clang-9.1.0'
]

requires = [
    "ilmbase-2.2"
]

variants = [
    #["platform-linux", "arch-x86_64", "os-CentOS-7"]
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13']
]

tools = [
    "exrenvmap",
    "exrheader",
    "exrmakepreview",
    "exrmaketiled",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr"
]

uuid = "repository.openexr"

def commands():
    env.PATH.append("{root}/bin")

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.M4PATH.append('{root}/aclocal')

