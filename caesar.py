import string
def alphabet_position(letter):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    if letter.isupper():
        return upper.find(letter)
    else:
        return lower.find(letter)
def rotate_character(char, rot):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    if char.isalpha():
        if char.isupper():
            upnum = (alphabet_position(char) + rot) % 26
            return upper[upnum]
        else:
            lownum = (alphabet_position(char) + rot) % 26
            return lower[lownum]
    return char
def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            if char.isalpha():
                encrypted = encrypted + rotate_character(char, int(rot))
            else:
                encrypted = encrypted + char
    return encrypted
