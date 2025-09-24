print("********************************")
print("*****         WELCOME      *****")
print("*****     To APPLE STORE   *****")
print("********************************")


# 1. Print a message, welcoming the user and asking for their name.
print("Welcome to the Apple Store!")

# 2. Now the user must enter their name.
print("Please enter your name:")
name = input()

# 3. Print message, greeting the user by name, and indicating that you currently have 20 apples available, each for a price of 5 (can be peso, euro, dollar, etc.).
num_apples = 20
price_per_apple = 5
print("Hello", name + "!")
print("You currently have", num_apples, "apples available, each for a price of", price_per_apple)

# 4. Print a message, asking the user how many apples they want to buy.
print("How many apples do you want to buy?")

# 5. Now the user must enter how many apples they want.
apples_you_want = int(input())

# 6. Print a message indicating how many apples the user bought, and what the total price was.
total_price = apples_you_want * price_per_apple
print("You bought", apples_you_want, "apples for a total price of", total_price)
num_apples -= apples_you_want

# 7. Finally, print a message indicating how many apples were available after the sale.
print("We now have", num_apples, "apples available after your purchase.")