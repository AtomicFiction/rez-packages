name = 'qt'

version = '5.6.3'

authors = [
    'The Qt Company <https://www.qt.io/>',
    'Qt Project <https://www.qt.io/>',
]

description = \
    '''
    Qt is a cross-platform application framework that is used for developing
    application software that can be run on various software and hardware platforms
    with little or no change in the underlying codebase, while still being a native
    application with native capabilities and speed.
    '''

# private_build_requires = [
#     'cmake-3.1+'
# ]

build_requires = [
    'gcc-4.8.2+'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-CentOS-7']
]

uuid = 'repository.qt'

def commands():
    env.PATH.append('{root}/bin')

    if building:
        env.CPATH.append('{root}/include')
        env.PKG_CONFIG_PATH.append('{root}/lib/pkgconfig')
        env.LD_LIBRARY_PATH.append('{root}/lib')

