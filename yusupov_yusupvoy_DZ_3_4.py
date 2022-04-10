def thesaurus(*args):
    dict_out = {}
    dict_out_tmp = {}
    argsa = [*args]
    # argsa.sort()
    for item in argsa:
        key_dict = item.split()
        dict_out_tmp['first_name'] = key_dict[0]
        dict_out_tmp['last_name'] = key_dict[1]
        key_dict_l = key_dict[1][0]
        key_dict_f = key_dict[0][0]
        if key_dict_l not in dict_out:
            dict_out[key_dict_l] = {key_dict_f: [item]}
        else:
            if key_dict_f in dict_out[key_dict_l]:
                dict_out[key_dict_l][key_dict_f].append([item])
            else:
                dict_out[key_dict_l][key_dict_f] = [item]
    return dict(sorted(dict_out.items()))


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
