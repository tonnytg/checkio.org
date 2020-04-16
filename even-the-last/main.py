def checkio(array: list) -> int:
    try:
        num_list = []

        for X in range (0,len(array)) :
            if X % 2 == 0:
                 num_list.append(array[X])

        X = array[len(array)-1]
        Numb = 0;
        for I in num_list:
             Numb = Numb + I
        Numb = Numb * X
        return(Numb)
    except IndexError:
        return(0)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(checkio([1, 3, 5]))
    print(checkio([]))