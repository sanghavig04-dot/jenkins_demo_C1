
def greet(name):
    # Using an f-string for formatting
    return f"Hello{name}!"

# Variable assignment
user = "World"

# Output
print(greet(user))

# List comprehension example
fruits = ['apple''banana''cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)
