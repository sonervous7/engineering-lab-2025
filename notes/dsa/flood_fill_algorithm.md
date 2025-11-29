# Flood fill – Study Notes

---

## 📘 Problem Description - Binary Search
Given a 2D grid `img[][]` representing an image, where each element `img[i][j]`
is an integer that denotes the color of a pixel. Also there is a coordinates
*(sr, sc)* representing the starting pixel (row sr and column sc) and an integer
`newColor`, which represents the new color to apply.
We need to perform a flood fill on the image starting from *(sr, sc)*.
It means we must change the color of the starting pixel and all other pixels
that are connected to it (directly or indirectly) and have the same original color
as the starting pixel.

Two pixels are considered connected if they are adjacent horizontally or vertically (not diagonally).

---

### Example:
- **Input:** `image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2`
- **Output:** `[[2,2,2],[2,2,0],[2,0,1]]`

### Boundary and Search Space Handling:
- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 216`
- `0 <= sr < m`
- `0 <= sc < n`
---

## 🧠 My Understanding of the Problem
**What the problem is really about:**  
The main goal is to color all pixels which are connected to starting pixel
(with constraints what means "connected")

Color of the starting pixel need to be different from newColor.

This is about DFS and BFS.

**My first thoughts before coding:**

I need get color of starting pixel and compare it to newColor, before I start.

There are 4 constraints:
1. If starting pixel has the same color as newColor, we return unchnaged img.
2. If starting pixel is out of range, we do not start algorithm.
3. The same thing goes for next pixel. We need to watch out edges.
4. Adjacent pixel has to have the same color as originalColor from starting pixel.

DFS seems to be easier to implement but idk.

---

## DFS approach

### ✔ Idea
For each adjacent pixel vertically and horizontally, we call the dfs function, which will change the color if the conditions are met.

### ✔ Complexity
- **Time:** $O(N \times M)$ 
- **Space:** $O(N \times M)$ 

### ✔ Implementation

I split the solution into two functions. One that replaces the color and checks the boundary conditions, and the other main one that checks the initial condition and calls the next one. 

1. Helper
```python
def dfs(img, sr, sc, new_color, original_color):
    if (sr < 0 or sr >= len(img)) or (sc < 0 or sc >= len(img[0])) or (img[sr][sc] != original_color):
        return

    img[sr][sc] = new_color

    dfs(img, sr + 1, sc, new_color, original_color)
    dfs(img, sr - 1, sc, new_color, original_color)
    dfs(img, sr, sc + 1, new_color, original_color)
    dfs(img, sr, sc - 1, new_color, original_color)

```
2. Main function
```python
def flood_fill_dfs(img, sr, sc, new_color):

    if img[sr][sc] == new_color:
        return img

    original_color = img[sr][sc]
    dfs(img, sr, sc, new_color, original_color)

    return img

```

## BFS approach

### ✔ Idea
We use a FIFO queue, where we have a condition—as long as the queue is not empty, we continue to perform operations. We change the first pixel manually.
### ✔ Complexity
- **Time:** $O(N \times M)$ 
- **Space:** $O(N \times M)$ 

### ✔ Implementation
```python
def flood_fill_bfs(img, sr, sc, new_color):

    original_color = img[sr][sc]

    if original_color == new_color:
        return img

    que = deque()
    que.append((sr, sc))

    img[sr][sc] = new_color

    while que:
        r, c = que.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < len(img) and 0 <= nc < len(img[0]) and img[nr][nc] == original_color:
                que.append((nr, nc))
                img[nr][nc] = new_color

    return img
```
---
### Thoughts
Breaking the solution down into two functions greatly improved readability (DFS).
The dfs solution seems natural for this type of problem.

I learned about a new structure called deque from the collections module.
According to the information I found, deque is better for this type of operation 
due to the complexity of the pop `O(1)` operation and does not require shifting
as with a regular list. 

Despite the differences in algorithms, the time complexity remains the same.
This is because we have to visit all pixels anyway to check whether
they should be colored or not.
The memory complexity is the same, but its source is different in both algorithms.
BFS is generally safer because it allows us to explicitly control the queue and
transfers the risk of recursion limits to RAM. 

