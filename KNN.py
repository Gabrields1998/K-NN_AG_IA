import sys

def KNNFunc(conjuntoTreino, conjuntoTeste, amostra):
	# arquivoTreino = open(sys.argv[1], 'r') #<------- Descomentar caso queira rodar apenas o K-NN
	# arquivoTeste = open(sys.argv[2], 'r') #<------- Descomentar caso queira rodar apenas o K-NN

	# Treino = arquivoTreino.read().split('\n') #<------- Descomentar caso queira rodar apenas o K-NN
	# Teste = arquivoTeste.read().split('\n') #<------- Descomentar caso queira rodar apenas o K-NN
	Treino = conjuntoTreino.split('\n') #<------- Comentar caso queira rodar apenas o K-NN
	Teste = conjuntoTeste.split('\n') #<------- Comentar caso queira rodar apenas o K-NN
	for i in range(len(Treino) -1):
		Treino[i] = Treino[i].split(' ')

	acertou = 0
	for i in range(len(Teste) -1): # itera por todos os testes
		Teste[i] = Teste[i].split(' ')
		# print(float(Teste[i][0]))
		distanciaEuclidiana = []
		for j in range(len(Treino) -1): # itera por todos os treinos
			result = 0
			classeTreino = -1
			for k in range(len(Treino[j])): # itera por todos os atributos do treino
				
				if((len(Treino[j]) -1) > k):
					if(amostra[k] == 1):
						result += (float(Teste[i][k]) - float(Treino[j][k]))**2
				else:
					classeTreino = int(Treino[j][k])
			sqrt = result ** (0.5)

			distanciaEuclidiana.append([sqrt,classeTreino])


		distanciaEuclidiana.sort(key = lambda x : x[0]) # ordena distancia euclidiana


		if (distanciaEuclidiana[0][1] == int(Teste[i][len(Teste[i]) - 1])):
			acertou += 1

	return acertou


# def main():
# 	print(sys.argv[1])
# 	print(sys.argv[2])                          #Vetor de caracteristicas, se quiser as 132 sete tudo como 1
# 	# vetorCaracteristicas = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1]
# 	vetorCaracteristicas = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 	taCerto = KNNFunc(sys.argv[1], sys.argv[2], vetorCaracteristicas)

# 	print('acertou', taCerto)

# main()