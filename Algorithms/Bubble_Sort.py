# Bubble Sort by Karpo

unsorted_list = [5,1,4,2,8]
# unsorted_list = [5,5,5,0,2,2,2,2,5,2,3,3,5,4,61,21,135,1643,41]

def bubble_sort(list):
    was_swapped = True

    while was_swapped:
        was_swapped = False

        for cur_item_index in range(len(list)):
            # making sure cur_item_index is not the last item in the list before continuing
            if cur_item_index + 1 != len(list):
                # next_item is the item that is after the current item
                next_item = list[cur_item_index + 1]

                # if the current item is bigger than the next item, swap between them, and make the 'was_swapped' var True
                if list[cur_item_index] > next_item:
                    was_swapped = True
                    temp = list[cur_item_index]
                    list[cur_item_index] = next_item
                    list[cur_item_index + 1] = temp

    return list

print(bubble_sort(unsorted_list))


