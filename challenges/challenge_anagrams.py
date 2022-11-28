def partition(string, start, end):
    value = string[end]
    prox = start - 1
    for index in range(start, end):
        if string[index] <= value:
            prox = prox + 1
            string[index], string[prox] = string[prox], string[index]
    string[prox + 1], string[end] = string[end], string[prox + 1]
    return prox + 1


def sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        sort(string, start, p - 1)
        sort(string, p + 1, end)
    return string


def is_anagram(first_string, second_string):
    if (first_string == '' or second_string == ''):
        return (first_string, second_string, False)
    item1 = list(first_string.lower())
    item2 = list(second_string.lower())
    item1_sort = sort(item1, 0, len(item1) - 1)
    item2_sort = sort(item2, 0, len(item2) - 1)
    return (''.join(item1_sort), ''.join(item2_sort), item1_sort == item2_sort)
