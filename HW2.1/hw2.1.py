"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple

list1 =[2, 2, 1, 1, 1, 2, 2]
list2=[3, 2, 3]
list3=[3, 3, 2, 2, 3, 3, 1]

def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    Tuple = list1, list2, list3
    for mostLeastCommon in Tuple:
        most_common_list = max(set(mostLeastCommon), key=mostLeastCommon.count)
        least_common_list = min(set(mostLeastCommon), key=mostLeastCommon.count)
        print(most_common_list, least_common_list)

major_and_minor_elem(Tuple)