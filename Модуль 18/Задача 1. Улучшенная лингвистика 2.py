words = input('Введите искомые слова: ').split()
text = input('Введите текст: ').split()
repetition_first_word = 0
repetition_second_word = 0
repetition_third_word = 0

for element in text:
    if element == words[0]:
        repetition_first_word += 1
    elif element == words[1]:
        repetition_second_word += 1
    elif element == words[2]:
        repetition_third_word += 1

repetition_list = [repetition_first_word, repetition_second_word, repetition_third_word]

for word in words:
    print('Cлово {word} встречается {repetition} раз.'.format(word=word, repetition=repetition_list[words.index(word)]))
