def merge(A, B) -> "sorted C, if A and B are sorted":
	C = []
	# Compare A and B while none is empty
	# => C is ordered to the smallest length between A and B
	while A and B:
		if A[0] > B[0]:
			C.append(B.pop(0))
		else:
			C.append(A.pop(0))
	# up to now, either A or B is empty
	# => append remaining elements (which should be sorted relative to C)
	while A: C.append(A.pop(0))
	while B: C.append(B.pop(0))
	return C

def mergesort(A):
	"""
		1 - Breaks the list in half recursively to the single element lists
		2 - Sort the first elements of the list pairs into a merged list
		3 - Recursively merges to the original list
	"""
	n = len(A)
	if n <= 1: return A
	B = A[:n//2]
	C = A[n//2:]
	B = mergesort(B)
	C = mergesort(C)
	print(B, C)
	return merge(B, C)