MENU = {
  "expresso": {
    "ingredients": {
      "water" : 50,
      "coffe" : 18,
    },
    "cost" : 1.5,
  },
      "latte": {
    "ingredients": {
      "water" : 200,
      "milk" : 150,
      "coffe" : 24,
    },
    "cost" : 2.5,
  },
      "cappuccino": {
    "ingredients": {
      "water" : 250,
      "milk" : 100,
      "coffe" : 24,
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

print(MENU["cappuccino"]["ingredients"]["milk"])