# IN THIS EXAMPLE, I FOCUS ON BINARY SEARCH, SO EVERY ARRAY IS ALREADY SORTED
# (although sorting could be done simply using .sort())

# TIME COMPLEXITY O(log n), SPACE COMPLEXITY O(1)
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

# TIME COMPLEXITY - O(log n) , SPACE COMPLEXITY - O(log n) because of recursive call stack

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



examples_dict = {
    1: { # Standard (mid)
        'arr': [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
        'target': 23,
        'ans': 5
    },
    2: { # Target at idx 0
        'arr': [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
        'target': 2,
        'ans': 0
    },
    3: { # Target at last idx
        'arr': [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
        'target': 91,
        'ans': 9
    },
    4: { # Target is not in arr (too low)
        'arr': [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
        'target': 0,
        'ans': None
    },
    5: { # Target is not in arr (too high)
        'arr': [2, 5, 8, 12, 16, 23, 38, 56, 72, 91],
        'target': 100,
        'ans': None
    },
    6: { # Empty arr
        'arr': [],
        'target': 5,
        'ans': None
    },
    7: { # Arr with one item (success)
        'arr': [5],
        'target': 5,
        'ans': 0
    },
    8: { # Arr with one item (failure)
        'arr': [5],
        'target': 1,
        'ans': None
    }
}



def run_iterative():
    for idx, v in examples_dict.items():
        if binary_search_iterative(v['arr'], v['target']) == v['ans']:
            print(idx ,"Correct")
        else:
            print(idx, "Incorrect")

def run_recursive():
    for idx, v in examples_dict.items():
        if v['arr']:

            if binary_search_recursive(v['arr'], v['target'], 0, len(v['arr']) - 1) == v['ans']:
                print(idx ,"Correct")
            else:
                print(idx, "Incorrect")
        else:
            print(idx, "Array Empty")

if __name__ == '__main__':
    run_recursive()