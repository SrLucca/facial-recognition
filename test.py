import os
i=0

ROOT_DIR = os.path.abspath(os.curdir)
os.chdir(fr'{ROOT_DIR}\img')
for arquivos in os.walk(f'{os.curdir}'):
    for arqs in arquivos[2]:
        print(arqs)
