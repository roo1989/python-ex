"""
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November) 
is part of the fourth quarter.
"""


def quarter_of(month):
    if month < 1 or month > 12:
        return 0

    if month <= 3:
        return 1


print("Basic Tests")
print(quarter_of(3), 1)
print(quarter_of(8), 3)
print(quarter_of(11), 4)
