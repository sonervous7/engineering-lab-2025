# Valid Parenthese – Study Notes

---

## 📘 Problem Description
Given a string **s** containing three types of brackets `{}`, `()` and `[]`. Determine whether the Expression are balanced or not.
An expression is balanced if each opening bracket has a corresponding closing bracket of the same type, the pairs are properly ordered and no bracket closes before its matching opening bracket.
- **Balanced:** "[()()]{}" → every opening bracket is closed in the correct order.
- **Not Balanced:** "([{]})" → the ']' closes before the matching '{' is closed, breaking the nesting rule.

You may assume:
- `1 <= input.length <= 10^4`,
- `input str` consists of parentheses only '()[]{}'

---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- Logical thinking
- String operations and some validation.

**My first thoughts before coding:**
- String are immutable in Python, so SPACE COMPLEXITY in some approaches could lead to additional space.
- This seems to be easy, but there are many unpredictable outcomes.

---

## Stack approach

### ✔ Idea
Create stack and add opening brackets to it, then if next char is closing bracket -> check if it matches corresponding opening bracket on the end of stack.

### ✔ Complexity
- **Time:** O(n) 
- **Space:** O(n)

### ✔ My Implementation (First Try – Python)

```python
def valid_parenthese_stack(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == '{':
            stack.append('}')
        if char == ')' or char == ']' or char == '}':
            boolean_stack = bool(stack)
            if boolean_stack:
                if stack[-1] != char:
                    return False
                stack.pop()
            else:
                return False

    return not stack
```

### Then I found, that I could do it more 'Pythonic'
Instead of casting list explicitly to bool, we can use default list behaviour.
```python
boolean_stack = bool(stack)
if boolean_stack:
```
**Changed to this:**
```python
if stack:
    if stack[-1] != char:
        return False
    stack.pop()
else:
    return False
```
## Expected approach

### ✔ Idea
- Create virtual stack. We reserve chunk of a string and use pointer
- The idea is mostly the same, but we do not use another structure.
- It only works with C++ and similar (strings are mutable in cpp).

### ✔ Complexity
- **Time:** O(n) 
- **Space:** O(1)

### ✔ My Implementation


---
### Thoughts
- I learned how to use boolean operations on lists in python.
- I have consolidated my knowledge about strings in Python (immutable).