"""Challenge - you have a collection of numbers, where you want to find if 
there exists a pair whose sum is equal to the user's input.
For example, for the numbers [1, 2, 4, 4]:
Input: 8
Output: True
Input: 7
Output: False
Task is to write a program to solve the problem described.
This problem can be solved in different ways, where the time complexity 
could be quadratic O(n²), quasilinear O(n log n) or linear O(n). 
Try your best to solve it in a linear time O(n).

"""

x = input()
numbers = [1, 2, 3, 4, 4, 7, 7, 9, 11, 19, 19, 27, 36, 48, 57, 69, 79, 81, 
93, 99, 107, 113]

"O(n²) - Quadratic time"
def find_the_pair_qt(x):
    for i in numbers:
        for j in numbers:
            if i + j == x and i is not j:
                return True 
    return False 
    
    
print(find_the_pair_qt(int(x)))

"O(n) - Linear time"
def find_the_pair_lt(x):
    for i in numbers:
        if (int(x) - i) in numbers and (int(x) - i) is not i:
            return True 
    return False 
    
    
print(find_the_pair_lt(int(x)))