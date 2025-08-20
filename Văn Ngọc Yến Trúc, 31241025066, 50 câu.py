# 1. Write a Python program to calculate the length of a string.
# s=input("Nhap mot chuoi:")
# length=len(s)
# print("Length:",length)
from dataclasses import replace

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# s=input("Nhap mot chuoi:")
# result = s[:2] + s[-2:]
# if len(s) < 2:
#     print("empty string")
# else: print(result)

# 4.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# s=input("Nhap mot chuoi:")
# ketqua=s[0]+s[1:].replace(s[0],"$")
# print(ketqua)

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# s=input("Nhap mot chuoi:")
# y=input("Nhap mot chuoi khac:")
# sy=y[0]+s[1:]+ " "+s[0]+y[1:]
# print(sy)

# 6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# s=input("Nhap mot chuoi:")
# if len(s)<3:
#     print(s)
# else:
#     if s[-3:]=="ing": print(s+"ly")
#     else: print(s+"ing")

# 9. Write a Python program to remove the nth index character from a nonempty string.
# s=input("Nhap mot chuoi:")
# n=int(input("nhap thu tu can xoa"))
# print(s[:n]+s[n+1:])

# 10.Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# s=input("Nhap mot chuoi:")
# print(s[-1]+s[1:]+s[0])

# 11.Write a Python program to remove characters that have odd index values in a given string.
# s=input("Nhap mot chuoi:")
# for i in range(len(s)):
#     if i%2==0: print(s[i])

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# s=input("Nhap mot chuoi:")
# print(s.upper())
# print(s.lower())

# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# s=input("Nhap mot chuoi:")
# a=s[-2:]*4
# print(a)

# 18.Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# s=input("Nhap mot chuoi:")
# if len(s) <3: print(s)
# else: print(s[:3])

# 20.Write a Python function to reverse a string if its length is a multiple of 4.
# s=input("Nhap mot chuoi:")
# if len(s)%4==0:print(s[::-1])
# else: print(s)

# 21.Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
# s = input("Nhap mot chuoi: ")
# count = 0
# for c in s[:4]:
#     if c.isupper():
#         count += 1
# if count >= 2:print(s.upper())
# else:print(s)

# 22.Write a Python program to sort a string lexicographically.
# s = input("Nhap mot chuoi: ")
# a=sorted(s)
# print("".join(a))

# 23.. Write a Python program to remove a newline in Python.
# s = input("Nhap mot chuoi: ")
# print(s.replace(" ",""))

# 24.Write a Python program to check whether a string starts with specified characters
# s = input("Nhap mot chuoi: ")
# n= input("ki tu duoc chi dinh")
# if s[0]==n: print("yes")
# else:print("no")

# 30. Write a Python program to print the following numbers up to 2 decimal places.
# n=float(input("nhap so thap phan bat ki"))
# print(round(n, 2))

# 36. Write a Python program to format a number with a percentage.
# n=float(input("nhap so bat ki"))
# percent = n * 100
# print( str(percent) + "%")

# 38. Write a Python program to count occurrences of a substring in a string
# s = input("Nhap mot chuoi: ")
# a = input("Nhập chuỗi con cần đếm: ")
# count = s.count(a)
# print(count)

# 39. Write a Python program to reverse a string.
# s = input("Nhap mot chuoi: ")
# print(s[::-1])

# 41. Write a Python program to strip a set of characters from a string.
# s = input("Nhập chuỗi: ")
# a = input("Nhập các ký tự cần xóa: ")
# print( s.strip(a))

# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
# dai = float(input("Nhập chiều dài hình chữ nhật: "))
# rong = float(input("Nhập chiều rộng hình chữ nhật: "))
# r = float(input("Nhập bán kính hình trụ: "))
# h = float(input("Nhập chiều cao hình trụ: "))
# S = dai * rong
# V = 3.14 * r * r * h
# print("dien tích hình chữ nhật", S)
# print("Thể tích hình trụ", V)

# 44. Write a Python program to print the index of a character in a string. Sample string: w3resource
# s = input("Nhập chuỗi: ")
# for i in range(len(s)):
#    print("Current character", s[i], "position at", i)

# 46. Write a Python program to convert a given string into a list of words.
# s = input("Nhập chuỗi: ")
# words = s.split()
# print(words)

# 47. Write a Python program to lowercase the first n characters in a string
# s = input("Nhập chuỗi: ")
# n= int(input("so ki tu muon thanh chu thuong"))
# a= s[:n].lower()+s[n:]
# print(a)

# 48. Write a Python program to swap commas and dots in a string.
# s = input("Nhập chuỗi: ")
# s=s.replace("." , "#")
# s=s.replace(",", ".")
# s=s.replace("#", ",")
# print(s)

# 57.Write a Python program to remove spaces from a given string.
# s = input("Nhập chuỗi: ")
# xoa=s.replace(" ", "")
# print(xoa)

# 60. Write a Python program to capitalize the first and last letters of each word in a given string.
# s = input("Nhập chuỗi: ")
# if len(s)==1: print(s.upper())
# else: print(s[0].upper()+s[1:-1]+s[-1].lower())


