def first_word(text: str) -> str:
    """
    When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.

        returns the first word in a given text.
    """
    print("Quantidade: %s" % len(text.split()))
    for i in range(0, len(text.split())):
        word = str(text.split()[i])
        # print("Valor bruto:", word)
        word = ''.join(word.replace(",", "").replace(".", ""))
        if word != '':
            print("Valor tratado:", word)
            break
    print("------" * 5)


if __name__ == '__main__':
    # print("Example:")
    # print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    first_word("Hello world") == "Hello"
    first_word(" a word ") == "a"


