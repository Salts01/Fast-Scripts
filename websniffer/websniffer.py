import requests

print("______Bem vindo o websniffer!_______")
print("-------------------------------------------------")
print("Não utilize essa ferramenta para fins maliciosos")
print("-------------------------------------------------")

url=input("digite a Url: ")
lista=input("digite a lista a ser usada: ")
with open(lista,'r') as words:
	ext=input("deseja ativar a extensão: ")
	if (ext=="sim"):
		ext=input("digite a extensão: ")
		for word in words:
			response=requests.get(url+'/'+word)
			if response.status_code==200:
				print("")
				print("-------------------------------")
				print("encontrado "+"/"+word)
				print("-------------------------------")
		for word in words:
			response=requests.get(url+'/'+word+"."+ext)
			if response.status_code==200:
				print("")
				print("-------------------------------")
				print("encontrado "+"/"+word+"."+ext)
				print("-------------------------------")
	else:
		for word in words:
			response=requests.get(url+'/'+word)
			if response.status_code==200:
				print("")
				print("-------------------------------")
				print("encontrado "+"/"+word)
				print("-------------------------------")
				