def apple_amount_func():
    apple = int(20)
    return apple 

def orange_amount_func():
    orange = int(25)
    return orange

def apple_func():
    apples = int(input("How many apples would you like to buy?:"))
    return apples 

def orange_func():
    oranges = int(input("How many oranges would you like to buy?:"))
    return oranges

def total_amount_func():
    total_amount = apple*total_apples+orange*total_oranges
    return total_amount

def displayOutput(total_amountZ):
    print(f"The total amount is {total_amountZ} pesos")
# Steps
# 1. define a function with the price of an apple and save as variable
apple = apple_amount_func()
# 2. define a function with the price of an orange and save as variable
orange = orange_amount_func()
# 3. define a function asking how many apples would you like to buy and save as variable
total_apples = apple_func()
# 4. define a function asking how many oranges would you like to buy and save as variable
total_oranges = orange_func()
# 5. define a function computing the total amount of the apples and oranges bought and save as variable
total_amount = total_amount_func()
# 6. display total amount
displayOutput(total_amount)