MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
coins = {
  'quarters': 0.25, 
  'dimes': 0.10,
  'nickles': 0.05,
  'pennies': 0.01
}

is_off = False

def calculate_money(user_money):
  total = 0
  for i in coins:
    total += user_money[i] * coins[i]
  return total

def is_resources_sufficient(drink):
  if 'water' in drink and drink['water'] > resources['water']:
    return 'water'
  if 'milk' in drink and drink['milk'] > resources['milk']:
    return 'milk'
  if 'coffee' in drink and drink['coffee'] > resources['coffee']:
    return 'coffee'
  return True

def update_resources(drink):
  for i in resources:
    if i in drink:
      resources[i] -= drink[i]
  resources['money'] += drink['cost']

def print_report():
  for i in resources:
      if i == 'water' or i == 'milk':
        print(i.capitalize() + ":", str(resources[i]) + 'ml')
      elif i == 'coffee':
        print(i.capitalize() + ":", str(resources[i]) + 'g')
      else:
        print(i.capitalize() + ":", '$' + str(resources[i]))

while not is_off:
  user_input = input("What would you like (espresso/latte/cappuccino):\n")
  if user_input == 'off':
    break
  elif user_input == 'report':
    print_report()
  elif user_input in ['espresso', 'latte', 'cappuccino']:
    drink = MENU[user_input]
    is_sufficient = is_resources_sufficient(drink['ingredients'])
    if is_sufficient == True:
      user_money = {}
      for i in coins:
        user_money[i] = int(input(f'Enter number of {i}: '))
      money = calculate_money(user_money)
      if money < drink['cost']:
        print("Sorry!!! that's not enough money. Money refunded.")
      else:
        print(f"Here's your change {round(money - drink['cost'], 2)}")
        print(f"Here's your {user_input}. Enjoy!!!!")
        update_resources(drink['ingredients'])
    else:
      print(f'Sorry!!! Machine cannot make {user_input} due to lack of {is_sufficient}.')
  else:
    continue
