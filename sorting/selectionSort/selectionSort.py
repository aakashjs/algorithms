#selectionSort.py

def findIndexOfSmallest(L,i):
	""" (List, int) -> int
	returns the index of the smallest element in the L[i:]

	>>> findIndexOfSmallest([2, 7 ,3 ,5], 1)
	2
	"""	
	indexOfSmallest = i
	for j in range(i+1,len(L)):
		if L[j] < L[indexOfSmallest]:
			indexOfSmallest = j

	return indexOfSmallest


def selectionSort(L):
	""" (List) -> Nonetype
	Returns the list in non-descending order

	>>> L = [50, 23, 14, 5, 21, 100]
	>>> selectionSort(L)
	>>> L
	[5, 14, 21, 23, 50, 100]
	""" 	
	#find the index of the smallest element in the list
	for i in range(len(L)):
		indexOfSmallest = findIndexOfSmallest(L,i)
		L[i], L[indexOfSmallest] = L[indexOfSmallest], L[i]


if __name__ == '__main__':
	import doctest
	print doctest.testmod()