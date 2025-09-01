# 1. Write a  Python program to sum all the items in a list.
# N = int(input("Nhập các số"))
# n = []
# for i in range (N):
#     x = int(input(f"Nhập các phần tử: "))
#     n.append(x)
# tong = 0
# for num in n:
#     tong += num
# print("tổng các phần tử", tong)

# 2. Write a  Python program to multiply all the items in a list.
# N = int(input("Nhập các số"))
# n = []
# for i in range (N):
#     x = int(input(f"Nhập các phần tử: "))
#     n.append(x)
# nhan = 1
# for num in n:
#     nhan *= num
# print("nhân các phần tử", nhan)

# 3. Write a Python program to get the largest number from a list.
# N = int(input("Nhập các số"))
# n = []
# for i in range (N):
#     x = int(input(f"Nhập các phần tử: "))
#     n.append(x)
# print("Phần tử lớn nhất là ", max(n))

# 4. Write a Python program to get the smallest number from a list.
# N=int(input("Bạn muốn bao nhiêu phần tử"))
# n=[]
# for i in range(N):
#     x=int(input("Nhập các phần tử"))
#     n.append(x)
# print("Phần tửu nhỏ nhất là ", min(n))

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# def giong_nhau (n):
#     if len(n)>=2 and n[0]==n[-1]:
#         return True
#     else:
#         return False
# def ket_qua():
#     N = int(input("Bạn muốn bao nhiêu phần tử"))
#     n = []
#     for i in range(N):
#         x=input("Nhập các phần tử")
#         n.append(x)
#     dem=0
#     for j in n:
#         if giong_nhau(j): dem+=1
#     print("các phần tử có đầu cuối giống nhau", dem)
# ket_qua()

# 7. Write a  Python program to remove duplicates from a list.
# n=input("Nhập các kí tự")
# xoa=set(n)
# print(xoa)

# 8. Write a  Python program to check if a list is empty or not.
# n=input("Nhập các kí tự")
# if not n: print("rỗng")
# else: print(n)

# 9. Write a Python program to clone or copy a list.
# n=input("Nhập các kí tự").split()
# saochep=n.copy()
# print(saochep)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
# w=input("Nhập các kí tự").split()
# n=int(input("nhập số kí tự bạn muốn"))
# long_words = []
# for x in w:
#     if len(x) > n:
#         long_words.append(x)
# print(long_words)

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# w=input("Nhập các kí tự")
# n=input("Nhập các kí tự")
# flag = False
# for i in w:
#     for j in n:
#         if i == j:
#             flag = True
# print(flag)

# 14. Write a  Python program to print the numbers of a specified list after removing even numbers from it.
# N=int(input("Bạn muốn bao nhiêu số"))
# n=[]
# for i in range(N):
#     x=int(input("Nhập các số"))
#     n.append(x)
# for x in n:
#     if x%2!=0: print(x)

# 15. Write a Python program to shuffle and print a specified list.
# import random
# N=int(input("Bạn muốn bao nhiêu phần tử"))
# n=[]
# for i in range(N):
#     x=int(input("Nhập các phần tử"))
#     n.append(x)
# random.shuffle(n)
# print("Danh sách các kí tự đã xáo trộn", n)

# 18. Write a  Python program to generate all permutations of a list in  Python.
# import itertools
# n=input("nhập các phần tử"). split()
# x=list(itertools.permutations(n))
# for p in x:
#     print (p)

# 19. Write a Python program to calculate the difference between the two lists.
# n1=input("nhập các phần tử danh sách 1: "). split()
# n2=input("nhập các phần tử danh sách 2: "). split()
# r=[]
# for i in n1:
#     if i not in n2: r.append(i)
# for i in n2:
#     if i not in n1: r.append(i)
# print(r)

# 21. Write a Python program to convert a list of characters into a string.
# list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# r=" ".join(list)
# print(r)

# 25. Write a Python program to select an item randomly from a list.
# import random
# n=input("nhập các phần tử"). split()
# i=random.choice(n)
# print(i)

# 27. Write a  Python program to find the second smallest number in a list.
# n=int(input("Bạn muốn bao nhiêu số"))
# N=[]
# for i in range(n):
#     s=int(input("Nhập các số"))
#     N.append(s)
# x=sorted(N)
# print(x[1])

# 28. Write a Python program to find the second largest number in a list.
# n=int(input("Bạn muốn bao nhiêu số"))
# N=[]
# for i in range(n):
#     s=int(input("Nhập các số"))
#     N.append(s)
# x=sorted(N)
# print(x[-2])

# # 30. Write a Python program to get the frequency of elements in a list.
# n=input("nhập các phần tử"). split()
# s={}
# for i in n:
#     s[i]=n.count(i)
# print(s)

# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# s= input("Nhập các phần tử: ").split()
# n = int(input("Nhập số n: "))
# result = []
# for i in range(1, n+1):
#     for j in s:
#         result.append(j + str(i))
# print(result)

# 37. Write a  Python program to find common items in two lists.
# s= input("Nhập các phần tử: ").split()
# x= input("Nhập các phần tử: ").split()
# c=[]
# for i in s:
#     if i in x and i not in c:
#         c.append(i)
# print(c)

# 39. Write a Python program to convert a list of multiple integers into a single integer.
# n=input("Nhập các số cách nhau bởi dấu cách").split()
# r=int("".join(n))
# print(r)

# 41. Write a  Python program to create multiple lists.
# n=int(input("Bạn muốn tạo bao nhiêu list"))
# s=[[]for _ in range(n)]
# print(s)

# 47. Write a Python program to insert an element before each element of a list.
# n=input("Nhập các kí tự").split()
# x=input("Nhập phần tử muốn chèn")
# r=[]
# for i in n:
#     r.append(x)
#     r.append(i)
# print(r)

# 58. Write a  Python program to replace the last element in a list with another list.
# n1=input("Nhập các kí tự").split()
# n2=input("Nhập các kí tự").split()
# n1[-1]=n2
# print(n1)

# 63. Write a  Python program to insert a given string at the beginning of all items in a list.
# n=input("Nhập các kí tự").split()
# x=input("Nhập phần tử muốn chèn")
# r=[]
# for i in n:
#     r.append(x+str(i))
# print(r)








