#!/usr/bin/python

from itertools import islice


def highest_product_of_three(intArray):
    if len(intArray) < 3:
        print("3 or more numbers are require.")

    highest = max(intArray[0], intArray[1])
    lowest = min(intArray[0], intArray[1])

    highest_product_of_2 = intArray[0] * intArray[1]
    lowest_product_of_2 = intArray[0] * intArray[1]
    highest_product_of_3 = intArray[0] * intArray[1] * intArray[2]

    # for i in range(len(intArray)):
    #     current = intArray[i]
    for current in islice(intArray, 2, None):
        highest_product_of_3 = max(max(highest_product_of_3, current * highest_product_of_2), current * lowest_product_of_2)
        highest_product_of_2 = max(max(highest_product_of_2, current * highest), current * lowest)
        lowest_product_of_2 = min(min(lowest_product_of_2, current * highest), current * lowest)
        # highest_product_of_3 = max(highest_product_of_3, current * highest_product_of_2,
        #                            current * lowest_product_of_2)
        # highest_product_of_2 = max(highest_product_of_2, current * highest, current * lowest)
        # lowest_product_of_2 = min(lowest_product_of_2, current * highest, current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)
    return highest_product_of_3


a_list = [1, 3, 7, -9, -10]
print(highest_product_of_three(a_list))
