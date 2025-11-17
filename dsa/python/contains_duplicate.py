
# NAIVE APPROACH - O(n^2) TIME COMPLEXITY
def contains_duplicate_naive(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Using set (hashmap) - O(n) TIME COMPLEXITY
def contains_duplicate_expected1(lst):
    s = set()
    for num in lst:
        if num in s:
            return True
        s.add(num)
    return False

# Other Approach - O(n * log(n)) TIME COMPLEXITY
def contains_duplicate_other(lst):
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return True
    return False




examples_dict = {
    1: {
        'arr': [4, 5, 6, 4],
        'ans': True
    },
    2: {
        'arr': [1, 2, 3, 4],
        'ans': False
    },
    3: {
        'arr': [1, 2, 3, 1],
        'ans': True
    },
    4: {
        'arr': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
        'ans': True
    }
}


def run_algorithm(fun):
    for _, v in examples_dict.items():
        if fun(v['arr']) == v['ans']:
            print("Correct")
        else:
            print("Incorrect")

if __name__ == '__main__':
    run_algorithm(contains_duplicate_other)
