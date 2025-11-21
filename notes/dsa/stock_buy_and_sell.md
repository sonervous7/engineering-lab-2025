# Stock Buy and Sell Max one Transaction Allowed – Study Notes

---

## 📘 Problem Description

Given an array `prices[]` of length `N`, representing the prices of the stocks
on different days, the task is to find the maximum profit possible
by buying and selling the stocks on different days when
at most one transaction is allowed.
Here one transaction means 1 buy + 1 Sell.
- **Note:** Stock must be bought before being sold.
---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- Operations on array and finding best solution which is maxium profit
- Finding appropriate solution without necessary operations on array.
- Avoiding naive comparing in nested loops.

**My first thoughts before coding:**
- The examples of input and output say that I need calculate each diff and compare them to find min (buy for 1, sell for 10 -> 1-10=-9, profit=9)
- I will first try to achieve appropriate solution with the worst complexity simply by calculating each diff and compare to each other.
- After that maybe I could figure out how to decrease time complexity.
---

## Naive approach

### ✔ Idea
Calculating each diff in two nested loop in order to find max profit. 

### ✔ Complexity
- **Time:** O(n^2) 
- **Space:** O(1)

### ✔ My Implementation (First Try – Python)

```python
def stock_buy_and_sell_naive(arr):
    diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] - arr[j] < diff:
                diff = arr[i] - arr[j]
    return abs(diff)
```

Then I found better way to do naive approach in more "Pythonic" way:
```python
def stock_buy_and_sell_naive2(arr):
    diff = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diff = max(diff, arr[j] - arr[i])
    return diff
```
## Expected approach

### ✔ Idea
- One travel through array, using additional variable `min_price` meaning Minimum Price so far.
### ✔ Complexity
- **Time:** O(n) 
- **Space:** O(1)

### ✔ My Implementation
```python
def stock_buy_and_sell(arr):
    min_price = arr[0]
    diff = 0
    for i in range(len(arr) - 1):
        if arr[i] < min_price:
            min_price = arr[i]
        if arr[i+1] - min_price > diff:
            diff = arr[i+1] - min_price
    return diff
```

---
### Thoughts
- As well as in naive approach, the expected approach could be done in more "Pythonic" way using built-in `max`, `min` methods.
- Very easy problem in my opinion. I figured out expected approach before naive.