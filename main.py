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

profit = 0.0
resources = {
  "water" : 300,
  "milk" : 200,
  "coffee" : 100,
}

def is_resource_sufficient(order_ingredints):
  for item in order_ingredints:
    if order_ingredints[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")

   
   

# TODO: 1. Print report of all coffe machin eresources
# TODO: 2. Check resources sufficient to make drink order

is_on = True
report = f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}"

while is_on:
  choice = input("Waht would you like? (expresso/latte/cappuccino): ").lower()
  if choice == "off":
     is_on = False
  elif choice == "report":
     print(report)
  else:
    drink = MENU[choice]
    is_resource_sufficient(drink["ingredients"])