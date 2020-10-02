"""Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by 
whitespaces (one space). The words contains only letters. 
You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains 
three words in succession.
Input: A string with words.
Output: The answer as a boolean.
Precondition: The input contains words and/or numbers. 
There are no mixed words (letters and digits combined).
0 < len(words) < 100

"""

def checkio(words):
    words_split = words.split(" ")
    try:
        for i in range (0, len(words_split)-1):
            if not words_split[i].isdigit():
                if not words_split[i+1].isdigit():
                    if not words_split[i+2].isdigit():
                        return True
                    else:
                        continue
                else:
                    continue        
            else:
                continue
        
        return False
    except IndexError:
        return False

if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert (checkio("one two 3 four five six 7 eight 9 ten eleven 12") 
    == True), "four five six"
    print("Coding complete")
