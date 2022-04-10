def num_translate(in_en):
    dictionary_base = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return dictionary_base.get(in_en)


en = input("введите число до десяти на английском: ")
res = num_translate(en)
print(res)
