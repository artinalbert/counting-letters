
# why should we define it as string?
def counter(sentence:str):
    counter_of_letters = {
        # 'a': 0,
        # 'b': 0,
    }
    for letter in ['a', 'b', 'c', 'd']:
        counter_of_letters[letter] = 0

    while len(sentence) != 0:
        for key in counter_of_letters.keys():
            if sentence[-1].lower() == key:
                counter_of_letters[key] += 1

        # if sentence[-1].lower() == 'a':
        #     counter_of_letters['a'] += 1
        # elif sentence[-1].lower() == 'b':
        #     # or sentence[-1] == 'B':
        #     counter_of_letters['b'] += 1
        sentence = sentence[:-1]

    for key, value in counter_of_letters.items():
        print(f'\n The Letter {key} was repeated {value} times. \n')

        # prints every letter in the opposite order
        # print(sentence[-1])


if __name__ == '__main__':
    sentence = input('Please enter something: \n\n')
    counter(sentence)
    print(sentence)


