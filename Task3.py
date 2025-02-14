# Find the First Non-Repeating Character

from collections import Counter

def first_unique_char(s: str) -> str:
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return "None"

s = "swiss"
print(first_unique_char(s))  # Output: "w"
