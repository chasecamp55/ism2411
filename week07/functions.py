# functions.py

# ------------------------------------------------------------
# SELF-ASSESSMENT
#
# 1. Exercise 5:
# The first bug I spotted was the missing colon after for sale 
# in sales. I noticed it from the traceback because it caused 
# a syntax error. This tells me I am getting better at using 
# error messages to find simple syntax mistakes.
#
# 2. apply_discount(price, tier) takes a price and a customer
# discount tier as inputs. It checks whether the tier is gold,
# silver, bronze, or none and returns the price after applying
# the correct discount.
#
# 3. AI DISCLOSURE:
# I used AI to help explain the Python concepts and check my
# code for this lab. I used the explanations to better
# understand functions, parameters, return values, and scope.
# ------------------------------------------------------------


# --- Exercise 1 ---
# calculate_tax

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---
# apply_discount

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---
# Compose the functions

discounted_price = apply_discount(200, "gold")
tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax

print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
# Loop + function

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Debug First, Then Ask

sales = [120, 80, 250, 175, 90]

total = 0

# Bug 1: total = sale replaced the total each time.
# I changed it to += so each sale is added to the running total.
for sale in sales:
    total += sale

print(f"Total: ${total}")


count = 0

# Bug 2: The for loop was missing a colon.
# I added the colon so the loop has correct Python syntax.
for sale in sales:
    count += 1

print(f"Count: {count}")


i = 0

# Bug 3: <= caused the loop to try an index outside the list.
# I changed it to < so it stops at the last valid index.
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
# Scope experiment

x = 100   # global variable

def double_it():
    x = 999   # local variable
    return x * 2

print(x)
print(double_it())
print(x)

# Scope explanation:
# The x outside the function is a global variable and has a
# value of 100. The x inside double_it() is a separate local
# variable with a value of 999. Changing the local x does not
# change the global x.