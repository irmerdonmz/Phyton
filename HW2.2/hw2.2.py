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

letters = {
  "A": "1", "c": "3", "b": "3", "e": "1", "d":"2", "g": "2","f": "4", "i": "1",
  "h": "4", "k": "5", "j": "8", "m": "3","l": "1", "o": "1", "n": "1", "q": "10",
  "p": "3", "s": "1","r": "1", "u": "1", "t": "1", "w": "4", "v": "4", "y": "4","x": "8", "z": "10"
}
print(letters)
for i,j in letters.items():
    print(i + " " + j)

    a = dict.fromkeys(letters[i][0], i)
    print(a)
def scrabble_score(word):
    total = 0
    for letter in word:
        total += letters[letter]
    return total

#def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:

