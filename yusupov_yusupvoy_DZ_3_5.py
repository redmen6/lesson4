from random import choice, randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def choise_item(list_in, listout_tmp):
    res = choice(list_in)
    if ' ' + res + ' ' not in str(listout_tmp):
        return res
    else:
        return False


def get_jokes(count, flag=False):
    list_out = []
    num = 0
    while num < count:
        num += 1

        noun = nouns[(randint(0, len(nouns))) - 1]
        adverb = adverbs[(randint(0, len(adverbs))) - 1]
        adjective = adjectives[(randint(0, len(adjectives))) - 1]
        list_out.append(f'{noun} {adverb} {adjective}')
    if flag:
        list_out = []
        num = 0

        while num < count:
            if num >= len(nouns) or num >= len(nouns) or num >= len(nouns):
                break
            noun = None
            adverb = None
            adjective = None
            while not noun:
                noun = choise_item(nouns, list_out)
            while not adverb:
                adverb = choise_item(adverbs, list_out)
            while not adjective:
                adjective = choise_item(adjectives, list_out)

            list_out.append(f'{noun} {adverb} {adjective}')
            num += 1

    return list_out


print(get_jokes(10))
print(get_jokes(10, True))
