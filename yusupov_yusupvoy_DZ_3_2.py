def num_translate_adv(in_en):
    is_lower = in_en.islower()

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
    if is_lower:
        result = dictionary_base.get(in_en)
    else:
        in_en = in_en.lower()
        result = dictionary_base.get(in_en)
        if result:
            result = result.title()
    return result


en = input("введите число до десяти на английском: ")
res = num_translate_adv(en)
print(res)
