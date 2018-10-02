def add(numb1, numb2):
    return numb1 + numb2

def add_and_print(numb1, numb2):
    print(numb1 + numb2)

total = add(5, 3)
print(total)


def intersection(first_word, second_word):
    result = []
    for x in first_word:
        if x in second_word:
            result.append(x)
    return result

word1 = "spammsms"
word2 = "scammmmm"
char_of_intersect = intersection(word1, word2)
print(char_of_intersect) # ['s', 'a', 'm']

print("lalala".center(40, " "))