def split_list(items: list) -> list:
    print (items[:len(items) // 2], items[len(items) // 2 :])
    # list = []
    # if len(items) / 2 > 2:
    #     j = 3
    # else:
    #     j = 2
    #
    # list.append(items[:j])
    # list.append(items[j:len(items)])
    # print(list)
    #num_list = []
    #I = 0;
    #for i in 0,1:
    #     print("Começando rodada: %i" %i)
    #     num_list.append([])
    #     while I <= 2:
    #     print("Valor da lista agora é: %s" % num_list)
    #
    #     for number in items:
    #         num_list[i].append(number)
    #         num_list[i].append(items)
    #         I += 1
    #
    # print(num_list)


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    split_list([1, 2, 3, 4, 5, 6]) #== [[1, 2, 3], [4, 5, 6]]
    split_list([1, 2, 3, 4, 5])  # == [[1, 2, 3], [4, 5] ]
    split_list([1,2,3])
    split_list([])