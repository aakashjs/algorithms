# cormenIntroToAlgoProblem1.1.py

#Qs: For each function f(n) and time t in the following table, 
#determine the largest size n of a problem that can be solved in time t, 
#assuming that the algorithm to solve the problem takes f(n) microseconds.
#f(n) = n!

# retruns n! for a given n
def factorial(n):
	if n<1:
		return 1
	else:
		return n*factorial(n-1)

#return maximum n for function f(n) for a given time t
def maxN(t):
	n = 1
	while factorial(n) <= t:
		n = n+1
		#print "n= ", n, "factorial(n) =", factorial(n)
		if factorial(n) >= t:			
			return n-1

def returnTime(optionNumber):
	if optionNumber == 1:
		#1 sec
		return 1000

	if optionNumber == 2:
		#1 min
		return 60*1000

	if optionNumber == 3:
		#1 hour		
		return 60*60*1000

	if optionNumber == 4:
		#1 day
		return 24*60*60*1000

	if optionNumber == 5:
		#1 month
		return 30*24*60*60*1000

	if optionNumber == 6:
		#1 year
		return 365*24*60*60*1000

	if optionNumber == 7:
		#1 day
		return 100*365*24*60*60*1000


def main():
	# select optionNumber 
	# 1 for 1 sec, 2 for 1 min, 3 for 1 hour 
	# 4 for 1 day, 5 for 1 month, 6 for 1 year, 7 for 1 century
	optionNumber = 7
	t = returnTime(optionNumber)
	maxSize = maxN(t)	
	print "max size of n can be: ", maxSize
	print "time limit                		   :", t, "microseconds"
	print "time taken by function for size 'n':", factorial(maxSize), "microseconds"
	print "time taken by next size   	       :", factorial(maxSize+1), "microseconds"

if __name__ == '__main__':
	main()