"""Task: Given the password length as input, create a program that will 
generate a random password by using a set of characters. The length must 
be between 8 and 32 characters.
Bonus: Program will calculate the strength of a created password.
"""

import random
import string

len_password = int(input())
if len_password < 8 or len_password > 32:
    print ('Your password length must be >= 8 and <= 32')     
    raise ValueError

characters = [i for i in string.printable if i not in string.whitespace]
    
password = ''
while len(password) < len_password:
    password = password + random.choice(characters)
print (password)

if (len(password) > 11 and any(x in string.digits for x in password) 
        and any(x in string.punctuation for x in password)):
    print ("Your password is strong")
elif len(password) > 9 and any(x in string.digits for x in password):
    print("Your password is medium difficulty")
else:
    print("Your password is weak")


