# 1.Write a Python function to find the maximum of three numbers.
def s(a, b, c):
    return max(a, b, c)
print(s(1, 2, 3))

# 2.Write a Python function to sum all the numbers in a list.
def s(numbers):
    return sum(numbers)
print( s([1, 2, 3]))

# 3.Write a Python program to reverse a string.
def n(s):
    return s[::-1]
print(n("Mynameis"))

# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def sốnguyên(n):
    if n<1:
        return "Số phải là số nguyên không âm"
    r=1
    for i in range(1,n+1):
        r *=i
    return r
print(sốnguyên(5))

# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def nguyento(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(nguyento(1))
print(nguyento(7))

# 6.Write a Python function to print
# 1.all prime numbers that less than a number (enter prompt keyboard).
n=int(input("Nhập số n"))
for x in range(2,n):
    for i in range(2,x):
        if x % i == 0:
            break
    else:  print(x)
# 2.the first N prime numbers
n=int(input("Nhập số n"))
count=0
x=2
while count<n:
 for i in range(2,x):
    if x%i==0:
        break
 else:
    print(x)
    count+=1
 x+=1

# 7.Write a Python function to check whether a number is "Perfect" or not. Then print all perfect number that less than 1000.
# Số hoàn hảo (Perfect number) là số bằng tổng các ước số dương của nó (trừ chính nó).
def perfect(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n
for x in range(1,1000):
    if perfect(x):
        print(x)

# 8.Write a Python function to check whether a string is a pangram or not.
def pangram(s):
    s = s.lower()
    for i in "abcdifjhijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True
print(pangram("The quick brown fox jumps over the lazy dog"))