MENU = {
  "expresso": {
    "ingredients": {
      "water" : 50,
      "coffee" : 18,
    },
    "cost" : 1.5,
  },
      "latte": {
    "ingredients": {
      "water" : 200,
      "milk" : 150,
      "coffee" : 24,
    },
    "cost" : 2.5,
  },
      "cappuccino": {
    "ingredients": {
      "water" : 250,
      "milk" : 100,
      "coffee" : 24,
    },
    "cost" : 3.0,
  },
}

resources = {
  "water" : 300,
  "milk" : 200,
  "coffee" : 100,
}

def is_resource_sufficient(order_ingredints):
  """Returns true when order can be made"""
  for item in order_ingredints:
    if order_ingredints[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
    else:
      resources[item] -= order_ingredints[item]
  return True

def process_coins():
  """Returns the total calculated from coins inserted"""
  print("Plase insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

def is_transaction_succesful(money_received, drink_cost): 
  """Return true if payment accepted or false if money is insufficient."""
  if money_received >= drink_cost:
    global profit
    profit+= drink_cost
    change = round((money_received - drink_cost), 2)
    print(f"Here is ${change} in change.")

    return True
  else:
    print("Sorry that's not enought money. Money refunded.")
    return False



# TODO: 1. Print report of all coffe machin eresources
# TODO: 2. Check resources sufficient to make drink order
profit = 0
is_on = True


while is_on:
  choice = input("Waht would you like? (expresso/latte/cappuccino): ").lower()
  if choice == "off":
     is_on = False
  elif choice == "report":
     print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: £ {profit}")
  else:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):    
      payment = process_coins()
      if is_transaction_succesful(payment, drink["cost"]):
        print(f"Here is your {choice}. Enjoy!")




    

      
    
    
      