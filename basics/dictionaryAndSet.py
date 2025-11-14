# dictionary 
info = {
    "key": "value",
    "name": "vishal",
    "learning": "coding",
    "age": 19,
    "is_adult": True
}

# print(info)

info2 = {
    "name": "apnacollege",
    "subjects": ["python", "C", "javaScript"],
    "topics": ("dict", "set"),
    "age": 19,
    "is_adult": True,
    "marks": 94.5
}
info2["subjects"][0] = "java"
# print(info2)
# print(info2["subjects"])
# print(info2["subjects"][0])

# nested dictionary

student = {
    "name": "vishal",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}

# print(student["subjects"]["chem"])
# print(student.keys())
# print([student.keys()])

# print(student.values())
# print(list(student.values()))

# print(student.items())
# print(student.get("name"))  # returns the key according to value

# student.update({"city": "delhi"})

# print(student)

# Sets 

collection = {1,2,2,4,5,3,4, "hello"}  # duplicate value not allowed
collection2 = set() #empty set

collection2.add(1)
collection2.add(2)

# print(collection2)
# print(collection)
# print(type(collection))

py_dict = {
    "table": ("a piece of furniture", "list of facts & figures"),
    "cat": "a small animal"
}