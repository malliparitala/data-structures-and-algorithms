Problem statement: Multples of 3(a) and 5(b):

	If we list all the natural numbers below 10(n) that are multiples of 3(a) or 5(b), we get 3, 5, 6 and 9. 
	The sum of these multiples is 23.

	Find the sum of all the multiples of a or b below n.

Algorithm:

	Step 1: sum = 0 and prompt for n, a and b with defaults of 1000, 3 and 5
		n is the maximum number under which you want to find multiples of a and b
		a is the first number to check if current number is multiple of a or not
		b is the second number to check if the current number is multiple of b or not
	Step 2: for x in  range 1 to n
			if x%a is 0 or x%b is 0
				sum is sum+x
	Step 3: print 'Sum of all the multiples of a or b below n is sum'

Test cases:

	what if user enters negative numbers for n or a or b ?
	what if user enters 0 for n or a or b ?
	What if user enters strings or non-numeric characters for n or a and b
	what if user doesn't provide natural numbers as input ? 
