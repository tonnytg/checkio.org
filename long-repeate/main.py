def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    X = line[0]
    for letter in line:
        X = letter

    return 0

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"