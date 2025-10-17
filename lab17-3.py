from collections import namedtuple as nt

Student = nt('Student', ['Name', 'Age', 'Grade'])
s1 = Student("Alice", 20, "A")
print(s1)