from collections import deque

# DFS APPROACH - O(N X M) TIME COMPLEXITY, O(N X M) - SPACE COMPLEXITY

def dfs(img, sr, sc, new_color, original_color):
    if (sr < 0 or sr >= len(img)) or (sc < 0 or sc >= len(img[0])) or (img[sr][sc] != original_color):
        return

    img[sr][sc] = new_color

    dfs(img, sr + 1, sc, new_color, original_color)
    dfs(img, sr - 1, sc, new_color, original_color)
    dfs(img, sr, sc + 1, new_color, original_color)
    dfs(img, sr, sc - 1, new_color, original_color)


def flood_fill_dfs(img, sr, sc, new_color):

    if img[sr][sc] == new_color:
        return img

    original_color = img[sr][sc]
    dfs(img, sr, sc, new_color, original_color)

    return img

# BFS APPROACH - O(N X M) TIME COMPLEXITY, O(N X M) - SPACE COMPLEXITY

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




examples_dict = {
    1: {
        'img': [[1, 1, 1, 0],
                [0, 1, 1, 1],
                [1, 0, 1, 1]],
        'sr': 1,
        'sc': 2,
        'new_color': 2,
        'output': [[2, 2, 2, 0],
                   [0, 2, 2, 2],
                   [1, 0, 2, 2]
                  ]
    },
    2: { # EDGE CASE 1
        'img': [[5, 2, 5],
                [5, 5, 5]],
        'sr': 1,
        'sc': 1,
        'new_color': 5,
        'output': [[5, 2, 5],
                   [5, 5, 5]
                  ]
    },
    3: { # EDGE CASE 2
        'img': [[2, 9, 2],
                [9, 1, 9],
                [2, 9, 2]],
        'sr': 1,
        'sc': 1,
        'new_color': 8,
        'output': [[2, 9, 2],
                   [9, 8, 9],
                   [2, 9, 2]
                  ]
    },
    4: { # EDGE CASE 3
        'img': [[3, 3, 3],
                [3, 3, 3]],
        'sr': 0,
        'sc': 0,
        'new_color': 7,
        'output': [[7, 7, 7],
                   [7, 7, 7]
                  ]
    },
    5: { # EDGE CASE 4
        'img': [[4, 4, 1],
                [4, 1, 1],
                [1, 1, 1]],
        'sr': 0,
        'sc': 0,
        'new_color': 0,
        'output': [[0, 0, 1],
                   [0, 1, 1],
                   [1, 1, 1]
                  ]
    },
    6: { # BIGGER EXAMPLE
        'img': [[0, 1, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1]],
        'sr': 1,
        'sc': 1,
        'new_color': 3,
        'output': [[0, 3, 3, 3, 0],
                   [3, 3, 0, 3, 3],
                   [3, 0, 0, 0, 3],
                   [3, 3, 0, 3, 3]
                  ]
    }
}

def run_algorithm(fun):
    for idx, item in examples_dict.items():
        output = fun(item['img'], item['sr'], item['sc'], item['new_color'])
        if output == item['output']:
            print(idx, "Correct\n", output)
        else:
            print(idx, "Incorrect\n", output)


if __name__ == '__main__':
    run_algorithm(flood_fill_bfs)
