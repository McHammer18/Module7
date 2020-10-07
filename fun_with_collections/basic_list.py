"""
Morgan Christensen

Module 7- Basic list

10/06/20
"""


def make_list():
    u_list = []
    for i in range(0,5):
        u_input = int(get_input())
        u_list.insert(i, u_input)
    return u_list


def get_input():
    u_input = input("give me a number: ")
    return u_input


if __name__ == '__main__':
    try:
        test_list = make_list()
        print(test_list)
    except ValueError:
        print("You gave an invalid input please give numbers")