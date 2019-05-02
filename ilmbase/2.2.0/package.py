name = "ilmbase"

version = "2.2.0"

authors = [
    "ILM"
]

description = \
    """
    Utility libraries from ILM used by OpenEXR.
    """

build_requires = [
    #"gcc-4.8.5",
    'clang-9.1.0'
]

variants = [
    #["platform-linux", "arch-x86_64", "os-CentOS-7"],
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13']
]

uuid = "ilmbase"

def commands():
    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
