import math 
import random 
import string

def generate_random_string(length=10):
    # Define the characters that can be used in the random string
    characters = string.ascii_letters + string.digits
    
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

def generate_unique_string(length=10):
    # Generate a random string
    random_string = generate_random_string(length)
    
    # Check if the string is already present in the list
    while random_string in unique_strings:
        random_string = generate_random_string(length)
    
    # Add the unique string to the list
    unique_strings.append(random_string)
    
    return random_string

# Initialize an empty list to store the unique strings
unique_strings = []

# Generate 10 unique strings
for _ in range(10):
    unique_string = generate_unique_string()
    print(unique_string)
    