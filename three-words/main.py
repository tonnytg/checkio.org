def checkio(words):
    list = (words.split())
    seq = 0
    for word in list:
        if word.isdigit():
            if seq <= 2:
                seq = 0
        else:
            seq +=1
    if seq > 1:
        print(True)
    else:
        print(False)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("He is 123 man")
    checkio("one two 3 four five 6 seven eight ten eleven 1")