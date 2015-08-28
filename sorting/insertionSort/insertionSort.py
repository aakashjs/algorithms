#insertionSort.py

def openFile():
	"""(file) -> List
	Opens up a file and returns the lines as a list of the numbers
	"""
	with open('numbers2.txt','r') as f:
		list1 = f.readlines()
		for index, value in enumerate(list1):
			list1[index] = int(value)

	return list1

def insert(L, i):
	"""(list, int) -> NoneType
	Precondition: L[:i] is sorted from smallest to largest
	Move L[i] to where it belong in L[:i+1]

	>>> L = [7, 3, 5, 2]
	>>> insert(L, 1)
	>>> L
	[3, 7, 5, 2]
	"""
	# the value to be inserted into the sorted part of the list
	value = L[i]
	# Find the index, j, where the value belongs
	# make room for the value by shifting
	j = i
	while j != 0 and L[j-1] > value:
		#shift L[j-1] on position to the right to L[j]
		L[j] = L[j-1]
		j = j-1

	#put the value where it belongs
	L[j] = value




def insertionSort(L):
	"""(list) -> NoneType
	Sort the items of L from smallest to largest
	>>> L = [7, 3, 5, 2]
	>>> insertionSort(L)
	[2, 3, 5, 7]
	"""
	for i in range(len(L)):
		insert(L, i)

	return L


def main():
	L = openFile()	
	list2 = insertionSort(L)
	for item in list2:
		print item

if __name__ == '__main__':
	main()