# # ch = input("enter any world or sentence")
# # if ch in 'aeiouAEIOU':
# #     print("Vowel")
# # elif ch.isalpha():
# #     print("consonent")
    
# # else:
# # #     print("not a letter") 

# year = int(input("Enter year"))
# if year % 4 == 0 and year % 100 != 0 :
#     print("Leap year")
# else :
#     print("not a leap year")

# i = 2
# while i <= 50:
#     print(i)
#     i+= 2

# n = int(input("Enter n: "))
# sum = 0
# for i in range( 1, n+1):
#     sum = sum + i
# print("sum is: ", sum)

# n = int(input("Enter any number"))
# fact = 1
# for i in range(1 , n+1):
#     fact = fact * i
# print("factorial is: ", fact)

# num = int(input("enter any number"))
# rev = 0
# while num > 0:
#     rev = rev*10 + num%10
#     num //= 10
# print("Reverse of a number is: ", rev)


# num = int(input("Enter any number: "))

# if num > 0 :
#     print("Positive")
# elif num < 0:
#     print("Negative")
# elif num == 0:
#     print("Zero")
# else:
#     print("please enter valid integer number")

# char = input("ENter any charecter")
# if char.isupper():
#     print("Charecter is Upper")
# elif char.islower():
#     print("charecter is Lower")
# elif char.isdigit():
#     print("charecter is digit")
# else:
#     print("Charecter is special charecter")

# a = int(input("Enter 1st Number: "))
# b = int(input("Enter 2nd Number: "))

# print("Greater Number is: ", a if a > b else b)

# i = 2
# while i <= 50:
#     i += 2
#     print(i)

# for i in range (1 , 11):
#     print(i * 5)

# n = 'Ayush sharma'
# for ch in n:
#     print(ch)

# digit = 9141
# count = 0
# while digit > 0:
#     count = count + 1
#     digit //= 10
# print(count)

# s = "hello world"
# for ch in s:
#     if ch in "aeiouAEIOU":
#         print(ch, end=" ")

# total = 6582
# sum = 0
# while total > 0 :
#     sum += total %10
#     total //= 10
# print(sum)

# arr = [10,20,30,40,50]
# print("Array elements are: ")
# for i in arr:
#     print(i)

# # arr = [1,4,5,6,8]
# # arr. insert(0,199)
# # print(arr)

# arr = [10,20,65,13,65,84]
# arr.remove(20)
# print(arr)
# print(max(arr))
# print(min(arr))
# key = 10

# found = False
# for i in arr:
#     if i == key:
#         found = True
#         break
# if found:    
#     print("key is found")
# else: 
#     print("key not found")

# arr = [10,20,40]
# print(max(arr))
# print(max(arr))

# a = 896
# b = 896
# c = 896

# if a > b:
#     if a > c:
#         print("a is largest.")
#     else:
#         print("c is largest.")
# else:
#     if b > a:
#         if b > c:
#             print("b is largest")
#         else:
#             print("c is largest")
#     else:
#         if a == b == c:
#             print("same size")

# year = 2028
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not a leap year")
#     else:
#         print("leap year")
# else:
#     print("not a leap year")

# text = 'Mercy'
# # for ch in text:
# #     print(ch)

# num = int(input("enter any number"))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10
# print("Sum of digits", sum)
   
# ayush = [10,20,30,40,50,10, 10, 10, 20 ,20 ,20 ,30 , 30, 50, 50, 50, 50]
# total = sum(ayush)
# average = total / len(ayush)
# print(total)
# print(average)
# print(max(ayush))
# print(min(ayush))
# x = 10
# count = ayush.count(x)
# print((f"{x} appears (count) times" ))

# i = 10
# while i >= 1:
#     print(i , end="  ")
#     i = i - 1

# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print(fact)

# num = 12345
# count = 0
# while num > 0:
#     num //= 10
#     count = count + 1
# print(count)
    
    
# for i in range(1,10):
#     for j in range(i):
#         print("*", end=" ")
# #     print()

# for i in range ( 1 , 50):
#     for j in range(1, i+1):
#         print(j, end=" ")
# #     print()
        
# for i in range(4, 0, -1):
#     for j in range(i, 0, -1):
#         print(j,end=" ")
#     print ()
    
# rows = 5
# for i in range(1, rows + 1):
#     print(" "* (rows - i)+ "* " * i)


