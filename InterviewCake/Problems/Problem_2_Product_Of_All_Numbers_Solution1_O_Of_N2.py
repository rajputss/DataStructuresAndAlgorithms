#!/usr/bin/python


def get_products_of_all_ints_except_at_index(int_list):

    # check the length of the list to raise index error
    if len(int_list) < 2:
        raise IndexError("List size is less than 2. Need at least 2 numbers.")

    # create a list to add to
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # for each integer calculate product of integer before the index
    # as long as index is less than length of input list
    # products of all ints except at that index equals product so far
    # then product so far equals product so far times input list at that index
    product_so_far = 1
    i = 0
    while i < len(int_list):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    # for each integer calculate product of integer after the index
    product_so_far = 1
    j = len(int_list) - 1
    while j >= 0:
        products_of_all_ints_except_at_index[j] *= product_so_far
        product_so_far *= int_list[j]
        j -= 1

    return products_of_all_ints_except_at_index

a_list = [1, 7, 3, 4]
print(get_products_of_all_ints_except_at_index(a_list))
