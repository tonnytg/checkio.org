def replace(phrase):
    list = phrase.split()
    new_word = 'left'
    old_word = 'right'

    for word in list:
        print(word.replace(old_word,new_word))


if __name__ == '__main__':
    replace("Hello,baby,aright, wright")