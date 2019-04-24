
name = "ptex"

version = "2.1.28"

build_requires = [
    'gcc-4.8.5'
]

requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-7"]
]

uuid = "ptex"

def commands():
    env.PATH.append("{root}/bin")
    env.PTEX_LOCATION = '{root}'

