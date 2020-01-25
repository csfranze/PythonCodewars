#For building the encrypted string:
#Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
#Do this n times!

#Examples:

#"This is a test!", 1 -> "hsi  etTi sats!"
#"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
#Write two methods:

#def encrypt(text, n)
#def decrypt(encrypted_text, n)
#For both methods:
#If the input-string is null or empty return exactly this value!
#If n is <= 0 then return the input text.

def encrypt(text,n):
    if n <= 0:
        encrypted_text = text
    else:
        encrypted_text = text
        for i in range(n):
            encrypted_text = encrypted_text[1::2]+encrypted_text[0::2]
    return(encrypted_text)

def decrypt(text,n):
    if n <= 0:
        decrypted_text = text
    else:
        import math
        decrypted_text = text
        for i in range(n):
            first_half = decrypted_text[:math.floor(len(text)/2)]
            second_half = decrypted_text[math.floor(len(text)/2):]
            new_list = [0 for i in range(len(text))]
            new_text = ""
            for j in range(len(first_half)):
                new_list[2*j+1] = first_half[j]
            for j in range(len(second_half)):
                new_list[2*j] = second_half[j]
            decrypted_text = new_text.join(new_list)
    return(decrypted_text)
