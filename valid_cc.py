def Validator(card):
    odd_num = []
    even_num = []
    even_num_2 = []
    for i in reversed(range(16)):
        if i % 2 != 0:
            odd_num.append(int(card[i]))
        elif i % 2 == 0:
            even_num.append(int(card[i]))
    first_part = sum(odd_num)
    for i in even_num:
        if i * 2 < 10:
            even_num_2.append(int(i*2))
        elif i * 2 > 10:
            even_num_2.append(int((i*2 - 9)))
    second_part = sum(even_num_2)
    total = first_part + second_part
    if total % 10 == 0:
        print(f'{card} is valid')
    else:
        print('not valid')
