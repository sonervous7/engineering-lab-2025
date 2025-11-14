# Two Sum – Study Notes

---

## 📘 Problem Description
Given an array of integers `nums` and an integer `target`,  
return **indices** of the two numbers such that they add up to `target`.

You may assume:
- the same element cannot be used twice,
- return the indices in order they occur.

---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- find *two* numbers in a list that sum to target  
- order doesn't matter  
- constraints push toward an O(n) solution  

**My first thoughts before coding:**
-  nested loops (i, j) and checking every possible values
-  is legal using python bulit-in method sort on list?
-  how can I reach to O(n)?

---

## 🐌 Naive Approach (Brute Force)

### ✔ Idea
Check every pair `(i, j)` and compare `nums[i] + nums[j]` with target.

### ✔ Complexity
- **Time:** O(n²)  
- **Space:** O(1)

### ✔ My Implementation (First Try – Python)

```python
def two_sum_naive(nums, target) -> list:
    output = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
            break
        break
    return output
```
## Better Approach (using binary search)

### ✔ Idea
Calculate expected value and search it using binary search.

### ✔ Complexity
- **Time:** O(n x log(n))  
- **Space:** O(1)

### ✔ My Implementation (Python)

```python
def two_sum_beter1(nums, target) -> list:
    output = []
    nums.sort()
    for i in range(len(nums) - 1):
        comp = target - nums[i]
        idx_of_comp = binary_search(nums, i+1, comp)
        if idx_of_comp:
            output.append(i)
            output.append(idx_of_comp)
            break
    return output

def binary_search(arr, low, x):
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return False
```

## Better Approach 2 (using pointers)

### ✔ Idea
Use left and right egdes of array as indices and move them to find sum with while loop.

### ✔ Complexity
- **Time:** O(n x log(n))  
- **Space:** O(1)

### ✔ My Implementation (Python)

```python
def two_sum_beter2(nums, target) -> list:
    output = []
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            output.append(left)
            output.append(right)
            break
        elif nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
    return output
```

## Expected Approach (using set or hashmap)

### ✔ Idea
For Python use empty set() and check if calculated component exist in set. 
### ✔ Complexity
- **Time:** O(n)  
- **Space:** O(1)

### ✔ My Implementation (Python)

```python
def two_sum_expected(nums, target) -> list:
    output = []
    s = set()
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in s:
            output.append(nums.index(comp))
            output.append(i)
            break
        else:
            s.add(nums[i])
    return output
```
---
### Thoughts
I learned that `set()` is implemented in Python as hash table.
Becasue of that:
- checking `x in set` -> **O(1)**
- as well adding `set.add(x)` -> **O(1)**

Only hashable elements can be in set, that is `int`, `str`, `tuple` but NOT `list`

