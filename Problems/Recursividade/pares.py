# N par 	->	0 2 4 6 ... N
# N ímpar 	->	0 2 4 6 ... N-1

def pares(N, crescente=True):
	""" Números pares de 0 até N """
	p = (N//2) * 2
	if p == 0:
		return [p]
	else:
		if crescente:
			return pares(p-2) + [p]
		else:
			return [p] + pares(p-2, crescente=False)
