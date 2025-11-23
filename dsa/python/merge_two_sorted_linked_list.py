# CLASS REPRESENTING NODE

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next_pointer = None

# HELPERS TO EASY TEST AND CREATE EXAMPLES

def create_linked_list(arr):
    if not arr:
        return None

    init_node = ListNode(0)
    current = init_node

    for val in arr:
        current.next_pointer = ListNode(val)
        current = current.next_pointer

    return init_node.next_pointer

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

# NAIVE APPROACH - TIME COMPLEXITY O((n+m) x log(n+m)), SPACE COMPLEXITY O(n+m)

def merge_two_sorted_naive(head1, head2):

    arr = []

    arr = linked_list_to_list(head1, arr)
    arr = linked_list_to_list(head2, arr)

    if not arr:
        return None
    arr.sort()

    return create_linked_list(arr)

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


examples_dict = {
    1: {
        'list1': [1, 2, 4],
        'list2': [1, 3, 4],
        'expected': [1, 1, 2, 3, 4, 4]
    },
    2: {
        'list1': [],
        'list2': [],
        'expected': None
    },
    3: {
        'list1': [],
        'list2': [0],
        'expected': [0]
    },
    4: {
        'list1': [1, 5, 10],
        'list2': [2, 3,  4],
        'expected': [1, 2, 3, 4, 5, 10]
    },
    5: {
        'list1': [5, 10, 15, 40],
        'list2': [2, 3, 20],
        'expected': [2, 3, 5, 10, 15, 20, 40]
    },
    6: {
        'list1': [1, 1],
        'list2': [2, 4],
        'expected': [1, 1, 2, 4]
    }
}

def test_helpers():
    for idx, example in examples_dict.items():
        test_head = create_linked_list(example['list1'])
        test_arr = linked_list_to_list(test_head)
        if test_arr == example['list1'] or (test_arr is None and not example['list1']):
            print('Test passed')
        else:
            print('Test failed')
        print("Original list: ", example['list1'], "-------", "Test list: ", test_arr)


def run_algorithm(fun):
    for idx, example in examples_dict.items():
        head1 = create_linked_list(example['list1'])
        head2 = create_linked_list(example['list2'])
        new_head = fun(head1, head2)
        if example['expected'] == linked_list_to_list(new_head):
            print(idx, "Correct")
        else:
            print(idx, "Incorrect")



if __name__ == '__main__':
    run_algorithm(merge_two_sorted_recursive)
