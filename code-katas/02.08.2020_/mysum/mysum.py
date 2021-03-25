def mysum(*args):
    """
    The challenge here is to write a mysum function that does the same thing as the built-in sum function.
    However,
    instead of taking a single sequence as a parameter, it should take a variable number of arguments. 
    Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).
    """
    # Basic way to do this.
    ret = 0
    for i in args:
        ret += i

    return ret 


def myaverage(numbers):
    """
    Write a function that takes a list of numbers. It should return the average (i.e., arithmetic mean) of those numbers.
    Note: Without using the len() built in Python function
    """
    mysum = 0
    length = 0

    for i in numbers:
        mysum += i
        length += 1

    return int(mysum / length)



def sum_obj(obj):
    """
    Write a function that takes a list of Python objects. Sum the objects that either are integers or can be turned into integers, ignoring the others.
    """
    
    ret = 0
    for i in obj:
        try:
            i = int(i)
        except:
            continue
    
        ret += i
    
    return ret



def length(obj):
    """
    Write a function that returns the length of an object (immitate len).
    """
    if not obj:
        return 0

    length = 0

    for i in obj:
        length += 1

    return length





print(sum_obj(['Ragnar', '23', [1,2,3]]))
print(myaverage([1,2,3]))
print(mysum(1,2,3))
