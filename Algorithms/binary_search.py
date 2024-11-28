# Binary Search by Karpo
sorted_list = [1,2,3,4,5,6,7,8,9,10,12,15,17,18,19,25,63,70]
# sorted_list = [1,2,3]

def binary_search(l, value_to_find):
    left_side = 0
    right_side = len(l)
    temp = l[(left_side + right_side) // 2]

    while temp != value_to_find:
        # if the item's not in the list
        if left_side + 1 == right_side:
            return False

        # if the item is smaller than value_to_find expand left side
        if temp < value_to_find:
            left_side = (left_side + right_side) // 2
        # if the item is bigger than value_to_find expand right side
        else:
            right_side = (left_side + right_side) // 2

        # giving the temp var its new value
        temp = l[(left_side + right_side) // 2]

    # if the item is in the list
    return True

print(binary_search(sorted_list, 1))
