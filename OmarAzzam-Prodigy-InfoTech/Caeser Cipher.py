def encrypt(text,shift):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text+=chr((ord(char)+shift - 97)%26 + 97)
    else:
        encrypted_text+=char

    return encrypted_text
originalmessage = "hello world"
encrypted_message= encrypt(originalmessage,3)
print(encrypted_message)

def decrypt(text,shift):
    text = text.lower()
    decrypted_text=""
    originalmessage = "hello world"
    for char in text:
        if char.islower():
            decrypted_text+=chr((ord(char)-shift - 97)%26 + 97)
        else:
            decrypted_text +=char
            return decrypted_text
