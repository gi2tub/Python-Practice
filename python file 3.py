

# Create a list
my_list = [1, 2, 3, 4, 5]

# Print the list
print(my_list)

# Access an element in the list
print(my_list[0])  # prints 1

# Add an element to the list
my_list.append(6)
print(my_list)  # prints [1, 2, 3, 4, 5, 6]

# Remove an element from the list
my_list.remove(4)
print(my_list)  # prints [1, 2, 3, 5, 6]

# Update an element in the list
my_list[0] = 10
print(my_list)  # prints [10, 2, 3, 5, 6]

# Get the length of the list
print(len(my_list))  # prints 5

# Loop through the list
for item in my_list:
    print(item)

