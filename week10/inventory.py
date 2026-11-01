# ISM2411 - Module 10 Lab
# Inventory List Manager

# REFLECTION 1:
# The most surprising thing about Python lists is how
# easily you can add, remove, and rearrange items.
# I also learned that negative indexing allows you
# to access items from the end of a list.

# REFLECTION 2:
# At Panther Creek Country Club, Python lists could
# have helped me track golf carts and equipment.
# Using lists would have made it easier to organize
# inventory and update records instead of manually
# entering everything in Excel.


# EXERCISE 1 - Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("Exercise 1:")
print(inventory)
print(len(inventory))


# EXERCISE 2 - Index practice

print("\nExercise 2:")

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# EXERCISE 3 - Slicing

print("\nExercise 3:")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# EXERCISE 4 - Modify

print("\nExercise 4:")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# EXERCISE 5 - Tuple comparison

print("\nExercise 5:")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught!")
    print("Tuples cannot be modified.")
    print("They are useful for coordinates that should stay fixed.")

print(coords)


# EXERCISE 6 - Average of sales

print("\nExercise 6:")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# EXERCISE 7 - Accumulator pattern

print("\nExercise 7:")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)


# EXERCISE 8 - Filter above threshold

print("\nExercise 8:")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

average_high = sum(high_sales) / len(high_sales)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(average_high, 2))
