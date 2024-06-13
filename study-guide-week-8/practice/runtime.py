def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    """
    #constant time
    if len(s1) != len(s2):
        return False
    #linear time
    for i in range(len(s1)):
        #constant
        if s1[i] != s2[i]:
            return False

    return True
#my guess: quadratic time 


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals."""

    if "hippo" in animals or "platypus" in animals:
        return True
    else:
        return False
#my guess: linear 

def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero."""
    #constant
    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)
    #linear times
    for x in s:
        #constant 
        if -x in s:
            #constant 
            result.append((-x, x))

    return result
#my guess: quadratic 

def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero. """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result
#guess: quadratic

def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y and (x, y) not in result and (y, x) not in result:
                result.append((x, y))
    return result
#guess big O of n^3