# Binary Search – Study Notes

---

## 📘 Problem Description - Binary Search

Binary Search is a searching algorithm that operates on a sorted or monotonic search space, repeatedly dividing it into halves to find a target value
or optimal answer in logarithmic time $O(\log N)$.

---

### Implementation Requirements:

* Implement **iterative** and **recursive** versions of the search function.
* The function should return the **index** of the target if found, and **None** otherwise.

### Boundary and Search Space Handling:

* The implementation must correctly handle an **empty input array**.
* The search range boundaries (`left` and `right`) must be managed robustly. The algorithm must guarantee termination and signal failure (return `None`) when the search space **collapses** (i.e., when the range of possible indices is exhausted or invalid).
---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- The problem is about finding target using two approaches - iterative and recursive
- Learning about one of the most popular searching algorithm
- Understaning the power of $O(\log N)$

**My first thoughts before coding:**
- Iterative approach is much simpler to do in my opinion.
- Checking if array is empty in recursive approach should be checked before entering function.
---

## Iterative approach

### ✔ Idea
- Use 3 variables - `left`, `right`, `mid`
- While loop with condition left >= right
- At each loop iteration, calculate mid and depends on conditions update variables.
### ✔ Complexity
- **Time:** O(log n) 
- **Space:** O(1)

### ✔ Implementation

```python
def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return None
```

## Recursive approach

### ✔ Idea
- As in iterative approach use 3 variables, but `left` and `right` is given parameter
- First calculate `mid`
- In contrast to iterative approach, manually check if `left` > `right`
- Then, depends on conditions, recursively call function with updated `left`/`right`
### ✔ Complexity
- **Time:** O(log n) 
- **Space:** O(log n)

### ✔ My Implementation
```python
def binary_search_recursive(arr, target, left, right):
    mid = (left + right) // 2

    if left > right:
        return None
    elif arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
```

---
### Thoughts
- If instead of passing `left` and `right`, I passed a split array (`arr[mid+1:]`), the space complexity would increase to $O(n)$. 
- Checking if array is empty in recursive should be done before entering the function.