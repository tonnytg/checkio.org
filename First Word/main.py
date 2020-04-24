def first_word(text: str) -> str:
    if len(text.split()) > 1:
        word = list(text.split())
    else:
        word = list(text.split('.'))
    i = 0
    while i < len(text.split()):
        i +=1
        if word[i-1].replace('.','').replace(',',''):
            return(word[i-1].replace('.','').replace(',',''))
            break


if __name__ == '__main__':
    # print("Example:")
    # print(first_word("Hello world"))
    first_word(" ")
    # These "asserts" are used for self-checking and not for an auto-testing
    first_word("Hello world")# == "Hello"
    first_word(" a word ")# == "a"
    first_word("... and so on ...")
    first_word("hi")
    first_word("Hello.World")


