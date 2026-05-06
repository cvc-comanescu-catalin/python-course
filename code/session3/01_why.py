from util import *

sales1=read_int('Enter the sales for stand 1: ')
sales2=read_int('Enter the sales for stand 2: ')
sales3=read_int('Enter the sales for stand 3: ')
sales4=read_int('Enter the sales for stand 4: ')
sales5=read_int('Enter the sales for stand 5: ')
sales6=read_int('Enter the sales for stand 6: ')
sales7=read_int('Enter the sales for stand 7: ')
sales8=read_int('Enter the sales for stand 8: ')
sales9=read_int('Enter the sales for stand 9: ')
sales10=read_int('Enter the sales for stand 10: ')

if sales1>sales2 and sales1>sales3 and sales1>sales4 \
   and sales1>sales5 and sales1>sales6 and sales1>sales7 \
   and sales1>sales8 and sales1>sales9 and sales1>sales10:
   print('Stand 1 had the best sales')

'''
Storing and working with large amounts of data is difficult if we have to create a separate variable for each piece of data.
We need something better. We need to create a collection of data.

In Python we have several built in collection types.
The most common one is the list.
A list is an ordered collection of items.
We can create a list by enclosing a comma separated sequence of items in square brackets.
Lists can contain items of any type. We can have a list of numbers, a list of strings, a list of booleans, or even a list of lists.
Lists are mutable, which means we can change the contents of a list after it has been created.
We can add items to a list, remove items from a list, and change the value of items in a list.
'''