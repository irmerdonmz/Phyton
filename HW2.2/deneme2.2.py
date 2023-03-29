"""
Extract scrabble scores from a legacy system.

The old system stored a list of letters per score:
    1 point: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
    2 points: "D", "G",
    3 points: "B", "C", "M", "P",
    4 points: "F", "H", "V", "W", "Y",
    5 points: "K",
    8 points: "J", "X",
    10 points: "Q", "Z",

The new system instead stores the score per letter:
    "a" is worth 1 point.
    "b" is worth 3 points.
    "c" is worth 3 points.
    "d" is worth 2 points.
    Etc.
Transform the legacy data format to the new format.

Input: {1: ["A", "E"], 2: ["D", "G"]}
Output: {"a": 1, "d": 2, "e": 1, "g": 2}
"""
from typing import Dict, List

def transform():
    #print(i + " " + j)
    #a = dict.fromkeys(letters[i][0], i)
    #print(a)
    list = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    list2 = ["D", "G"]
    list3 = ["B", "C", "M", "P"]
    list4 = ["F", "H", "V", "W", "Y"]
    list5 = ["K"]
    list6 = ["J", "X"]
    list7 = ["Q", "Z"]

    x = dict.fromkeys(list,1)
    x2 = dict.fromkeys(list2, 2)
    x3 = dict.fromkeys(list3, 3)
    x4 = dict.fromkeys(list4, 4)
    x5 = dict.fromkeys(list5, 5)
    x6 = dict.fromkeys(list6, 6)
    x7 = dict.fromkeys(list7, 7)
    print(dict(**x, **x2, **x3, **x4, **x5, **x6, **x7))

transform()

#def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:

