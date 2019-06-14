import sys
import random
from KNN import KNNFunc

arquivoTreino = open(sys.argv[1], 'r')
arquivoTeste = open(sys.argv[2], 'r')

Treino = arquivoTreino.read()
Teste = arquivoTeste.read()
amostras = []

def generate():
	for i in range(7):
		vec = []
		for j in range(132):
			vec.append(random.choice([0, 1]))
		amostras.append(vec)

def mutation(amostras, qntMut):
	for i in range(qntMut):
		iA = random.randrange(0,7,1)
		indMut = random.randrange(0,131,1)
		if(amostras[iA][indMut] == 0):
			amostras[iA][indMut] = 1
		else:
			amostras[iA][indMut] = 0
	return amostras

def selecao(amostras, qtdeAmostras):
	amostras.sort(key = lambda x : x[1], reverse = True)
	novaAmostra = []
	for i in range(qtdeAmostras):
		novaAmostra.append(amostras[i][0])

	random.shuffle(novaAmostra)
	return novaAmostra

def cruzamento(amostras, qtdeAmostras):
	novaAmostra = []
	for i in range(0, qtdeAmostras, 2):
		exemplo1 = amostras[i][0:(len(amostras[0])/2)] + amostras[i + 1][(len(amostras[0])/2) : len(amostras[0])]
		exemplo2 = amostras[i + 1][0:(len(amostras[0])/2)] + amostras[i][(len(amostras[0])/2) : len(amostras[0])]
		novaAmostra.append(exemplo1)
		novaAmostra.append(exemplo2)
	novaAmostra.append(amostras[0])
	return novaAmostra

generate()

breaker = 1
resultados = []
resultadoGeral = [-1, -1]
qtdeAg = 1
while(breaker):

# 	salva a amostra e o resultado da iteracao em uma posicao no "resultados"
#	Problema: nao esta salvando em tuplas 
	resultados = []
	for i in range(7):
		resultados.append(amostras[i])
		resultados[i] = [resultados[i], KNNFunc(Treino, Teste, amostras[i])]

	#	imprime os resultados
	resultados.sort(key = lambda x : x[1], reverse = True)
	for i in range(len(resultados)):
		if resultadoGeral[1] < resultados[i][1]:
			resultadoGeral = resultados[i]
		print("-----------------------------------------------------------")
		print(resultados[i])
		print("-----------------------------------------------------------")
	print("resultado geral = ", resultadoGeral, "iterancao numero", qtdeAg)
	print("-----------------------------------------------------------")
	amostras = selecao(resultados, 6)
	amostras = cruzamento(amostras, 6)
	amostras = mutation(amostras, 10)
	qtdeAg += 1
	if(resultadoGeral > 940 or qtdeAg > 200):
		breaker == 0
		
print("resultado geral", resultadoGeral)
print("Quantidade de iteracoes", qtdeAg)


