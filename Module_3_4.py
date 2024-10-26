def single_root_words(root_word, *other_words): #Объявление функции "single_root_words" с параметрами "root_word", "*other_words"
    same_words = [] #Создание пустого списка "same_words"
    for i in other_words: #Цикл for для перебора предполагаемого подходящего слова среди *произвольного числа параметров "other_words"
        if root_word.lower() in i.lower() or i.lower() in root_word.lower(): #Условие, при котором добавляются слова в результирующий список "same_words"
            same_words.append(i)
    return same_words #Возвращение образованного функцией списка "same_words"
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
