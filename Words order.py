"""You have a text and a list of words. You need to check if the words in a 
list appear in the same order as in the given text.
Cases you should expect while solving this challenge:
- a word from the list is not in the text - your function should return False;
- any word can appear more than once in a text - use only the first one;
- two words in the given list are the same - your function should return False;
- the condition is case sensitive, which means 'hi' and 'Hi' are two different 
words;
- the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of 
words.
Output: A bool.

"""

def words_order(text: str, words: list) -> bool:
    text_split = text.split()
    try:
        if len(words)==1 and words[0] in text:
            return True 
        else:
            for i in range(len(words)-1):
                print(text_split.index(words[i]))
                if (text_split.index(words[i+1]) > text_split.index(words[i]) 
                    and words[i] in text): 
        #if text.find(words[i+1]) > text.find(words[i]) or (len(words)==1 and i in text):
                    print(text.find(words[i]))  
                else:    
                    return False
            if len(words)==1 and not words[0] in text:
                return False
            else:      
                return True
    except ValueError:
        return False
        
if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    assert words_order("london in the capital of great britain",["London"]) == False
    print("Coding complete!")