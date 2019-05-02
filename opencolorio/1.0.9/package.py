name = "opencolorio"

version = "1.0.9"

authors = [
    "Sony Imageworks"
]

description = \
    """
    OpenColorIO Color Management Framework
    """

private_build_requires = [
    #"gcc-4.8.5",
    'clang-9.1.0'
]

requires = [
    "python-2.7",
    'boost-1.55.0'
]

variants = [
    #["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"],
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13', 'python-2.7']
]

tools = [
    "ociobacklut",
    "ociocheck"
]

uuid = "opencolorio"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')

    if building:
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')

