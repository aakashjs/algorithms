#binarySearch.py

def binarySearch(L,v):
	"""(list, int) -> int
	Returns the index of the first occurance of v,
	else returns -1 if v not in L
	>>> L = [2, 3, 5, 7]
	>>> binarySearch(L, 2)
	0
	>>> binarySearch(L, 5)
	2
	>>> binarySearch(L, 8)
	-1
	"""
	b = 0
	e = len(L) -1

	while b<=e:
		m = (b+e)//2
		if L[m]<v:
			b = m+1
		else:
			e = m-1

	if b == len(L) or L[b] != v:
		return -1
	else:
		return b


def main():
	L = [2, 3, 5, 6, 7, 9]
	v = 9
	print binarySearch(L, v)


if __name__ == '__main__':
	main()
	import doctest
	print doctest.testmod()