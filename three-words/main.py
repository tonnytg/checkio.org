def checkio(words):
    list = (words.split())
    seq = 0
    for word in list:
        try:
            if int(word):
                if seq <= 2:
                    seq = 1
        except ValueError:
            seq +=1
    if seq > 2:
        print(True)
    else:
        print(False)


#         try:
    #             print("Inteiro:",int(word))
    #             status = False
    #         except ValueError:
    #             if status != False:
    #                 status = True
    #                 seq = seq + 1
    # else:
    #     status = False
    # print(status)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))
    checkio("Hello World people 21 hello")
    checkio("He is 123 man")
    #checkio("Teste ola como vai")