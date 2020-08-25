"""Write a function called every_third_from_list. This function will take a list as an argument. This function should use slicing to return a new list containing every third element of the passed in list.

For example, given the input list:

some_list = ['ford', 'taurus', '1997', 'chevy', 'malibu', '2003', 'amish', 'buggy', '1857']

you would expect to return

['1997', '2003', '1857']"""

some_list = ['ford', 'taurus', '1997', 'chevy', 'malibu', '2003', 'amish', 'buggy', '1857']

def every_third_from_list(some_list):
  return some_list[2:len(some_list):3]

print(every_third_from_list(some_list))

