"""
Morgan Christensen

Module7
Program that has a function using arbitrary argument lists,
and keyword arguments to return a string
"""


def average_scores(*args, **kwargs):

    for key, value in kwargs.items():
        average = (args[0] + args[1] + args[2] + args[3])/4
        print("%s == %s" % (key, value))

    return 'Results: name = {} {}, gpa = {}, major = {}'.format(kwargs['first_name'],  kwargs['last_name'], average, kwargs['major'])


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(5, 1, 6, 8, first_name='Austin', last_name='Powers', major='Super villian'))
    print(average_scores(7, 2, 8, 6, first_name='Micheal', last_name='Myers', major='Hero'))
