"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3."""

list_positive_integer = [i for i in range(1,100)]

def find_first_missing_integer(list_input):
	if not list_input:
		return 1
	list_filter_on_positive_values = sorted([val for val in list_input if val > 0])
	for val,ref in zip(list_filter_on_positive_values,list_positive_integer):
		if val != ref :
			return ref
	return max(list_input) + 1
	
print(find_first_missing_integer([1, 2, 0]))