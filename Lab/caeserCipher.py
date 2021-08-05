def encrypt(text, s):
    result = ''
    for i in range(0, len(text)):
        # ENCRYPT UPPERCASE LETTERS
        if text[i].isupper():
            result += chr((ord(text[i])+s-65)%26+65)
        # ENCRYPT LOWERCASE LETTERS
        else:
            result += chr((ord(text[i])+s-97)%26+97)
    return result


if __name__ == "__main__":
    text = input("Enter the text: ").strip()
    shift = int(input("Enter the shift value: "))
    print(f'Cipher: {encrypt(text, shift)}')

