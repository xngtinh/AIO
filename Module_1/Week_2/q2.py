def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)


string = 'Happiness'
count_chars(string)

string = 'smiles'
count_chars(string)
