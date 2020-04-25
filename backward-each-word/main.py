def backward_string_by_word(text: str) -> str:
    #https://py.checkio.org/mission/backward-each-word
    # your code here
    # word = ''
    # print((len(text) - 1)
    # for i in range((len(text)), -1, -1):
    #     word = word + (text[i])
    # print(word)
    letters = ''
    for word in text.split():
        for i in range((len(word)-1),-1,-1):
            letters = letters + (word[i])
        letters = letters + ' '
    print(letters)

if __name__ == '__main__':
    # print("Example:")
    # print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    #backward_string_by_word('abc')
    #backward_string_by_word('world') == 'dlrow'
    backward_string_by_word('hello world') == 'olleh dlrow'
    #backward_string_by_word('hello   world') == 'olleh   dlrow'
    #backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    # print("Coding complete? Click 'Check' to earn cool rewards!")