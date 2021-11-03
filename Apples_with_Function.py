def total_money_func():
    total_money = int(input("How much money do you have?:"))
    return total_money

def apple_cost_func():
    apple_cost = int(input("How much does an apple cost?:"))
    return apple_cost

def compute_maximum_apples():
    maximum_apples = int(money/apple)
    return maximum_apples

def compute_remaining_money():
    remaining_money = money-maximum_apples*apple
    return remaining_money

def displayOutput(maximum_applesZ, remaining_moneyZ):
    print(f"You can buy {maximum_applesZ} apples and your change is {remaining_moneyZ} pesos")
# Steps
# 1. define a function asking the amount of money you have and save as variable
money = total_money_func()
# 2. define a function asking the prince of an apple and save as variable
apple = apple_cost_func()
# 3. define a function computing the maximum apples that could be bought and save as variable
maximum_apples = compute_maximum_apples()
# 4. define a function computing the remaining money and save as variable
remaining_money = compute_remaining_money()
# 5. display maximum apples and remaining money
displayOutput(maximum_apples, remaining_money)