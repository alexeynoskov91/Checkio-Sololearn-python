"""Challenge is to create a program that takes 3 inputs, a lower bound, an 
upper bound and the expression. Calculate the sum of that range based on 
the given expression and output the result.

For Example:
Input: 2 4 *2
Output: 18 (2*2 + 3*2 + 4*2)

Input: 1 5 %2
Output: 3 (1%2 + 2%2 + 3%2 + 4%2 + 5%2)

"""

x = input ()
y = input ()
z = input ()
numbers = [z[:1:], z[1::]]
sum = ""
for i in range (int(x), int(y)+1):
    sum = f'{str(sum)}+{i}{"".join(numbers)}'
print (f'{eval(sum)} ({sum[1::]})')
