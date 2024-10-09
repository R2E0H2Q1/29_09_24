# #Create a list of even numbers 2, 4, 6, 8 ... 20
import random
#
# even_num: list[int] = [i for i in range(2, 21, 2)]
# print(f'These are the even numbers: {even_num}')
#
# #Create a list of numbers in reverse 99, 96, 93, ...60
#
# numbers: list[int] = [i for i in range(99, 60 -1, -3)]
# print(f'This is a list of numbers in reverse order: {numbers}')
#
# #Bonus: Create a list of 10 random numbers 1 - 100.
#
# ran_num: list[int] = [random.randint(1, 100) for _ in range(10)]
# print(f'This is a list of random numbers: {ran_num}')
#
# #insert 3 numbers from the user
# numbers_user: list[int] = [int(input('Please enter a number: ')) for _ in range(3)]
# print(f'This is a list of 3 numbers from the user: {numbers_user}')

#a. Create a list of 10 numbers between -50 to 50.

list_a: list[int] = [random.randint(-50, 50) for _ in range(10)]
print(f'This is list a: {list_a}')

#b. Create a list from the list created on a and add only the even numbers.

list_blong: list[int] = []
for num in list_a:
    if num % 2 == 0:
        list_blong.append(num)
print(f'This is list b long way: {list_blong}')

list_b: list[int] = [num for num in list_a if num %2 == 0]
print(f'This is list b, the short way: {list_b}')

#c. Create a list from the list you created in a and add only the positive numbers.

list_c: list[int] = [num for num in list_a if num > 0]
print(f'This is list c(only positive numbers), the short way: {list_c}')

