import os
import shutil


erro = False
while True:
	if erro:
		print("\033[31mNome do pacote ja existe!\033[m")
		erro = False
	pkg = input("nome do package: ")
	if not os.path.exists(pkg):
		dados ={"c":"c.py",
			"m":"db.py","v":"vw.py",
			"i":"init.py"}
		dados2={"c":"cl.py",
			"m":"dbl.py","v":"vwl.py"}
		
		
		arq = {"c":"config.py",
			"i":"__init__.py","m":"model.py",
			"v":"views.py"
			}
		
		pas = {"c":"config",
			"m":"model","s":"static",
			"t":"templates","v":"views"}
		
		for c,v in dados.items():
			with open(f"GerarApp/{v}","r") as i:
				dados[c] = i.read()
		
		for c,v in dados2.items():
			with open(f"GerarApp/{v}","r") as i:
				dados2[c] = i.read()
		
		os.mkdir(pkg)
		os.mkdir(pkg+"/app")
		os.system(f"""
			echo "export FLASK_APP=app.app:create_app\nexport FLASK_ENV=development" > {pkg}/.env
			echo "{dados['i']}" > {pkg}/app/app.py
			echo "" > {pkg}/app/{arq['i']}
		""")
		for i,v in pas.items():
			if i == "s":
				os.mkdir(f"{pkg}/app/{v}")
				os.mkdir(f"{pkg}/app/{v}/js")
				os.mkdir(f"{pkg}/app/{v}/css")
			elif i == "t":
				os.mkdir(f"{pkg}/app/{v}")
			else:
				os.mkdir(f"{pkg}/app/{v}")
				os.system(f"echo '{dados[i]}' > {pkg}/app/{v}/{arq['i']}")
				os.system(f"echo '{dados2[i]}' > {pkg}/app/{v}/{arq[i]}")
        
		print(f"\033[32mAplicação FLASK criada com sucesso!\033[m")
		break
	else:
		erro = True
		continue