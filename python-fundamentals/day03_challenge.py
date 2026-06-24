salary = 35000
rent = 9000
utilities = 2900
food = 4000
grocery = 2000

remaining = salary - rent - utilities - food - grocery

print(f"Remaining Budget: ₱{remaining}")
print(remaining > 10000)

print(salary >= 35000)
print(rent < food)
print(food == 4000)
print(grocery != 1000)