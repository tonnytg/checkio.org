def checkio(words):
    list = (words.split())
    seq = 1
    for word in list:
        try:
            if int(word):
                print("Inteiro")
                if seq <= 2:
                    seq = 1
        except ValueError:
            print("String")
            seq +=1
    if seq >= 3:
        return(True)
    else
        return(False)


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
    checkio("Hello World 21 hello")
    #checkio("Teste ola como vai")