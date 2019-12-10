import matplotlib.pyplot as plt
from random import randint

diceRolls = []
for i in range(100000):
    num1 = randint(0, 9)
    num2 = randint(0, 9)
    diceRolls.append(num1 * 10 + num2)
    diceRolls.append(num2 * 10 + num1)

plt.hist(diceRolls)
plt.show()
