import sys
import dns.resolver

argumentos = sys.argv # le os argumentos do comando
try:
	dominio = argumentos[1]
	lista = argumentos[2]
except:
	print("faltam argumentos no comando")
	sys.exit(1)

# abre wordlist
try:
	arquivo = open(lista)
	linhas = arquivo.read().splitlines()
except:
	print("arquivo nao encontrado ou invalido")
	sys.exit(1)

# para cada linha de wordlist testa o dns
for linha in linhas:
	subdominio = linha + '.site.com.br'
	try:
		respostas = dns.resolver.query(subdominio, 'a')
		for resultado in respostas:
			print subdominio, resultado
	except:
		pass