# def greet(name):
#     print("Hello",name)
    
# greet("Mercy")


# def sum(a,b):
#     return a + b

# result = sum(5, 3)
# print(result)
    
# def even_odd(a):
#     if a % 2 == 0:
# #         print("even")
# #     else:
#         print("Odd")
        
# even_odd(10)

# def fact(a):
#     result = 1
#     for i in range(1, a+1):
#         result = result * i
#         print (result)
# fact(5)

# def square_list(list):
#     return[x**2 for x in list]
# print(square_list([1,2,3,4,5]))


# rows = 4 
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "* " * i)


# rows = 4
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "* " * i)

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(65, 69):
#     print((chr(i) + " ") * (i - 64))

# i = 1
# while i <= 3:
#     print("* " * i)
#     i+= 1

# for i in range(65, 69):
#     print((chr(i) + " ")* (i - 64))

# for i in range(1, 5):
#     num = 1
#     for j in range(i):
#         print(num, end=" ")
#         num += 2
#     print()

# count = 1
# for i in range(1,5):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()

# num = 1
# for i in range(1,6):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# char = 65
# for i in range(1,5):
#     for j in range(i):
#         print(chr(char), end=" ")
#         char = char + 1
#     print()

# for i in range(4,0,-1):
#     print((chr(64 + i) + " ") * i)
    
# n = 4 
# for i in range(1, n+1):
#     print(" " * (n - 1) + "* " * i)   

# n = 1
# for i in range(69,71):
#     for j in range(i):
#         print(n,end=" ")
#         n+= 1
#     print()

# num = 1 
# n = 4 
# for i in range(1, n+1):
#     print(" " * (n-1), end=" ")
#     for j in range(i):
#         print(num, end=" ")
# #         num += 1
# #     print()


# for i in range(4):
#     for j in range(65,69):
#         print(chr(j),end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(64+i, 64, -1):
#         print(chr(j),end=" ")
#     print()

# n = 11   # 11 rows and 11 columns 
# for i in range(n): # 
#     for j in range(n):
#         if j == i or j == n - i - 1:
#             print("*",end="")
#         else:
#             print(" ", end="")
#     print()

# def add(a,b):
#     return a + b
# print(add(5,7))

# num = int(input("enter any number"))
# print("Square is: ", num ** 2)

# def Even_Odd(n):
#     if n % 2 == 0:
#         print("Number is Even")
#     else:
#         print("Number id Odd")
# num = int(input("Enter any number: "))
# Even_Odd(num)

# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#         print(result)
# fact(5)

# def find_max(a,b):
#     return a if a > b else b
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# print(find_max(a,b))

# def return_reverse(s):
#     return s[::-1]
# print(return_reverse('mercy'))


# def simple_int(p,r,t):
#     return p * r * t / 100
# p = int(input("Enter Principle: "))
# r = int(input("Enter Rate: "))
# t = int(input("Enter Time: "))

# print(simple_int(p,r,t))

# a = int(input("enter any number"))
# b = int(input("enter any number"))
# print(a + b)

# def prime_num(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# print(prime_num(4))
        
# def max_num(a,b):
#     return a if a > b else b
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# # print(max_num(a,b))

# def reverse_string(s):
#     return s[::-1]
# print(reverse_string('Mercy'))

# def palindrome(s):
#     return s == s[::-1]

# print(palindrome('madam'))

# nums = [50,69,45,70,36,98]
# for num in nums:
#     print(num,end=" ")
    
# user_list = []
# for i in range(5):
#     val = int(input("Enter numbers {i+1}:"))
#     user_list.append(val)
# print("your list:", user_list)

# list= [5,5,5,5,4,4,4,8,8,9,6,6,5,6]
# print("Repeated number:",list.count(5))

# nums = [11,22,33,44,55,66,77,88,99,100]
# nums[2:4]= [300,400]
# print(nums)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
# print(matrix[1][2])
# for coloumn in matrix:
#     print(coloumn)

# for row in matrix:
#     for item in row:
#         print(item,end=" ")
        
# matrix[2][1]= 5000
# print(matrix)


matrix = []
for i in range(3):
    row= []
    for i in range(3):
        val = int(input("Enter values:"))
        row.append(val)
    matrix.append(row)
print("Matrix:")
for r in matrix:
    print(r)




























