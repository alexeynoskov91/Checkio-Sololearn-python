"""Challenge is to create a program to find all the integer values 
between 0 and n, which contain the digit d.
d is from the range 0 to 9.

For Example:
Input: n = 20, d = 5
Output: 5, 15

Input: n = 50, d = 2
Output: 2, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 42.

Bonus: You may extend the value of d to any integer value.
For Example:
Input: n = 300, d = 42
Output: 42, 142, 242.

"""

n = int(input())
d = input()
x = ''

for i in range (0, n):
    if d in str(i): 
            x = x + str(i) + ', '
            print(x[0:-2:]+'.')