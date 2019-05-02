name = 'libjpeg'

version = '9c'

private_build_requires = [
    #'gcc-4.8.5',
    'clang-9.1.0'
]

variants = [
    #['platform-linux', 'arch-x86_64', 'os-CentOS-7'],
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13']
]

uuid = 'libjpeg'

def commands():
    env.PATH.append('{this.root}/bin')

