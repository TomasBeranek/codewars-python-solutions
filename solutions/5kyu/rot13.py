# ROT13 is a simple letter substitution cipher that replaces a letter with the
# letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should
# be returned as they are. Only letters from the latin/english alphabet should be
# shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def encode_char(c):
    if c.isalpha():
        a, z = (ord('a'), ord('z')) if c.islower() else (ord('A'), ord('Z'))
        c = chr(((ord(c) - a + 13) % (z - a + 1)) + a)

    return c


def rot13(message):
    encoded_message = [encode_char(c) for c in message]
    return ''.join(encoded_message)
