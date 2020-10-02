"""Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space 
between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this 
letter in uppercase.
Input: The secret message.
Output: The decrypted text.

"""

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    secret_message = code.split(" ")
    message = ""
    for i in secret_message:
        if i == " ":
            message += i 
        elif i == "":     
            message += " "
        else:     
            message += MORSE[i]
    message1 = message.replace("  ", " ")
    message2 = message1.capitalize()
    print (message2)
    return message2

if __name__ == '__main__':
    print("Example:")

    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert (morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") 
        == "It was a good day")
    print("Coding complete")
