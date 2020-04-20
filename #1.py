"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""

def func(val_, list_):
	return list(set([True for val2 in [ [val+i for i in list_] for val in list_ ] if val_ in val2 ]))

def main(list_ = [10, 2, 3, 7], val_ = 17):
	return func(val_, list_)

if __name__ == '__main__' : 
	print(main())
	
	
	