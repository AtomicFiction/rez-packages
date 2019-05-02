name = "boost"

version = "1.55.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

private_build_requires = [
    #'~gcc-4.8.5',
    'clang-9.1.0',
    'python-2.7'
]



variants = [
    #["platform-linux", "arch-x86_64", "os-CentOS-7", "python-2.7"],
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13', 'python-2.7']
]

uuid = "boost"

