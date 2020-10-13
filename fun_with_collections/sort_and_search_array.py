"""
Morgan Christensen

Module 7: Search and sort lists
program that has functions for sorting and searching through an array

10/11/20
"""
import array as arr

def make_array():
    a = arr.array = []
    for i in range(0, 5):
        try:
            u_input = int(get_input())
            if u_input < 1 or u_input > 50:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            a.insert(i, u_input)
    return a


def get_input():
    u_input = input("give me a number: ")
    return u_input


def sort_array(a):
    """My function includes a return statement because
    with a print in the method my test does not pass"""
    a.sort()
    return a


def search_array(a, x):
    for i in a:
        if i == x:
            return x
        elif i != x and i < len(a):
            ++i
        else:
            x = -1
            return x


if __name__ == '__main__':
    try:
        test_array = make_array()
        print(test_array)
        search = search_array(test_array, 45)
        print(search)
        print(sort_array(test_array))
    except ValueError:
        print("You gave an invalid input please give numbers")