#1. Comprehension lists:
import random

# a. In one line - create a list of numbers from 105-95.

list10n: list[int] = [_ for _ in range(105, 94, -1)]; print(f'This is a reverse list: {list10n}')
print()

# b. In one line - create a list of even numbers from 10-20.
# That is: 10, 12, 14, 16, 18, 20

listeven: list[int] = [ _ for _ in range(10, 21, 2)]; print(f'This is list of even numbers: {listeven}')
print()

# c. In one line - create a list of 5 random elements of False True

fivelments = [random.choice([False, True]) for _ in range(5)]
print(f'This is a list of 5 random elements: {fivelments}')
print()

# d. In one line - create a list of 10 random numbers in the range 1-100

rlist: list[int] = [random.randint(1, 100) for _ in range(10)]
print(f'This is list of 10 random numbers: {rlist}')
print()

# e. In one line - from the list you created in the previous section, create a list containing only the numbers
# greater than 50

bigger50 = [ _ for _ in rlist if _ > 50]
print(f'This list contains numbers > 50 from list rlist: {bigger50}')
print()
# f.* Bonus: Can you do the previous 2 sections in one line?

concalist = [ x for x in (random.randint(1, 100) for _ in range(10)) if x > 50]
print(f'This is a concatenated list: {concalist} ')
print()

"""g.* Bonus: Accept strings from the user. In one line create a list containing all the letters
who typed except for the letter t and except for a space.
For example if the user entered masters python hello
- The answer will be the list: ['h', 'e', 'l', 'l', 'o', 'p', 'y', 'h', 'o', 'n', 'm', 'a', ' s', 'e', 'r', 's']"""

strlist = [letter for letter in input('Please enter a valid string: ') if letter != 't' if letter != ' ']
print(f'This is a list of strings: {strlist}')

# h. In one line - create a list of 10 random numbers in the range 10-99. Then Print the list

rlist2: list[int] = [random.randint(10, 100) for _ in range(10)]
print(f'This is list of 10 random numbers: {rlist2}')
print()

"""Now in one line - create a list of 10 numbers that will contain only the unity digit of
- The organs from the previous list. For example:
- If the first list was - 51, 19, 44, 99...
- The second list will be - 1, 9, 9, 1...."""

unitlist = [x % 10 for x in rlist and rlist2]
print(f'This is a list of unit digits: {unitlist}')