import os

dirs = ['.', '.vscode', 'bin', 'doc', 'lib', 'inc', 'src', 'tmp']

for d in dirs: 
    try: os.mkdir(d)
    except FileExistsError: pass
    with open(f'{d}/.gitignore','w') as giti: print('!.gitignore',file=giti)

files = ['README.md','LICENSE','Makefile','apt.Debian','.clang-format','.doxygen']

for f in files:
    with open(f,'a') as ff: pass
