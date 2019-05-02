name = 'python'

version = '2.7.10'

tools = ['python']

variants = [
    ['platform-osx', 'arch-x86_64', 'os-osx-10']
]

uuid = 'python'

build_command = '/usr/bin/true'

def commands():
    env.PATH.append('/usr/bin/python')

