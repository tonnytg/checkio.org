def long_repeat(line):
    try:
        I = 0
        for x in range (0,len(line)):
            word = line[x+1]
            if word == line[x]:
                print(word)
                I = I + 1
        print(I)
    except IndexError:
        print(I)


if __name__ == '__main__':
    long_repeat('sdsffffse')# == 4, "First"