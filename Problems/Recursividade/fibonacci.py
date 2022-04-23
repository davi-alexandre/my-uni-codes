# 0 1 1 2 3 5 8 13 21 ...

def fibonacci(n):
  """ Calcula n termos da sequência de Fibonacci """
	if n == 0:
		return []
	if n == 1:
		return [0]
	elif n == 2:
		return [0, 1]
	else:
		*inicio, x, y = fibonacci(n-1)
		return inicio + [x, y] + [x+y]
