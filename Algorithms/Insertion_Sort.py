# Insertion Sorting by Karpo

unsorted_list = [801,4,4,4,1,2,3,5,6,7,8,6,5,3,100,102,18,15,102,102,102,103,103,102,1.5,11,13,801]
# unsorted_list = [4,3,2,10,12,1,5,6]
unsorted_list2 = [5,4,3,2,1]

def insertion_sort(list):
    for item_index in range(len(list)):
        if item_index > 0:
            for swapping_index in range(item_index):
                cur_item = list[item_index - swapping_index]
                predecessor = list[item_index - swapping_index - 1]

                # if the item selected is smaller than its predecessor then swap between them
                if cur_item < predecessor:
                    list[item_index - swapping_index - 1] = cur_item
                    list[item_index - swapping_index] = predecessor

                else:
                    break

    return list

if __name__ == '__main__':
    print(insertion_sort(unsorted_list))
    # print(insertion_sort(unsorted_list2))
