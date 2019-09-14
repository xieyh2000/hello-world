what1 = input("Please tell me what you want to do, encrypt or decrypt: ")
if what1=="encrypt":
    message = input("Please tell me which you want to encrypt: ")
    key = input("Please tell me the step(1-25): ")
    key = int(key)
    letters = list(message.lower())
    letters2 = []
    abcs = []
    for letter in letters:
        asc1 = ord(letter)
        if asc1 == 32 or asc1 == 44 or asc1 == 46:
            letters2.append(asc1)
        elif asc1 + key > 122:
            asc1 = asc1 + key - 26
            letters2.append(asc1)
        else:
            asc1 = asc1 + key
            letters2.append(asc1)
    for letter2 in letters2:
        abc = chr(letter2)
        abcs.append(abc)
    print(''.join(abcs))
elif what1=='decrypt':
    message = input("Please tell me which you want to decypt : ")
    key = input("Please tell me the step(1-25): ")
    key = int(key)
    letters = list(message.lower())
    letters2 = []
    abcs = []
    for letter in letters:
        asc1 = ord(letter)
        if asc1 == 32 or asc1 ==44 or asc1 ==46:
            letters2.append(asc1)
        elif asc1 - key < 97:
            asc1 = asc1 - key + 26
            letters2.append(asc1)
        else:
            asc1 = asc1 - key
            letters2.append(asc1)
    for letter2 in letters2:
        abc = chr(letter2)
        abcs.append(abc)
    print(''.join(abcs))

