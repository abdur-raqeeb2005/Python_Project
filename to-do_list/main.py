items = ["buy milk", "Do homework", "Clean the house", "Wash the car", "wash the dishes", "fold the clothes"]

type = input("Enter the tasks: ")
items.append(type)
print(items)

print("\nYour To-Do tasks: ")
for i in range(len(items)):
    print(str(i+1) + ".", items[i])



item = int(input("Which task number do you want to remove: "))
items.pop(item - 1)
print(items)

print("\nYour To-Do tasks: ")
for i in range(len(items)):
    print(str(i+1) + ".", items[i])
