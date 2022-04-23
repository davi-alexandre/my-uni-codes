# ordena cada posição, do fim ao começo, comparando maior-menor nos elementos que vão desde o começo até a posição à ordenar
# à cada comparação, o maior é levado à frente (se estava em i) XOU é deixado onde está (se estava em i+1)
# assim, o maior elemento encontrado até então vai sendo "carregado" até a posição à ordenar
# à cada laço de posicao, um elemento é ordenado


# for loops
def bubble_sort(vetor):
	for posicao in range(len(vetor)-1,0,-1):
		for i in range(posicao):
			if vetor[i] > vetor[i+1]:
				vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

# while loops
def bubble_sort(vetor):
	posicao = len(vetor) - 1
	while posicao > 0:
		i = 0
		while i < posicao:
			if vetor[i] > vetor[i+1]:
				vetor[i], vetor[i+1] = vetor[i+1], vetor[i]
			i += 1
		posicao -= 1
