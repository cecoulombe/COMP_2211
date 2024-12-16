import random
list1 = [10, 20, 30, 40, 50]
firstChoice = random.choice(list1)
list1.remove(firstChoice)
secondChoice = random.choice(list1)

print([firstChoice, secondChoice])
