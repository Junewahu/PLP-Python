# odd_length_words.py

# Step 1: Store a list of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Step 2: Use list comprehension to create a new list with words of odd length
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Step 3: Print the new list
print("Words with odd number of characters:", odd_length_words)