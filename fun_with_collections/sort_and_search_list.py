"""
Morgan Christensen

Module 7: Search and sort lists
program that has functions for sorting list and searching through the list

10/11/20
"""


def make_list():
    u_list = []
    for i in range(0, 5):
        try:
            u_input = int(get_input())
            if u_input < 1 or u_input > 50:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            u_list.insert(i, u_input)
    return u_list


def get_input():
    u_input = input("give me a number: ")
    return u_input


def sort_list(list):
    return list.sort()


def search_list():
    pass


if __name__ == '__main__':
    try:
        test_list = make_list()
        print(test_list)
        sorted_list = sort_list(test_list)
        print(sorted_list)
    except ValueError:
        print("You gave an invalid input please give numbers")