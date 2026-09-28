def caesar(text, shift, encrypt=True):
#  concept of encryption and decryption using the Caesar Cipher.
#  The `encrypt` function shifts the letters of the input text by a specified number
#  of positions in the alphabet.
#  while decryption this processed is reversed by shifting in the opposite direction.
# Demonstration : 
# say that we dont know what was the original letter but we have the encrypted from i.e 'i'
# now we are given that the shift while encrypting was +3.That means the original 
# letter was 3 alphabets left of 'i'
# we can come to a concluding expression that---
#  original letter = encrypted letter( i. 'i') - shift(3) = 'f'

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
        # the shift msut be between 1 and 25 because the alphabet has 26 letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        # case of decryption
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# encrypted_text = encrypt('freeCodeCamp', 3)
# print(encrypted_text)  # Output: iuhhFrghFdps

# decrypted_text = decrypt(encrypted_text, 3)
# print(decrypted_text)  # Output: freeCodeCamp

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)