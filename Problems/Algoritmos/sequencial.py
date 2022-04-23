def busca_sequencial(vetor, e, ordenado=False):
	for i in range(len(vetor)):
		if vetor[i] == e:
			return i
		if ordenado and vetor[i] > e:
			break
	return None
