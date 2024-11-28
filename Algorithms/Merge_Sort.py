# Merge Sort by Karpo
unsorted_list = [2,8,5,3,9,4,1,7]

def merge_sort(lst_to_sort):
    # if the list is sorted return
    if len(lst_to_sort) <= 1:
        return

    # first_half is the left half of the list and second_half is the right half of the list
    first_half = lst_to_sort[: len(lst_to_sort) // 2]
    second_half = lst_to_sort[len(lst_to_sort) // 2:]

    # sorting the two halves
    merge_sort(first_half)
    merge_sort(second_half)

    first_half_index = 0
    second_half_index = 0
    main_index = 0

    while first_half_index < len(first_half) and second_half_index < len(second_half):
        # checking first half
        if first_half[first_half_index] < second_half[second_half_index]:
            lst_to_sort[main_index] = first_half[first_half_index]
            first_half_index += 1

        # second half
        else:
            lst_to_sort[main_index] = second_half[second_half_index]
            second_half_index += 1

        main_index += 1

    while first_half_index < len(first_half):
        lst_to_sort[main_index] = first_half[first_half_index]
        first_half_index += 1
        main_index += 1

    while second_half_index < len(second_half):
        lst_to_sort[main_index] = second_half[second_half_index]
        second_half_index += 1
        main_index += 1

if __name__ == '__main__':

    merge_sort(unsorted_list)
    print(unsorted_list)

    # lst = [1,2,3,4]
    # print(lst)
    #
    # left = lst[:len(lst) // 2]
    # right = lst[len(lst) // 2:]
    # print(left)
    # print(right)
    #
    # left[1] = 22
    # print(left)
    # print(right)
    # print(lst)


