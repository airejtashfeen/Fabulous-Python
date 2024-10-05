list1 = list(map(int, input("Enter values for the first list (separated by spaces): ").split()))
list2 = list(map(int, input("Enter values for the second list (separated by spaces): ").split()))

merged_list = list1 + list2
sorted_list = sorted(merged_list)

print("Largest element is:", sorted_list[-1])
print("Smallest element is:", sorted_list[0])
