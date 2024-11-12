class CoffeeMaker:
  def report(self):
        resources_quantity = ""
        for resource in resources_list:
            if resource.name == "water" or resource.name == "milk":
                unit = "ml"  
            elif resource.name == "coffee":
                unit = "g"
            resources_quantity += f"{resource.name}: {resource.quantity} {unit}\n"
        print(resources_quantity)
  

  def is_resources_sufficient(self, drink):
     for ingredient, amount_needed in drink.ingredients.items():
        resource = next((r for r in resources_list if r.name == ingredient), None)
        if resource is None:
           print(f"Error no se encontro {ingredient}.")
           return False
        
        if resource.quantity < amount_needed:
           print(f"There is not enough {ingredient}. More needed {amount_needed}")
           return False
     return True
  
  def make_coffee(self,drink):
     for ingredient, amount_needed in drink.ingredients.items():
        resource = next((r for r in resources_list if r.name == ingredient), None)

        if resource:
           if resource.quantity >= amount_needed:
              resource.quantity -= amount_needed
              
class Resources:
  def __init__(self, name, quantity):
    self.name = name
    self.quantity = quantity

water = Resources("water", 300)
milk = Resources("milk", 200)
coffee = Resources("coffee", 100)

resources_list = [water,milk,coffee]

class MenuItem:
  def __init__(self, name, cost, ingredients):
    self.name = name
    self.cost = cost
    self.ingredients = ingredients

class Menu:    
  def get_items(self):
    menu = ""
    for item in menu_list:
        menu+= f"{item.name}/"
    return menu

  def find_drink(self, order_name):
    for item in menu_list:
        if order_name == item.name:
          return item
    return None    
           

class MoneyMachine:
   def report(self):
     print(f"Current profit: ${profit}")

   def make_payment(self, cost):
      coins = {
         "quarters" : 0.25,
         "dimes" : 0.10,
         "nickels" : 0.05,
         "pennies" : 0.01
      }
      total_payment = 0
      print("Please insert coins.")

      for coin, value in coins.items():
         while True:
            try:
               coin_count = int(input(f"How many {coin}?: "))
               if coin_count < 0:
                  print("Please enter a non-negative number.")
               else:
                  total_payment += coin_count * value
                  break
            except ValueError:
               print("Invalid input. Please enter a valid integer.")
      if total_payment >= cost:
         change = total_payment - cost
         print(f"Payment successful. Your change is: ${change:.2f}")
         return True
      else:
         print(f"Sorry, that's not enough money. You still need ${cost-total_payment:.2f}.")
         return False       
      

expresso = MenuItem("expresso", 1.5, {"water": 50, "coffee": 18})
latte = MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24})
cappuccino = MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})

menu_list = [expresso,latte,cappuccino]
menu = Menu()
profit = 0
is_on = True
my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



while is_on:
  options = menu.get_items()
  choice = input(f"Waht would you like? ({options}): ").lower()
  if choice == "off":
     is_on = False
  elif choice == "report":
    coffee_maker.report()
    my_money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resources_sufficient(drink) and my_money_machine.make_payment(drink.cost):
        profit += drink.cost
        coffee_maker.make_coffee(drink)
      