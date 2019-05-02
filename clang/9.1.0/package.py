name = 'clang'

version = '9.1.0'

tools = ['python']

variants = [
    ['platform-osx', 'arch-x86_64', 'os-osx-10.13']
]

uuid = 'clang'

build_command = '/usr/bin/true'

def commands():
    env.PATH.append('/usr/bin/clang')

