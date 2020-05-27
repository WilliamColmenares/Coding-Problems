"""
Given an array of integers, return a new array such that each element at index i of the new array
 is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].

If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""

def product(elements):
	results = []
	for i in range(0, len(elements)):
		# Use slice to remove the current element in the list
		results.append(multiply(elements[0:i], elements[i+1:len(elements)]))
	return results

def multiply(lst1, lst2):
	# starting point will always be one for simplicity.
	product = 1
	for el in lst1:
		product *= el
	for el in lst2:
		product *= el

	return product

print(product([1, 2, 3, 4, 5]))