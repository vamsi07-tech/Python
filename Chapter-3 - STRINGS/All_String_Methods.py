"""
====================================================
        PYTHON STRING METHODS
====================================================
"""

# Sample String
s = "  Hello Python World  "
print("Original String :", repr(s))
print("-" * 60)

# ====================================================
# CASE CONVERSION METHODS
# ====================================================

print("upper()        :", s.upper())          # Convert to uppercase
print("lower()        :", s.lower())          # Convert to lowercase
print("capitalize()   :", s.capitalize())     # First letter capital
print("title()        :", s.title())          # Capitalize every word
print("swapcase()     :", s.swapcase())       # Swap upper/lower case
print("casefold()     :", s.casefold())       # Aggressive lowercase

print("-" * 60)

# ====================================================
# WHITESPACE METHODS
# ====================================================

print("strip()        :", repr(s.strip()))    # Remove both sides spaces
print("lstrip()       :", repr(s.lstrip()))   # Remove left spaces
print("rstrip()       :", repr(s.rstrip()))   # Remove right spaces

print("-" * 60)

# ====================================================
# SEARCH METHODS
# ====================================================

text = "Python Programming"

print("find('Pro')    :", text.find("Pro"))       # Returns index
print("find('Java')   :", text.find("Java"))      # Returns -1

print("index('Pro')   :", text.index("Pro"))      # Returns index

# print(text.index("Java"))      # Raises ValueError

print("count('m')     :", text.count("m"))        # Count occurrences

print("-" * 60)

# ====================================================
# REPLACE
# ====================================================

print("replace()      :", text.replace("Python", "Java"))

print("-" * 60)

# ====================================================
# STARTS / ENDS
# ====================================================

filename = "report.pdf"

print("startswith()   :", filename.startswith("rep"))
print("endswith()     :", filename.endswith(".pdf"))

print("-" * 60)

# ====================================================
# SPLIT & JOIN
# ====================================================

sentence = "Python is easy to learn"

words = sentence.split()

print("split()        :", words)

csv = "A,B,C,D"

print("split(',')     :", csv.split(","))

joined = "-".join(words)

print("join()         :", joined)

print("-" * 60)

# ====================================================
# PARTITION
# ====================================================

email = "user@gmail.com"

print("partition()    :", email.partition("@"))
print("rpartition()   :", email.rpartition("@"))

print("-" * 60)

# ====================================================
# JUSTIFICATION
# ====================================================

word = "Python"

print("center()       :", word.center(20, "-"))
print("ljust()        :", word.ljust(20, "-"))
print("rjust()        :", word.rjust(20, "-"))
print("zfill()        :", "25".zfill(6))

print("-" * 60)

# ====================================================
# BOOLEAN METHODS
# ====================================================

print("'abc'.isalpha()        :", "abc".isalpha())
print("'123'.isdigit()        :", "123".isdigit())
print("'123'.isdecimal()      :", "123".isdecimal())
print("'123'.isnumeric()      :", "123".isnumeric())
print("'abc123'.isalnum()     :", "abc123".isalnum())
print("'HELLO'.isupper()      :", "HELLO".isupper())
print("'hello'.islower()      :", "hello".islower())
print("'Hello World'.istitle():", "Hello World".istitle())
print("' '.isspace()          :", " ".isspace())
print("'abc'.isascii()        :", "abc".isascii())
print("'my_var'.isidentifier():", "my_var".isidentifier())
print("'Hello'.isprintable()  :", "Hello".isprintable())

print("-" * 60)

# ====================================================
# ENCODING
# ====================================================

print("encode()       :", "Python".encode())

print("-" * 60)

# ====================================================
# TRANSLATE
# ====================================================

translation_table = str.maketrans("aeiou", "12345")

print("maketrans()    :", translation_table)

print("translate()    :", "education".translate(translation_table))

print("-" * 60)

# ====================================================
# SPLITLINES
# ====================================================

multiline = "Line1\nLine2\nLine3"

print("splitlines()   :", multiline.splitlines())

print("-" * 60)

# ====================================================
# FORMATTING
# ====================================================

name = "Vamsi"
age = 25

print("format()       :", "My name is {} and I am {} years old".format(name, age))

print("f-string       :", f"My name is {name} and I am {age} years old")

print("-" * 60)

# ====================================================
# FORMAT_MAP
# ====================================================

student = {
    "name": "Vamsi",
    "city": "Hyderabad"
}

print("format_map()   :", "Name: {name}, City: {city}".format_map(student))

print("-" * 60)

# ====================================================
# EXPANDTABS
# ====================================================

tab_text = "Python\tJava\tC++"

print("Original       :", tab_text)
print("expandtabs()   :", tab_text.expandtabs(20))

print("-" * 60)

# ====================================================
# RFIND / RINDEX
# ====================================================

sample = "banana"

print("rfind('a')     :", sample.rfind("a"))
print("rindex('a')    :", sample.rindex("a"))

print("-" * 60)

# ====================================================
# STRING IMMUTABILITY
# ====================================================

x = "Python"

print("Original       :", x)

x = x.replace("P", "J")

print("Modified       :", x)

print("-" * 60)

# ====================================================
# STRING COMPARISON
# ====================================================

print("'abc' == 'ABC' :", "abc" == "ABC")
print("'abc'.lower()== 'ABC'.lower():", "abc".lower() == "ABC".lower())

print("-" * 60)

# ====================================================
# MEMBERSHIP
# ====================================================

print("'Python' in sentence :", "Python" in sentence)
print("'Java' in sentence   :", "Java" in sentence)

print("-" * 60)

# ====================================================
# STRING REVERSAL
# ====================================================

print("Reverse        :", sentence[::-1])

print("-" * 60)

print("************ END OF STRING REVISION ************")