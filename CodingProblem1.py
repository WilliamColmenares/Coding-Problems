"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

from itertools import combinations

def addsUp(numbers, k):
	for i in combinations(numbers, 2):
		if sum(i) == k:
			return True
	return False


print(addsUp([10, 15, 3, 7], 24))