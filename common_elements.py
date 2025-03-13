# common_elements.py

# Step 1: Accept user input to create two sets of integers
set1 = set(map(int, input("Enter the first set of integers separated by spaces: ").split()))
set2 = set(map(int, input("Enter the second set of integers separated by spaces: ").split()))

# Step 2: Find the common elements between the two sets
common_elements = set1.intersection(set2)

# Step 3: Print the common elements
print("Common elements:", common_elements)