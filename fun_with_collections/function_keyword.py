"""
Morgan Christensen

Module7
Program that has a function using arbitrary argument lits,
and keyword arguments to return a string
"""


def average_scores(*args, **kwargs):
    # Use *args for average calculation
    for key, value in kwargs.items():

        print("%s == %s" % (key, value))

    #return 'Resukts: name = {} {}, gpa = {}, major = {}'.format(kwargs['first_name'], kwargs['last_name'], , kwargs['major'])


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))