from collections import Counter
list = [2, 2, 1, 1, 1, 2, 2]
list1 = [3, 2, 3]
list2 = [3, 3, 2, 2, 3, 3, 1]

most_common_list = max(set(list), key=list.count)
most_common_list1 = max(set(list1), key=list1.count)
most_common_list2 = max(set(list2), key=list2.count)

print("The most common element of list is:", most_common_list)
print("The most common element of list1 is:", most_common_list1)
print("The most common element of list2 is:", most_common_list2)

least_common_list = min(set(list), key=list.count)
least_common_list1 = min(set(list1), key=list1.count)
least_common_list2 = min(set(list2), key=list2.count)

print("The least common element of list is:", least_common_list)
print("The least common element of list1 is:", least_common_list1)
print("The least common element of list2 is:", least_common_list2)