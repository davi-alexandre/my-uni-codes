def selection_sort(elementos):
	"""
	Compara-se os elementos não ordenados para encontrar o index do menor
	Depois, faz a troca da posição com o primeiro não ordenado
	"""
	tamanho = len(elementos)
	for item in range(tamanho):
		# todos os indices anteriores à *item* já estarão absolutamente ordenados
		menor = item

		for i in range(item + 1, tamanho):
			if elementos[i] < elementos[menor]:
				menor = i

		elementos[item], elementos[menor] = elementos[menor], elementos[item]
