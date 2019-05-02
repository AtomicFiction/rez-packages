
name = "ptex"

version = "2.1.28"

private_build_requires = [
    #'gcc-4.8.5',
    'clang-9.1.0'
]

requires = [
]

variants = [
    #["platform-linux", "arch-x86_64", "os-CentOS-7"],
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13']
]

uuid = "ptex"

def commands():
    env.PATH.append("{root}/bin")
    env.PTEX_LOCATION = '{root}'

