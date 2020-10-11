"""
Morgan Christensen

Module 7: Search and sort lists
program that has functions for sorting and searching through an array

10/11/20
"""
import array

def make_array():
    arr = []
    for i in range(0, 5):
        try:
            u_input = int(get_input())
            if u_input < 1 or u_input > 50:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            arr.insert(i, u_input)
    return arr


def get_input():
    u_input = input("give me a number: ")
    return u_input


def sort_array(arr):
    """My function includes a return statement because
    with a print in the method my test does not pass"""
    #arr.sort()
    #return arr


def search_array(arr, x):
    for i in arr:
        if i == x:
            return x
        elif i != x and i < len(arr):
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