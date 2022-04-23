# vai do começo ao fim, salva o elemento key
# copia os maiores que ele para os respectivos índices seguintes
	# elemento j é copiado para j+1
	# j-- até 0, ou até achar menor que key
# coloca key à frente do primeiro que for menor que ele 
	# j será a posição do menor, que foi copiado -> j+1
	# assim, colamos key em j+1 (este, copiado para j+2)
# resultado =>
	# elementos à direita - maiores que key
	# elementos à esquerda - menores que key (ou inexistentes)
	# Logo, elementos até a posição inicial de key (i) estão ordenados


def insertion_sort(vetor):
	for i in range(1, len(vetor)):
		key = vetor[i]
		j = i - 1
		while j >= 0 and key < vetor[j]:
			vetor[j + 1] = vetor[j]
			j -= 1
		vetor[j + 1] = key
