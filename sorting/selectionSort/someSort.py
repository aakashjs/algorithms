#selectionSort.py

def someSort(L):
	""" (List) -> Nonetype
	returns the sorted List

	>>> L = [50, 23, 14, 5, 21, 100]
	>>> someSort(L)
	>>> L
	[5, 14, 21, 23, 50, 100]
	"""
	i = 0
	while i < (len(L)):
		for j in range(len(L)):
			if L[i] < L[j]:
				L[i], L[j] = L[j], L[i]
		i+=1


if __name__ == '__main__':
	import doctest
	print doctest.testmod()
