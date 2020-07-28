import os
from time import sleep

def appc():
	erro = False
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		if erro:
			print("\n\n\033[31mNome do pacote ja existe!\033[m\n")
			erro = False
		pkg = input("nome do package: ")
		if not os.path.exists(pkg):
			dados ={
				"c":"cod/c.py",
				"m":"cod/db.py",
				"v":"cod/vw.py",
				"i":"cod/init.py",
				"re":'requirements.txt',
				"bhtml":"html/base.html",
				"inhtml":"html/index.html"
				}
			dados2={
				"c":"cod/cl.py",
				"m":"cod/dbl.py",
				"v":"cod/vwl.py"
				}
			
			
			arq = {
				"c":"config.py",
				"i":"__init__.py",
				"m":"model.py",
				"v":"views.py"
				}
			
			pas = {
				"c":"config",
				"m":"model","s":"static",
				"t":"templates","v":"views"}
			
			
			for c,v in dados.items():
				with open(f"GerarApp/base/{v}","r") as i:
					dados[c] = i.read()
			
			for c,v in dados2.items():
				with open(f"GerarApp/base/{v}","r") as i:
					dados2[c] = i.read().replace('€|€',pkg.upper())
			
			
			
			os.mkdir(pkg)
			os.mkdir(pkg+"/app")
			os.system(f"""
				echo "export FLASK_APP=app.app:create_app\nexport FLASK_ENV=development" > {pkg}/.env
				echo "{dados['i']}  " > {pkg}/app/app.py
				echo "{dados['re']} " > {pkg}/requirements.txt
				echo "" > {pkg}/app/{arq['i']}
				""")
			for i,v in pas.items():
				if i == "s":
					os.mkdir(f"{pkg}/app/{v}")
					os.mkdir(f"{pkg}/app/{v}/js")
					os.mkdir(f"{pkg}/app/{v}/css")
					os.system(f"echo '' >{pkg}/app/{v}/js/custom.js")
					os.system(f"echo '' >{pkg}/app/{v}/css/custom.css")
					
				elif i == "t":
					os.mkdir(f"{pkg}/app/{v}")
					os.system(f"echo '{dados['bhtml']}'  > {pkg}/app/{v}/base.html")
					os.system(f"echo '{dados['inhtml']}' > {pkg}/app/{v}/index.html")
				else:
					os.mkdir(f"{pkg}/app/{v}")
					os.system(f"echo '{dados[i]}' > {pkg}/app/{v}/{arq['i']}")
					os.system(f"echo '{dados2[i]}' > {pkg}/app/{v}/{arq[i]}")
			

			os.system('cls' if os.name == 'nt' else 'clear')
			print(f"\n\033[32mAplicação FLASK criada com sucesso!\033[m\n")
			break