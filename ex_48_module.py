NAME = "ex_48_module"

import time

def floor(x):
    """
    Return the floor of x.
    """
    print("function from mymodule.....  floor(%s)" % x)
    return x // 1

# import courses,


import courses

print(dir(courses))
courses.html.get_html()
courses.java.get_java()