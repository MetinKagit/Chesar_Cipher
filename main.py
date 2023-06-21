import logo
import functions
import time

if __name__ == '__main__':
    finish_process = False
    time_sec = 5
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9']
    print(logo.logo)
    while finish_process is False:
        process = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        if process != "encode" and process != "decode":
            print("Please write a valid process!")
            exit()

        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        if process == "encode":
            functions.encrypt(alphabet,numbers, text, shift)
        elif process == "decode":
            functions.decrypt(alphabet,numbers, text, shift)

        temp = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

        if temp == 'yes':
            finish_process = False
        elif temp == 'no':
            finish_process = True
            print("Goodbye :)")
        else:
            print("Unvalid command, self-destruct process will start...\n ")
            time.sleep(3)
            print("Boom!")
            finish_process = True





