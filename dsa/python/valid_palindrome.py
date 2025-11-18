# NAIVE APPROACH O(n) TIME COMPLEXITY AND O(n) SPACE COMPLEXITY

def is_palindrome_naive(s):
    s1 = s.lower()
    s2 = ''.join(filter(str.isalnum, s1))
    return s2 == s2[::-1]


# Expected Approach O(n) Time and O(1) Space TWO POINTERS

def is_palindrome_expected_approach(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[j].isalnum():
            j -= 1
            continue
        if not s[i].isalnum():
            i += 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

examples_dict = {
    1: {
        's': 'Too hot to hoot',
        'ans': True
    },
    2: {
        's': 'Abc 012..## 10cbA',
        'ans': True
    },
    3: {
        's': 'ABC $. def01ASDF..',
        'ans': False
    },
    4: {
        's': '',
        'ans': True
    },
    5: {
        's': '!',
        'ans': True
    },
    6: {
        's': 'A',
        'ans': True
    },
    7: {
        's': '0P',
        'ans': False
    },
    8: {
        's': '.,',
        'ans': True
    }
}


def run_algorithm(fun):
    for idx, value in examples_dict.items():
        if fun(value['s']) == value['ans']:
            print(idx, "Correct")
        else:
            print(idx, "Incorrect")


if __name__ == '__main__':
    run_algorithm(is_palindrome_expected_approach)