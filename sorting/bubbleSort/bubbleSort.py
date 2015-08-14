#bubbleSort.py

def bubbleSort(L):
	""" (list) -> NoneType
	sort the items of L from smallest to largest

	>>> L= [7, 3, 5, 2]
	>>> bubbleSort(L)
	>>> L
	[2, 3, 5, 7]
	"""
	# the index of the last unsorted item
	end = len(L) - 1

	#make several passes until end, reaches index 0
	while end != 0:

		#bubble once through the list to
		#move the largest item to the index end
		for i in range(end):
			#check the size of adjacent elements
			if L[i] > L[i+1]:
				#swap if left one is larger
				L[i],L[i+1] = L[i+1],L[i]				
		#sorted section grows by 1, hence end moves 1 left
		end = end -1


if __name__ == '__main__':
	import doctest
	doctest.testmod()