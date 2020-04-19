def checkio(words):
    list = (words.split())
    status = True
    for word in list:
        try:
            print("Inteiro:",int(word))
            status = False
        except ValueError:
            if status != False:
                status = True
    print(status)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))
    checkio("Hello 31 hello")# == True, "Hello"
    checkio("Teste ola como vai")