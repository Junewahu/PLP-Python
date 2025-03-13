# sum_of_integers.py

# Step 1: Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ")

# Step 2: Convert the input string into a list of integers
numbers_list = list(map(int, numbers.split()))

# Step 3: Compute the sum of all integers in the list
total_sum = sum(numbers_list)

# Step 4: Print the sum
print("The sum of the integers is:", total_sum)