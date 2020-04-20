def checkio(words):
    list = (words.split())
    seq = 1
    for word in list:
        print(word)
        if word.isdigit():
            print("É digito:",word.isdigit())
            print("Valor:", seq)
            if seq <= 3:
                print("Zeramos")
                seq = 1
        else:
            seq +=1
    if seq > 2:
        print(True)
    else:
        print(False)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("He is 123 man")
    checkio("one two 3 four five 6 seven eight ten eleven 1")