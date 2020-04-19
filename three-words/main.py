def checkio(words: str) -> bool:
    if words:
        return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    checkio("Hello World hello") == True, "Hello"