#1.Create a list of 5 of your favorite fruits. Print the list.
fruits = ['mango', 'banana', 'apple', 'orange', 'watermelon']
print(fruits)
print()
#2.Given the list colors = ['red', 'blue', 'green', 'yellow', 'purple'], print the first, third, and last color in the list.
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("First element:", colors[0])
print("Third elemment:", colors[2]) 
print("Last element:", colors[4])
print()
#3.Create a list numbers with values [10, 20, 30, 40, 50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list.
values = [10, 20, 30, 40, 50]
values[1] = 25
values .append(60)
print(values)
print()
#4.Using the list names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma'], create a new list subset containing only the first three names. Print subset.
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = (names[:3])
print(subset)
print()
#5.Create a list of numbers from 1 to 10 and use a loop to print each number squared.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in list1:
    print(number ** 2)
print()
#6.Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list.
shopping_cart = []
shopping_cart .append('milk')
shopping_cart .append('bread')
shopping_cart .append('eggs')
shopping_cart .extend('butter')
shopping_cart .extend('cheese')
print(shopping_cart)
print()
#7.Write a program to find the maximum and minimum values in the list numbers = [45, 22, 88, 56, 92, 33].
numbers = [45, 22, 88, 56, 92, 33]
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print()
#8.Given the list letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd'], count how many times the letter 'a' appears in the list.
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_a = letters.count('a')
print("times a gets repeated:", count_a)
print()
#9.Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.
evens = [x**2 for x in range(11) if x % 2 == 0]
print(evens)
print()
#10.Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)
print()
 