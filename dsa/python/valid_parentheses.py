# STACK APPROACH - O(n) TIME COMPLEXITY and O(n) SPACE COMPLEXITY
def valid_parenthese_stack(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(')')
        elif char == '[':
            stack.append(']')
        elif char == '{':
            stack.append('}')
        if char == ')' or char == ']' or char == '}':
            if stack:
                if stack[-1] != char:
                    return False
                stack.pop()
            else:
                return False

    return not stack




examples_dict = {
    1: {
        'input': '[{()}]',
        'ans': True
    },
    2: {
        'input': '([{]})',
        'ans': False
    },
    3: {
        'input': '()[]{}',
        'ans': True
    },
    4: {
        'input': '([)]',
        'ans': False
    },
    5: {
        'input': '([])',
        'ans': True
    },
    6: {
        'input': '}',
        'ans': False
    },
    7: {
        'input': '{',
        'ans': False
    },
    8: {
        'input': '',
        'ans': True
    },
    9: {
        'input': ')(){}',
        'ans': False
    },
    10: {
        'input': '((()))',
        'ans': True
    }
}


def run_algorithm(fun):
    for idx, v in examples_dict.items():
        if fun(v['input']) == v['ans']:
            print(f"{idx}: Correct")
        else:
            print(f"{idx}: Incorrect")

if __name__ == '__main__':
    run_algorithm(valid_parenthese_stack)
