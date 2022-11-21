import os
i=0
for arquivos in os.walk(f'{os.curdir}'):
    for arqs in arquivos[2]:
        print(arqs)
