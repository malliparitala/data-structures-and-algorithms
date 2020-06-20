def sum_of_multiples_of_a_and_b():
    n = int(input("Enter the number you want to find sum of multiples of a and b under(default is 1000):") or '1000')
    a = int(input("Enter number a(default is 3):") or '3')
    b = int(input("Enter number b(default is 5):") or '5')
    sum = 0
    for x in range(n):
        if ((x%a == 0) or (x%b == 0)):
            sum = sum + x
    print("Sum of all the multiples of " , a , "or " , b  , " below " , n , " is:" , sum)

sum_of_multiples_of_a_and_b()
