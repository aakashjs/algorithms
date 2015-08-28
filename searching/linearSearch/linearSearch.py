#linearSearch.py

def linearSearch(L, v):
	"""(list, int) -> int
	Returns the index of first occurance v in L
	else returns -1, if v, not in L
	
	>>> linearSearch([2, 3, 5, 3], 2)
	0
	>>> linearSearch([2, 3, 5, 3], 5)
	2
	>>> linearSearch([2, 3, 5, 3], 8)
	-1
	"""
	i = 0
	while i != len(L) and v != L[i]:
		i = i+1
	if i == len(L):
		return -1
	else:
		return i

def main():
	L = [2, 3, 5, 3]
	print linearSearch(L, 3)

if __name__ == '__main__':
	main()
	import doctest
	print doctest.testmod()