#!/usr/bin/env python3.5 

lst=[1,2,4,6,9,0,12,14]
def count_evens(lst):
	counter = 0
	for n in lst:
		if ((n % 2) == 0):
			counter += 1
	return counter
counter=count_evens(lst)
print (counter)
