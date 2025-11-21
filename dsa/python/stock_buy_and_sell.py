# NAIVE APPROACHES - O(n^2) TIME COMPLEXITY, O(1) SPACE COMPLEXITY

def stock_buy_and_sell_naive(arr):
    diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] - arr[j] < diff:
                diff = arr[i] - arr[j]
    return abs(diff)

def stock_buy_and_sell_naive2(arr):
    diff = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diff = max(diff, arr[j] - arr[i])
    return diff

# EXPECTED APPROACHES ONE LOOP - O(n) TIME COMPLEXITY, O(1) SPACE COMPLEXITY
def stock_buy_and_sell(arr):
    min_price = arr[0]
    diff = 0
    for i in range(len(arr) - 1):
        if arr[i] < min_price:
            min_price = arr[i]
        if arr[i+1] - min_price > diff:
            diff = arr[i+1] - min_price
    return diff

def stock_buy_and_sell2(arr):
    min_price = arr[0]
    diff = 0
    for i in range(len(arr) - 1):
        min_price = min(min_price, arr[i])
        diff = max(diff, arr[i+1] - min_price)
    return diff



examples_dict = {
    1: {
        'prices': [7, 10, 1, 3, 6, 9, 2],
        'output': 8
    },
    2: {
        'prices': [7, 6, 4, 3, 1],
        'output': 0
    },
    3: {
        'prices': [1, 3, 6, 9, 11],
        'output': 10
    }
}


def run_algorithm(fun):
    for idx, value in examples_dict.items():
        if fun(value['prices']) == value['output']:
            print(idx, "Correct")
        else:
            print(idx, "Incorrect")

if __name__ == '__main__':
    run_algorithm(stock_buy_and_sell2)