def busca_binaria(vetor, e):
	""" o vetor deve estar ordenado """
	menor = 0
	maior = len(vetor) - 1
	while menor <= maior:
		meio = (menor + maior) // 2
		if vetor[meio] < e:
			# elemento na parte superior
			menor = meio + 1
		elif vetor[meio] > e:
			# elemento na parte inferior
			maior = meio - 1
		else:
			return meio
	return None
