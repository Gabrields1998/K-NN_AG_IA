import sys

arquivoTreino = open(sys.argv[1], 'r')
arquivoTeste = open(sys.argv[2], 'r')

Treino = arquivoTreino.read().split('\n')
Teste = arquivoTeste.read().split('\n')

for i in range(len(Treino) -1):
	Treino[i] = Treino[i].split(' ')

for i in range(len(Teste) - 1): # itera por todos os testes
	Teste[i] = Teste[i].split(' ')
	# print(float(Teste[i][0]))
	distanciaEuclidiana = []
	for j in range(len(Treino) -1): # itera por todos os treinos
		result = 0
		classeTreino = -1
		for k in range(len(Treino[j])): # itera por todos os atributos do treino
			
			if((len(Treino[j]) -1) > k):
				result += (float(Teste[i][k]) - float(Treino[j][k]))**2
			else:
				print('treino = ', Treino[j][k])
				classeTreino = int(Treino[j][k])
		sqrt = result ** (0.5)
		distanciaEuclidiana.append([sqrt,classeTreino])


	print(distanciaEuclidiana[0])
	for m in range(len(distanciaEuclidiana) - 1 ): # ordena lista euclidiana
		for n in range(len(distanciaEuclidiana) - 1 ):
			if (distanciaEuclidiana[m][0] < distanciaEuclidiana[n][0]):
				aux = distanciaEuclidiana[m][0]
				distanciaEuclidiana[m][0] = distanciaEuclidiana[n][0]
				distanciaEuclidiana[n][0] = aux

	if (distanciaEuclidiana[0][1] == int(Teste[i][len(Teste[i]) - 1])):
		print("acertou classe = ", distanciaEuclidiana[0][1])
	else:
		print("errou classe = ", distanciaEuclidiana[0][1])