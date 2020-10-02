"""In this mission your task is to determine the popularity of certain words 
in the text. At the input of your function are given 2 arguments: the text 
and the array of words the popularity of which you need to determine.
When solving this task pay attention to the following points:
The words should be sought in all registers. This means that if you need to 
find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary 
with 0 (zero) value.
Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are 
the number of times when those words are occurring in a given text.
Precondition:
The input text will consists of English letters in uppercase and lowercase 
and whitespaces.

"""

import re
def popular_words(text: str, words: list) -> dict:
    pop_words = {}
    for i in words:
        count = (len(re.findall(r'\b' + i + r'(?!\w)', text, 
            flags=re.IGNORECASE))) 
        pop_words[i] = count 
    print (pop_words)        
    return pop_words
        
if __name__ == '__main__':
    print("Example:")

    assert (popular_words('When I was One I had just begun When I was Two \
        I was nearly new', 
        ['i', 'was', 'three', 'near']) == 
        {'i': 4, 'was': 3, 'three': 0, 'near': 0})
    assert popular_words("\nWhen I was One\nI had just begun\nWhen I was \
        Two\nI was nearly new\n",
        ["one","two","three"]) == {'one': 1, 'two': 1, 'three': 0}
    assert popular_words("It's flying from somewhere\nAs fast as it can\nI \
        couldn't keep up with it\nNot if I ran",
        ["it's","ran","i"]) == {"it's": 1, 'ran': 1, 'i': 2}  
    assert (popular_words("And the Raven never flitting still is sitting \
        still is sitting\nOn the pallid bust of Pallas just above my chamber \
        door\nAnd his eyes have all the seeming of a demon’s that is \
        dreaming\nAnd the lamp-light o’er him streaming throws his shadow \
        on the floor\nAnd my soul from out that shadow that lies floating \
        on the floor\nShall be lifted nevermore",
        ["raven","still","is","floor","nevermore"]) == 
        {'raven': 1, 'still': 2, 'is': 3, 'floor': 2, 'nevermore': 1} == 
        {'raven': 1, 'still': 2, 'is': 3, 'floor': 2, 'nevermore': 1})
    
    print("Coding complete")
                                                            