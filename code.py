
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def menue():
    print("Press. 1 For Encryption.")
    print("Press. 2 For Decryption.")
    print("Press. 3 To exit")

def encrypt(orignal_text,shift):
    encrypted_text=" "
    for char in orignal_text:
        if char in alphabet:
            index_position=alphabet.index(char)
            encrypted_text+= alphabet[index_position+shift]
    print(encrypted_text)


def decrypt(orignal_text,shift):
    encrypted_text=" "
    for char in orignal_text:
        if char in alphabet:
            index_position=alphabet.index(char)
            
            encrypted_text+= alphabet[index_position-shift]
    print(encrypted_text)


def game():
        choice=0
        while choice!=3:
            menue()
            choice=int(input("Enter your choice: "))
            if choice==3:
                print("Exiting..")
                exit()
            user_input=input("Enter the string: ").lower()
            no_shifts=int(input("Enter the shift no you wanted: "))
            if choice==1:
                encrypt(user_input,no_shifts)
            elif choice==2:
                decrypt(user_input,no_shifts)
            else:
                print("Invalid choice")

game()
