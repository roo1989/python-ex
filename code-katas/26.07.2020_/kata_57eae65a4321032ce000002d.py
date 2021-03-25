"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: In Python, strings are immutable, so we have to create a list and join it.
"""

def solution_1(x):
    """
    First solution to the problem.

    Pros: Easy to read 
    """
    ret = []

    for num in x:
        if int(num) < 5:
            ret.append("0")
        else:
            ret.append("1")

    return "".join(ret)


def solution_2(x):
    """
    Second solution:

    TODO: Find a way to optimize.
    """

    return "".join([str(0) if int(num) < 5 else str(1) for num in x])
    


print("Example Tests")
tests = [
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

for exp, inp in tests:
    print(solution_2(inp), exp)
