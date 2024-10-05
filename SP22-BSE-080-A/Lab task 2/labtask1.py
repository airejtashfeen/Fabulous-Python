def get_list_input(prompt):
    return list(map(int, input(prompt).split()))

def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    return sorted(merged_list)

list1 = get_list_input("Enter values for the first list (separated by spaces): ")
list2 = get_list_input("Enter values for the second list (separated by spaces): ")

sorted_list = merge_and_sort_lists(list1, list2)

print(f"Sorted merged list: {sorted_list}")
