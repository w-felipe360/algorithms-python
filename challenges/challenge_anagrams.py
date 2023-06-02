def ordenar_rapido(param):
    if len(param) <= 1:
        return param

    pivot_value = param[len(param) // 2]
    menor, igual, maior = [], [], []

    for index in param:
        if index < pivot_value:
            menor.append(index)
        elif index == pivot_value:
            igual.append(index)
        else:
            maior.append(index)

    return ordenar_rapido(menor) + igual + ordenar_rapido(maior)


def is_anagram(first_string, second_string):
    first = ''.join(ordenar_rapido(list(first_string.lower())))
    second = ''.join(ordenar_rapido(list(second_string.lower())))

    if len(first) == 0 or len(second) == 0:
        return (first, second, False)

    return (first, second, first == second)
