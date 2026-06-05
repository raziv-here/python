S={1,2,3,4}
# A set is a collection of unique items.
# unordered
students = {"Ram", "Shyam", "Hari" }
print(students)
print(type(students))
numbers  = {1, 2, 3, 3, 4, 4, 5}
print(numbers)
colors = {"red", "pink", "blue"}
print(colors)

# to add an item to a set, we can use the add() method
students = {"Shisam", "Nafisha"}
students.add("Rajeev")
print(students)

# to remove an item from a set, we use the remove() method
students.remove("Rajeev")
print(students)

# to clear a set, we use the clear()method
students.clear()
print(students)

for item in students:
    print(item)

# to convert a list to a set, we can use the set()function
nums = [1,2,2,3,3,4,4,5]

unique_nums = set(nums)
print(unique_nums)