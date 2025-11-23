# Merge two sorted linked list – Study Notes

---

## 📘 Problem Description - Merge two sorted linked list

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

### Constraints:

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
-  Both list1 and list2 are sorted in non-decreasing order.
---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
- The problem is about merging two sorted list in one sorted list.
- I think, the idea is to do it without any additional space complexity.
- The problem shows differences between array and linked-list.

**My first thoughts before coding:**
- If I have pointers to each element I can try change item they point.
- Maybe first, I can use additional space complexity to do it in naive way.
- In Python I need to do additional class/container denoting a node.

## Defining appropriate structure (Python)

To begin, I defined the `class ListNode` to represent the structure of a single node. This class serves as the foundation for all solution approaches:

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next_pointer = None
```
**Note:** I named the reference to the subsequent node *next_pointer* instead of *next* to avoid potential conflicts with Python's built-in next() function/keyword.

## Naive approach

### ✔ Idea
- Use additional array/list and append each of item of two lists
- Then sort it with (in Python - with `sort()` method)
- Retrun new merged list
### ✔ Complexity
- **Time:** $O((N+M) \times \log (N+M))$
- **Space:** $O(N+ M)$

### ✔ Implementation Python

To effectively test the results using my standard `examples_dict` pattern,
I needed a way to bridge the gap between the Linked List structure and standard
Python arrays. I implemented two helper functions to handle this data transformation.
I initially created them for testing purposes, but they also proved essential
for the *Naive* approach, which relies on converting data types.

**Helper 1**: Create Linked List Constructs a fully operational linked list from a standard input array

```python
def create_linked_list(arr):
    if not arr:
        return None

    init_node = ListNode(0)
    current = init_node

    for val in arr:
        current.next_pointer = ListNode(val)
        current = current.next_pointer

    return init_node.next_pointer
```

**Helper 2:** Convert Linked List to Array Traverses the linked list and collects values into a standard list. This is primarily used to verify the output against expected results.

```python
def linked_list_to_list(head, arr=None):

    if not head:
        return None

    if arr is None:
        arr = []

    current = head
    while current:
        arr.append(current.val)
        current = current.next_pointer

    return arr
```

**Algorithm**:
```python
def merge_two_sorted_naive(head1, head2):

    arr = []

    arr = linked_list_to_list(head1, arr)
    arr = linked_list_to_list(head2, arr)

    if not arr:
        return None
    arr.sort()

    return create_linked_list(arr)
```

With this two helpers, the implementation is very easy. I pass array as reference so functions work on the same chunk of data. Nevertheless, the space complexity remains at $O(N + M)$.

## Recursive merge approach

### ✔ Idea
The idea is to pick the smaller head node at each step and let recursion merge the remaining parts. if one list is empty, return the other, otherwise the smaller node becomes the next node in the merged list and its next is the recursive merge of the rest.

### ✔ Complexity
- **Time:** $O(N + M)$ 
- **Space:** $O(N +M)$

### ✔ My Implementation
```python
def merge_two_sorted_recursive(head1, head2):

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val <= head2.val:
        head1.next_pointer = merge_two_sorted_recursive(head1.next_pointer, head2)
        return head1
    else:
        head2.next_pointer = merge_two_sorted_recursive(head1, head2.next_pointer)
        return head2
```
In this version there are hidden costs of recursion. Despite the lack of loops, each *Node* must be checked
once, which gives us a time complexity of $O(N+M)$ for two lists.

When ut comes to space complexity, as is standard fo recursion,
we have a stack of calls, so the space complexity is  $O(N+M)$.

---

## Iterative merge approach

---
### Thoughts
