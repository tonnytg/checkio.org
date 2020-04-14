#time spend 4hs :(
#Antonio Thomacelli Gomes
#Problem - https://py.checkio.org/en/mission/sum-numbers/

def sum_numbers(text: str) -> int:
    print(type(text))
    print(text)
    numbers = 0
    for word in text.split():
        try:
            print(int(word))
            numbers = numbers + int(word)
        except ValueError as err:
            print("Texto puro")
    return(numbers)


if __name__ == '__main__':
    print(sum_numbers('Hi 12 and you 10'))