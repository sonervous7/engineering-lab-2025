
def is_anagram_naive(a, b):
    return sorted(a) == sorted(b)

def is_anagram_expected1(a, b):
    char_count = {}
    for char in a:
        char_count[char] = char_count.get(char, 0) + 1
    for char in b:
        char_count[char] = char_count.get(char, 0) - 1

    for value in char_count.values():
        if value != 0:
            return False
    return True

def is_anagram_expected2(a, b):

    character_list = [0] * 26
    for char in a:
        character_list[ord(char) - ord('a')] += 1
    for char in b:
        character_list[ord(char) - ord('a')] -= 1
    return all([val == 0 for val in character_list])


examples_dict = {
    1: {
    's': 'geeks',
    't': 'kseeg'
    },
    2:
    {
    's': 'allergy',
    't': 'allergyy'
    },
    3: {
    's': 'listen',
    't': 'lists'
    },
    4:
    {
    's': 'rat',
    't': 'car'
    },
    5:
    {
    's': 'anagram',
    't': 'nagaram'
    }
}

if __name__ == '__main__':
    for _, example in examples_dict.items():
        print(is_anagram_expected2(example['s'],  example['t']))
