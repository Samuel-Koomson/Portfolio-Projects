"""
Morse code is an encoding system used in converting text to
specialised telegraphic codes

Identify the morse code and put them in a list or dictionary
map each code to a latin alphabet.
accept a string and convert it to morse code
"""

def morse_code_converter(strings):
        output_string = ""
        morse_codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
              '--', '-.', '---', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        mapped_data = dict(zip(morse_codes, alphabets))
        for string in strings:
            if string.upper() in alphabets:
                morse_code = morse_codes[alphabets.index(string.upper())]
                output_string += morse_code
        return output_string
print(morse_code_converter('ABA is a fine lady'))