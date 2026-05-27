#!/usr/bin/env python3
'''Lab 3 Part 3 Using Lists '''
# Author ID: tchu20

# Place my_list below this comment (before the function definitions)

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)

    # Created a new variable call "last_item" and equal to the last number of the my_list
    last_item = ordered_list[-1]

    # created new variable and call "new_item" and the last number of the list + 1
    new_item = last_item + 1
    
    # Add the new number to the end of the my_list
    ordered_list.append(new_item)

    # return new numbers to the my_list
    return ordered_list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list

        # item take each number from the list and store inside variable "item = 1"
        for item in items_to_remove:
            # if the item = 1 inside the my_list
            if item in ordered_list:
                 # remove 1 from the my_list
                 ordered_list.remove(item)
        
        return ordered_list


# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)