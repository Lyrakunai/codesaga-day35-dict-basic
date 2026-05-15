# Codesaga Day 35 - Dictionary Basics

# 1. Creating dictionary
student = {
    "name": "Asha",
    "age": 20,
    "marks": 95,
    "city": "Patna"
}
print(student["name"])
print(student["marks"])


# 2. Duplicate key behavior
data = {
    "a": 10,
    "a": 20
}
print(data)  


# 3. List as value
student_data = {
    "marks": [90, 80, 70]
}
print(student_data["marks"])


# 4. Tuple as key
data2 = {
    (1, 2): "hello"
}
print(data2[(1, 2)])


# 5. dict() function
data3 = dict(name="Riya", age=21)
print(data3)


# 6. Empty dictionary vs set
a = {}
b = set()
print(type(a))
print(type(b))