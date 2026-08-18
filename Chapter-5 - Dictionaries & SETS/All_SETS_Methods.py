"""
=========================================================
            PYTHON SET METHODS
=========================================================
"""

# =========================================================
# SET CREATION
# =========================================================

numbers = {10, 20, 30, 40, 50}

print("Original Set        :", numbers)

print("-" * 60)

# =========================================================
# ADD()
# =========================================================

temp = numbers.copy()

temp.add(60)

print("add()               :", temp)

print("-" * 60)

# =========================================================
# UPDATE()
# =========================================================

temp = numbers.copy()

temp.update([70, 80, 90])

print("update()            :", temp)

print("-" * 60)

# =========================================================
# REMOVE()
# =========================================================

temp = numbers.copy()

temp.remove(30)

print("remove()            :", temp)

# temp.remove(100)      # Raises KeyError

print("-" * 60)

# =========================================================
# DISCARD()
# =========================================================

temp = numbers.copy()

temp.discard(20)
temp.discard(100)      # No Error

print("discard()           :", temp)

print("-" * 60)

# =========================================================
# POP()
# =========================================================

temp = numbers.copy()

removed = temp.pop()

print("pop()               :", temp)
print("Removed Element     :", removed)

print("-" * 60)

# =========================================================
# CLEAR()
# =========================================================

temp = numbers.copy()

temp.clear()

print("clear()             :", temp)

print("-" * 60)

# =========================================================
# COPY()
# =========================================================

copy_set = numbers.copy()

print("copy()              :", copy_set)

print("-" * 60)

# =========================================================
# UNION()
# =========================================================

A = {1,2,3}
B = {3,4,5}

print("union()             :", A.union(B))
print("Using |             :", A | B)

print("-" * 60)

# =========================================================
# INTERSECTION()
# =========================================================

print("intersection()      :", A.intersection(B))
print("Using &             :", A & B)

print("-" * 60)

# =========================================================
# DIFFERENCE()
# =========================================================

print("difference()        :", A.difference(B))
print("Using -             :", A - B)

print("-" * 60)

# =========================================================
# SYMMETRIC DIFFERENCE()
# =========================================================

print("symmetric_difference():", A.symmetric_difference(B))
print("Using ^             :", A ^ B)

print("-" * 60)

# =========================================================
# INTERSECTION_UPDATE()
# =========================================================

temp = A.copy()

temp.intersection_update(B)

print("intersection_update :", temp)

print("-" * 60)

# =========================================================
# DIFFERENCE_UPDATE()
# =========================================================

temp = A.copy()

temp.difference_update(B)

print("difference_update   :", temp)

print("-" * 60)

# =========================================================
# SYMMETRIC_DIFFERENCE_UPDATE()
# =========================================================

temp = A.copy()

temp.symmetric_difference_update(B)

print("sym_diff_update     :", temp)

print("-" * 60)

# =========================================================
# ISDISJOINT()
# =========================================================

X = {1,2}

Y = {3,4}

print("isdisjoint()        :", X.isdisjoint(Y))

print("-" * 60)

# =========================================================
# ISSUBSET()
# =========================================================

small = {1,2}

large = {1,2,3,4}

print("issubset()          :", small.issubset(large))
print("Using <=            :", small <= large)

print("-" * 60)

# =========================================================
# ISSUPERSET()
# =========================================================

print("issuperset()        :", large.issuperset(small))
print("Using >=            :", large >= small)

print("-" * 60)

# =========================================================
# MEMBERSHIP
# =========================================================

print("20 in numbers       :", 20 in numbers)
print("100 in numbers      :", 100 in numbers)

print("-" * 60)

# =========================================================
# LENGTH
# =========================================================

print("len()               :", len(numbers))

print("-" * 60)

# =========================================================
# MAX MIN SUM
# =========================================================

print("max()               :", max(numbers))
print("min()               :", min(numbers))
print("sum()               :", sum(numbers))

print("-" * 60)

# =========================================================
# SORTING
# =========================================================

print("sorted()            :", sorted(numbers))

print("-" * 60)

# =========================================================
# ENUMERATE
# =========================================================

print("enumerate()")

for index, value in enumerate(numbers):
    print(index, value)

print("-" * 60)

# =========================================================
# SET COMPREHENSION
# =========================================================

square = {x*x for x in range(6)}

print("Comprehension       :", square)

print("-" * 60)

# =========================================================
# CONVERT LIST TO SET
# =========================================================

lst = [1,2,2,3,4,4,5]

print("List to Set         :", set(lst))

print("-" * 60)

# =========================================================
# CONVERT STRING TO SET
# =========================================================

text = "Programming"

print("String to Set       :", set(text))

print("-" * 60)

# =========================================================
# FROZENSET
# =========================================================

fs = frozenset([1,2,3])

print("Frozen Set          :", fs)

# fs.add(4)        # Error

print("-" * 60)

# =========================================================
# COMMON INTERVIEW PROGRAMS
# =========================================================

# Remove Duplicates

numbers = [1,2,2,3,3,4,5]

print("Remove Duplicates   :", list(set(numbers)))

print()

# Common Elements

A = {1,2,3,4}

B = {3,4,5,6}

print("Common Elements     :", A & B)

print()

# Unique Elements

print("Unique Elements     :", A ^ B)

print()

# Union

print("Union               :", A | B)

print()

# Difference

print("Difference          :", A - B)

print()

# Check Subset

print("Subset              :", {1,2}.issubset(A))

print()

# Check Superset

print("Superset            :", A.issuperset({1,2}))

print()

# Remove Duplicate Words

sentence = "python is easy python is powerful"

unique_words = set(sentence.split())

print("Unique Words        :", unique_words)

print("-" * 60)

print("************* END OF SET REVISION *************")