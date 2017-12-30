# Objetivo é tratar todos os caracteres e numberos
# E depois contar as letras repetidas em ordem alfabetica, ignorando case sentive

def checkio(text):
    for letter in text :
        for char in " !?-,.":
           if char in text :
               text = text.replace(char, "" )
    text = ''.join(i for i in text if not i.isdigit())
    text = text.lower()
    value = sorted( text )
    value = ''.join(set(value))
    value = sorted ( value )
    winner = 0
    for letra in value :
        if winner < text.count ( letra ) :
             winner = text.count ( letra )
             l = letra
    return l
            
    #return 'a'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
