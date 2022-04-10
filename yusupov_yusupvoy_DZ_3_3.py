def thesaurus(*args):
    dict_out = {}
    argsa = [*args]
    argsa.sort()

    for item in argsa:
        key_dict = item[0]
        if key_dict in dict_out:
            dict_out[key_dict].append(item)
        else:
            dict_out[key_dict] = [item]
    return dict(sorted(dict_out.items()))


print(thesaurus("Мая", "Иван", "Мария", "Петр", "Илья"))
