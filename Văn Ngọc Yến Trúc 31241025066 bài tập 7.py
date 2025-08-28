# # 1.Write python program:
# # a) Convert two lists into a dictionary
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# dict_a = dict(zip(keys, values))
# print("Convert lists to dict:", dict_a)
#
# # b) Merge two Python dictionaries into one
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged_dict = {**dict1, **dict2}
# print("Merged dict:", merged_dict)
#
# # c) Print the value of key ‘history’
# d = {"marks": {"physics": 70, "history": 80}}
# print(d["marks"]["history"])
#
# # d) Initialize dictionary with default values
# names = ["John", "Emma"]
# defaults = {"role": "Marketing"}
# print(dict.fromkeys(names, defaults))
#
# # e) Extract some keys from dictionary
# d = {"a": 1, "b": 2, "c": 3}
# print({k: d[k] for k in ["a", "c"]})
#
# # f) Delete list of keys
# d = {"name": "Kelly", "age": 25, "salary": 8000}
# for k in ["name", "salary"]:
#     d.pop(k)
# print(d)
#
# # g) Check if a value exists
# d = {"a": 100, "b": 200}
# print(200 in d.values())
#
# # h) Rename key
# d = {"name": "Kelly", "city": "NY"}
# d["location"] = d.pop("city")
# print(d)
#
# # i) Get key of min value
# d = {"Math": 65, "History": 75}
# print(min(d, key=d.get))
#
# # j) Change nested value
# d = {"emp1": {"salary": 7500}, "emp2": {"salary": 6500}}
# d["emp2"]["salary"] = 8500
# print(d)
#
# # 2.Write a Python program that counts the number of times characters appear in a text paragraph.
# text = "Hello world! Python is fun."
# count_dict = {}
# for char in text:
#     if char != " ":
#         count_dict[char] = count_dict.get(char, 0) + 1
# print("Character count:", count_dict)
#
# # 3.Write a program using a dictionary containing keys starting from 1 and values containing prime numbers less than a value N.
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# N = 20
# primes = [x for x in range(2, N) if is_prime(x)]
#
# prime_dict = {i+1: primes[i] for i in range(len(primes))}
# print("Prime dict:", prime_dict)

# Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

dept_employees = {}
for emp_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees:
        dept_employees[dept] = {}
    dept_employees[dept][emp_id] = {"name": info["name"], "salary": info["salary"]}
print(dept_employees)