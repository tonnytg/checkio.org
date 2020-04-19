def long_repeat(line):
    try:
        if line == "":
            print(0)
        numb = 1
        num_old = 1
        num_new = 1
        for I in range (len(line)):
            J = I + 1
            if line[I] == line[J]:
                num_new = num_new + 1
            else:
                num_new = 1
            if num_new > num_old:
                num_old = num_new
        print(num_old)
    except IndexError:
        print(num_old)


if __name__ == '__main__':
    long_repeat('sdsffffse')
    long_repeat('ddvvrwwwrggg')
    #long_repeat('abababaab')