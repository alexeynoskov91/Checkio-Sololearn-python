'''Run the programm and please enter your new password
A valid password is the one that conforms to the following rules:
 - Minimum length is 5;
 - Maximum length is 10;
 - Should contain at least one number;
 - Should contain at least one special character 
(such as !, @, #, $, %, ^, &, *, (, ), _, +, ect.);
 - Should not contain spaces.
 
'''

from string import punctuation

set2 = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

def Validator(user_password):
    if not len(user_password) > 5 and len(user_password) < 10:
        return f'Minimum length of your password should be 10 and maximum \
        length of your password should be 10'
    elif not  set(user_password).intersection(set(punctuation)) != set():
        return f'Your password should contain at least one of the special \
        symbols as !, @, #, $, %, ^, &, *, (, ), _, +, ect.'
    elif not set2.intersection(set(user_password)) != set():            
        return f'Your password should contain at least one number'
    elif any(i in " " for i in user_password):
        return f'Your password should not contain spaces'                
    else:
        return f'Your password is changed'                   


user_password = input("")
print(Validator(user_password))