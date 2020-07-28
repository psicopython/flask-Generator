import os
import shutil
from time import sleep
from app import *

try:
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("""\033[36mQUAL TIPO DE APP:
-----------------
\033[32m[ 1 ] APP Padrão\n[ X ] Cancelar\033[m""")
		opt = input('$ ')
		if opt.upper() == 'X':
			break
		elif opt.isdigit():
			opt = int(opt)
			if opt == 1:
				appc()
				break
		else:
			erro = True
			continue

except KeyboardInterrupt:
	print('\n\033[31mOperação Abortada pelo usuário!\033[m')
except EOFError:
	print('\n\n\033[31mOperação Abortada pelo usuário!\033[m')


