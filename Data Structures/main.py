# Queue FIFO
print("QUEUE")
queue = []
print(queue)
# Add to the queue
print("Insert 1")
queue.append(1)
print(queue)
print("Insert 2")
queue.append(2)
print(queue)
print("Insert 3")
queue.append(3)
print(queue)
print("Get the queue's top")
# Get the first element
print(queue[0])
print("Remove the queue's top")
# Remove the first element
queue.pop(0)
print(queue)


print("------------------------------------")
# Stack LIFO
print("STACK")
stack = []
print(stack)
# Add to the stack
print("Insert 1")
stack.append(1)
print(stack)
print("Insert 2")
stack.append(2)
print(stack)
print("Insert 3")
stack.append(3)
print(stack)
print("Get the stack's top")
# Get the last element
print(stack[-1])
print("Remove the stack's top")
# Remove the last element
stack.pop()
print(stack)


# Sets
print("------------------------------------")
print("SET")
set = set()
print(set)
# Add to the set
print("Insert 1")
set.add(1)
print(set)
print("Insert 2")
set.add(2)
print(set)
print("Insert 3")
set.add(3)
print(set)
# Check if the element is in the set
print("Check if 2 is in the set")
print(2 in set)
# Remove from the set
print("Remove 3")
set.remove(3)
print(set)
# Other way to check if the element is in the set
print("Check if 3 is in the set")
if 3 in set:
    print(True)
else:
    print(False)


# Dictionary or Map
print("------------------------------------")
print("DICTIONARY OR MAP")
dict = {}
print(dict)
# Add to the dictionary
print("Insert 1")
dict["1"] = 1
print(dict)
print("Insert 2")
dict["2"] = 2
print(dict)
print("Insert 3")
dict["3"] = 3
print(dict)
# Check if the key is in the dictionary
print("Check if 2 is in the dictionary")
print("2" in dict)
# Remove from the dictionary
print("Remove 3")
dict.pop("3")
print(dict)
# Other way to check if the key is in the dictionary
print("Check if 3 is in the dictionary")
if "3" in dict:
    print(True)
else:
    print(False)

# List
print("------------------------------------")
print("LIST")
list = []
print(list)
# Add to the list
print("Insert 1")
list.append(1)
print(list)
print("Insert 2")
list.append(2)
print(list)
print("Insert 3")
list.append(3)
print(list)
# Check if the element is in the list
print("Check if 2 is in the list")
print(2 in list)
# Remove from the list
print("Remove 3")
list.remove(3)
print(list)
# Other way to check if the element is in the list
print("Check if 3 is in the list")
if 3 in list:
    print(True)
else:
    print(False)

# Diferences between List and Tuple
# List is mutable, Tuple is immutable
print("------------------------------------")
print("LIST VS TUPLE")
list = [1,2,3]
tuple = (1,2,3)
print(list)
print(tuple)
# Modify the list
print("Modify the list")
print("list[0] = 4")
list[0] = 4
print(list)
# Modify the tuple
# This will throw an error
print("You can't modify the tuple")
print("tuple[0] = 4, will throw an error")
# Add to the list
print("Insert 4")
list.append(4)
print(list)
# Add to the tuple
# This will throw an error
print("You can't add to the tuple")
print("tuple = tuple + (4,), will throw an error")
# Remove from the list
print("Remove 4")
list.remove(4)
print(list)
# Remove from the tuple
# This will throw an error
print("You can't remove from the tuple")
print("tuple.remove(4), will throw an error")
# Check if the element is in the list
print("Check if 2 is in the list")
print(2 in list)
# Check if the element is in the tuple
print("Check if 2 is in the tuple")
print(2 in tuple)
# Get element from the list
print("Get the first element from the list")
print(list[0])
# Get element from the tuple
print("Get the first element from the tuple")
print(tuple[0])

