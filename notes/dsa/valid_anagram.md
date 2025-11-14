# Valid Anagram – Study Notes

---

## 📘 Problem Description
Given two non-empty strings `s1` and `s2` of lowercase letters,
determine if they are anagrams — i.e., if they contain the same characters
with the same frequencies.

You may assume:
- `1 <= s.length`, `t.length <= 5 * 10^4`,
- `s` and `t` consist of lowercase English letters.

---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- I guess, about working on strings
- Knowing good practices if it comes to strings

**My first thoughts before coding:**
- Python has many bulit-in string methods
- Could be It that simple?

---

## The most simple approach

### ✔ Idea
Sort both strings and check if they're the same.

### ✔ Complexity
- **Time:** O(m x log(m) + n x log(n)) 
- **Space:** Python - O(m + n), C++ - O(1)

### ✔ My Implementation (First Try – Python)

```python
def is_anagram_naive(a, b):
    return sorted(a) == sorted(b)
```

## Expected approach 1

### ✔ Idea
- Use hashmap or dict to count occurrences of each letter.
- Don't convert letters to numbers (ASCII)

### ✔ Complexity
- **Time:** O(n+m) 
- **Space:** O(1)

### ✔ My Implementation

```python
def is_anagram_expected1(a, b):
    char_count = {}
    for char in a:
        char_count[char] = char_count.get(char, 0) + 1
    for char in b:
        char_count[char] = char_count.get(char, 0) - 1

    for value in char_count.values():
        if value != 0:
            return False
    return True
```

## Expected approach 2

### ✔ Idea
- Use list with finite number of items and count occurrences of each letter.
- Every letter has its assigned position.

### ✔ Complexity
- **Time:** O(n+m) 
- **Space:** O(1)

### ✔ My Implementation

```python
def is_anagram_expected2(a, b):

    character_list = [0] * 26
    for char in a:
        character_list[ord(char) - ord('a')] += 1
    for char in b:
        character_list[ord(char) - ord('a')] -= 1
    return all([val == 0 for val in character_list])
```
---
### Thoughts
- I learned that the simplest way isn't always the most effective way.
- For most cases, probably I'll still use naive approach, but it's good to know how to do it effectively.
- I consolidated my knowledge about mutable and non-mutable vars in Python.
- The third approach demanded converting ASCII letters to nums. I used bulit-in `ord` method for that.
- The most interesting thing leaving aside time complexity is space complexity when it comes to the first approach specifically in Python.
- This is correlated strongly with `str` type in Python. Strings are immutable, so every changed on them (sorting, adding new letters e.t.c) incurs additional space complexity. 

