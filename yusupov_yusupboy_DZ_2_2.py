some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
res_str = ''
for ind, element in enumerate(some_list):

    if element.isdigit() or element.replace('+', '').isdigit() or element.replace('-', '').isdigit():
        res_str += '"'
        if len(element) == 1:
            element = element.zfill(2)
        elif len(element.replace('+', '')) == 1 or len(element.replace('-', '')) == 1:
            element = element[0:1] + element[1:].zfill(2)
        res_str += element
        res_str += '"'
    else:
        res_str += element
    res_str += ' '
res_str = res_str[0:len(res_str)-1]
print(res_str)
