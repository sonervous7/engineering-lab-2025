# Valid Palindrome – Study Notes

---

## 📘 Problem Description
Given a sentence `s`, determine whether it is a **palindrome sentence** or not.
A palindrome sentence is a sequence of characters that reads
the same forward and backward after:
- Converting all uppercase letters to lowercase,
- Removing all non-alphanumeric characters (i.e., ignore spaces, punctuation, and symbols).

---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- Data normalization
- Two pointer technic

**My first thoughts before coding:**
- String are immutable in Python, so SPACE COMPLEXITY in some approaches could lead to additional space.
- There are many str methods and approaches to modify strings in Python

---

## Naive approach

### ✔ Idea
Firstly - operations on Strings (copy, modify etc.), then Pythonic way with [::-1].

### ✔ Complexity
- **Time:** O(n) 
- **Space:** O(n)

### ✔ My Implementation (First Try – Python)

```python
def is_palindrome_naive(s):
    s1 = s.lower()
    s2 = ''.join(filter(str.isalnum, s1))
    return s2 == s2[::-1]
```
## Expected approach

### ✔ Idea
- Use two pointers (`i`, `j`) and while loop, then check if `s[i]` == `s[j]` and skip non-numerical.
### ✔ Complexity
- **Time:** O(n) 
- **Space:** O(1)

### ✔ My Implementation
```python
def is_palindrome_expected_approach(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[j].isalnum():
            j -= 1
            continue
        if not s[i].isalnum():
            i += 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True
```

---
### Thoughts
- In expected approach with two pointers space complexity is O(1) even if whe use `.lower()` method. The thing is, that I use this method on a single temporary char with const. lenght == 1. That's why space complexity is O(1).
.