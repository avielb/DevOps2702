# importing the module
import ast

# reading the data from the file
with open('dict.txt') as moshe:
    data = moshe.read()
    print(data)
    d = ast.literal_eval(data)

print(f"name: {d['name']}, age: {d['age']}")