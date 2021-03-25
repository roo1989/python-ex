"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(string):
    ret = {}

    for i in range(len(string)):
        if string[i] not in ret.keys():
            ret[string[i]] = 0
        ret[string[i]] += 1

    return ret


print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})
