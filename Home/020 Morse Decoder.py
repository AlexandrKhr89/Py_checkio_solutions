'''
Elementary+
English RU
Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them
and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

example

Input: The secret message.

Output: The decrypted text.

Example:

morse_decoder("... --- -- .   - . -..- -") == "Some text"
morse_decoder("..--- ----- .---- ---..") == "2018"
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

How it is used: For cryptography and spy work.

Precondition:
0 < len(message) < 100
The message will consists of numbers and English letters only.
'''

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    # replace this for solution
    print("\ncode:", code)
    message_words = code.split('   ')
    # print('message_words:', message_words)

    text_word_letter = []

    for word in message_words:
        # print('word:', word)
        word_letter = word.split(' ')

        text_word_letter.append(word_letter)
        # print('word_letter:', word_letter)
        # print('text_word_letter:', text_word_letter)

    message_code = []
    word_message_code = ''

    for word in text_word_letter:
        for letter in word:
            word_message_code += MORSE.get(letter)
        # print('word_message_code:', word_message_code)
        message_code.append(word_message_code)
        word_message_code = ''
        # print('message_code:', message_code)

    # print((' '.join(message_code)))
    if ' '.join(message_code)[0].isalpha():
        text = ' '.join(message_code).capitalize()
        # text = text.capitalize()
    else:
        text = ' '.join(message_code)

    print('text:', text)

    return text


if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
