# NAIVE APPROACH - O(n^2) TIME, O(n) SPACE
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

# BETTER APPRACH 1 - O(n x log(n)) TIME

def two_sum_beter1(nums, target) -> list:
    output = []
    nums.sort()
    for i in range(len(nums)):
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

examples_dict = {
    1: {
        'target': 9,
        'nums': [2, 7, 11, 15],
    },
    2: {
        'target': 6,
        'nums': [3, 2, 4],
    },
    3: {
        'target': 6,
        'nums': [3, 3]
    },
    4: {
        'target': -2,
        'nums': [0, -1, 2, -3, 1]
    },
    5: {
        'target': 0,
        'nums': [1, -2, 1, 0, 5]
    }
}

if __name__ == "__main__":
    for _, example in examples_dict.items():
        output = two_sum_beter1(example['nums'], example['target'])
        print(output)