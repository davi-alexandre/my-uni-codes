def recursive_quicksort(A, start, end):
	""" Recursive implementation with in-place changes """
	def swap(i, j):
		A[i], A[j] = A[j], A[i]
	if end - start <= 0:
		return
	else:
		pivot = end
		# index of the first biggest number (than pivot) from left to right
		left_bigger = start
		# index of the first smallest number (than pivot) from right to left
		right_smaller = end
		is_pivot_sorted = False
		while not is_pivot_sorted:
			while left_bigger < right_smaller and A[left_bigger] <= A[end]:
				left_bigger += 1
			while left_bigger < right_smaller and A[right_smaller] >= A[end]:
				right_smaller -= 1
			if left_bigger >= right_smaller:
				swap(pivot, left_bigger)
				pivot = left_bigger
				is_pivot_sorted = True
			else:
				swap(left_bigger, right_smaller)
		recursive_quicksort(A, start, pivot-1)
		recursive_quicksort(A, pivot + 1, end)

def iter_quicksort(A):
	""" Iterative implementation with in-place changes """
	def swap(i, j):
		A[i], A[j] = A[j], A[i]
	partitions = [(0, len(A)-1)]
	while True:
		if not partitions: break
		start, end = partitions.pop(0)
		i = j = start + 1
		while i <= end:
			if A[i] <= A[start]:
				swap(i, j)
				j += 1
			i += 1
		swap(start, j-1)
		sorted_index = j-1
		left_part = (start, sorted_index-1) if (sorted_index-1) - start > 0 else None
		right_part = (sorted_index+1, end) if end - (sorted_index+1) > 0 else None
		if left_part:
			partitions.append(left_part)
		if right_part:
			partitions.append(right_part)