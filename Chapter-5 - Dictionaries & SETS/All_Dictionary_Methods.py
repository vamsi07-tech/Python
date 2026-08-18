"""
=========================================================
        PYTHON DICTIONARY METHODS - ONE GO REVISION
=========================================================
"""

# =========================================================
# DICTIONARY CREATION
# =========================================================

student = {
    "name": "Vamsi",
    "age": 25,
    "city": "Hyderabad"
}

print("Original Dictionary :", student)

print("-" * 60)

# =========================================================
# ACCESSING VALUES
# =========================================================

print("Using Key           :", student["name"])
print("Using get()         :", student.get("age"))

# get() returns None if key not found
print("Key Not Present     :", student.get("salary"))

print("-" * 60)

# =========================================================
# ADD NEW KEY-VALUE PAIR
# =========================================================

student["salary"] = 50000

print("Added Salary        :", student)

print("-" * 60)

# =========================================================
# UPDATE EXISTING VALUE
# =========================================================

student["age"] = 26

print("Updated Age         :", student)

print("-" * 60)

# =========================================================
# UPDATE()
# =========================================================

student.update({
    "city": "Bangalore",
    "experience": 3
})

print("update()            :", student)

print("-" * 60)

# =========================================================
# KEYS()
# =========================================================

print("keys()              :", student.keys())

print("-" * 60)

# =========================================================
# VALUES()
# =========================================================

print("values()            :", student.values())

print("-" * 60)

# =========================================================
# ITEMS()
# =========================================================

print("items()             :", student.items())

print("-" * 60)

# =========================================================
# ITERATING DICTIONARY
# =========================================================

print("Iterating Keys")

for key in student:
    print(key)

print()

print("Iterating Values")

for value in student.values():
    print(value)

print()

print("Iterating Key-Value")

for key, value in student.items():
    print(key, ":", value)

print("-" * 60)

# =========================================================
# POP()
# =========================================================

temp = student.copy()

removed = temp.pop("experience")

print("pop()               :", temp)
print("Removed Value       :", removed)

print("-" * 60)

# =========================================================
# POPITEM()
# =========================================================

temp = student.copy()

item = temp.popitem()

print("popitem()           :", temp)
print("Removed Item        :", item)

print("-" * 60)

# =========================================================
# SETDEFAULT()
# =========================================================

temp = student.copy()

temp.setdefault("Country", "India")

print("setdefault()        :", temp)

print("-" * 60)

# =========================================================
# FROMKEYS()
# =========================================================

keys = ["Math", "Science", "English"]

marks = dict.fromkeys(keys, 0)

print("fromkeys()          :", marks)

print("-" * 60)

# =========================================================
# COPY()
# =========================================================

copy_dict = student.copy()

print("copy()              :", copy_dict)

print("-" * 60)

# =========================================================
# CLEAR()
# =========================================================

temp = student.copy()

temp.clear()

print("clear()             :", temp)

print("-" * 60)

# =========================================================
# MEMBERSHIP
# =========================================================

print("'name' in student   :", "name" in student)
print("'salary' in student :", "salary" in student)
print("'phone' in student  :", "phone" in student)

print("-" * 60)

# =========================================================
# LENGTH
# =========================================================

print("len()               :", len(student))

print("-" * 60)

# =========================================================
# DELETE USING del
# =========================================================

temp = student.copy()

del temp["salary"]

print("del                 :", temp)

print("-" * 60)

# =========================================================
# MERGING DICTIONARIES
# =========================================================

d1 = {"A":1,"B":2}
d2 = {"C":3,"D":4}

merged = d1 | d2       # Python 3.9+

print("Merge (|)           :", merged)

print("-" * 60)

# =========================================================
# NESTED DICTIONARY
# =========================================================

employees = {

    "E101":{

        "Name":"Vamsi",

        "Age":25
    },

    "E102":{

        "Name":"Rahul",

        "Age":28
    }

}

print("Nested Dictionary   :", employees)

print("Employee Name       :", employees["E101"]["Name"])

print("-" * 60)

# =========================================================
# DICTIONARY COMPREHENSION
# =========================================================

square = {x:x*x for x in range(1,6)}

print("Comprehension       :", square)

print("-" * 60)

# =========================================================
# SORTING DICTIONARY
# =========================================================

marks = {

    "Math":80,

    "Science":95,

    "English":70
}

print("Sorted Keys         :", dict(sorted(marks.items())))

print("-" * 60)

# =========================================================
# MAX / MIN
# =========================================================

print("Max Key             :", max(marks))
print("Min Key             :", min(marks))

print("Max Value           :", max(marks.values()))
print("Min Value           :", min(marks.values()))

print("-" * 60)

# =========================================================
# UPDATE MULTIPLE VALUES
# =========================================================

temp = student.copy()

temp.update({
    "Age":30,
    "City":"Pune",
    "Role":"Python Developer"
})

print("Multiple Update     :", temp)

print("-" * 60)

# =========================================================
# COMMON INTERVIEW PROGRAMS
# =========================================================

# Character Frequency

text = "programming"

frequency = {}

for ch in text:

    frequency[ch] = frequency.get(ch,0)+1

print("Character Frequency :", frequency)

print()

# Word Frequency

sentence = "python is easy python is powerful"

word_count = {}

for word in sentence.split():

    word_count[word] = word_count.get(word,0)+1

print("Word Frequency      :", word_count)

print()

# Invert Dictionary

data = {

    "A":1,

    "B":2,

    "C":3
}

inverse = {}

for key,value in data.items():

    inverse[value]=key

print("Invert Dictionary   :", inverse)

print()

# Merge Two Dictionaries

dict1 = {"A":1}

dict2 = {"B":2}

print("Merged Dictionary   :", dict1 | dict2)

print()

# Dictionary Equality

d1 = {"A":1,"B":2}

d2 = {"B":2,"A":1}

print("Dictionary Equal    :", d1==d2)

print("-" * 60)

# =========================================================
# SHALLOW COPY
# =========================================================

original = {

    "student":{

        "name":"Vamsi"

    }

}

shallow = original.copy()

shallow["student"]["name"]="Rahul"

print("Original            :", original)

print("Shallow Copy        :", shallow)

print("-" * 60)

# =========================================================
# DEEP COPY
# =========================================================

import copy

original = {

    "student":{

        "name":"Vamsi"

    }

}

deep = copy.deepcopy(original)

deep["student"]["name"]="Krishna"

print("Original            :", original)

print("Deep Copy           :", deep)

print("-" * 60)

print("************ END OF DICTIONARY REVISION ************")