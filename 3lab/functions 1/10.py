def unique_elements(lst):
    unique_lst = []
    for elem in lst:
        if elem not in unique_lst:
            unique_lst.append(elem)
    return unique_lst
