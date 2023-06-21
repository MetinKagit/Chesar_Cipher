import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}'.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

def encrypt(alphabet,numbers, plain_text, shift_amount):
    cipher_text = ""

    for letter in plain_text:
        if letter.isspace():
            cipher_text += " "
        elif letter not in alphabet and letter not in numbers:
            cipher_text += letter
        else:
            if not letter.isdigit():
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                position = numbers.index(letter)
                new_position = position + shift_amount
                new_letter = numbers[new_position]
                cipher_text += new_letter
    print(f" The enctypted text is '{cipher_text}'")


def decrypt(alphabet,numbers, cipher_text, shift_amount):
    decoded_text = ""
    for letter in cipher_text:
        if letter.isspace():
            decoded_text += " "
        elif letter not in alphabet and letter not in numbers:
            decoded_text += letter
        else:
            if not letter.isdigit():
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                decoded_text += new_letter
            else:
                position = numbers.index(letter)
                new_position = position - shift_amount
                new_letter = numbers[new_position]
                decoded_text += new_letter
    print(f" The decrypted text is '{decoded_text}'")