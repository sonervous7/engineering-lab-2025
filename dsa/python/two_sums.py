# NAIVE APPROACH - O(n^2) TIME, O(n) SPACE
from operator import index


def two_sum_naive(nums, target) -> list:
    output = []
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                output.append(i)
                output.append(j)
                break
    return output

# BETTER APPROACH 1 - O(n x log(n)) TIME

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

# BETTER APPROACH 2 - O(n x log(n)) TIME

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

# EXPECTED APPROACH - O(n) TIME

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


examples_dict = {
    1: {
        'target': 9,
        'nums': [2, 7, 11, 15],
        'correct': [0, 1],
        'correct_sorted': [0, 1]
    },
    2: {
        'target': 6,
        'nums': [3, 2, 4],
        'correct': [1, 2],
        'correct_sorted': [0, 2]
    },
    3: {
        'target': 6,
        'nums': [3, 3],
        'correct': [0, 1],
        'correct_sorted': [0, 1]
    },
    4: {
        'target': -2,
        'nums': [0, -1, 2, -3, 1],
        'correct': [3, 4],
        'correct_sorted': [0, 3]
    },
    5: {
        'target': 0,
        'nums': [1, -2, 1, 0, 5],
        'correct': [],
        'correct_sorted': []
    }
}

def sorted_run(fun):
    for _, example in examples_dict.items():
        output = fun(example['nums'], example['target'])
        if output == example['correct_sorted']:
            print('TRUE')
        else:
            print('FALSE')

def unsorted_run(fun):
    for _, example in examples_dict.items():
        output = fun(example['nums'], example['target'])
        if output == example['correct']:
            print('TRUE')
        else:
            print('FALSE')

if __name__ == "__main__":
    unsorted_run(two_sum_expected)