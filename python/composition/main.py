import rpg

aragorn = rpg.Ranger('Aragorn','Human', 100, 50)
galadriel = rpg.Mage('Galadriel', 'Elf', 120, 75)
frodo = rpg.Burglar('Frodo','Hobbit', 50, 25)
saruman = rpg.Wizard('Saruman', 'Human', 80, 100)

# Setter

frodo.inv.set_currency(9, 47, 23)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 50)

print(chest.inv.__dict__)
# print(aragorn.__dict__)
# print(frodo.__dict__)
# print(galadriel.__dict__)

# Getter
# print(frodo.inv.get_currency())
 

# Test chest method

# Frodo loots a chest!
chest.inv.transfer(chest.inv, frodo.inv)
# transfer is a method of inventory not chest. The from is chest.inv and to is frodo.inv
print(frodo.inv.__dict__)
print(frodo.inv.get_currency())
print(chest.inv.__dict__)

# CAN REDUCE CODE FURTHER BY CHANGING FROM-INV TO JUST SELF (IN BOTH FILES) LINE 42 IN RPG.PY


# Frodo loots a chest!
chest.inv.transfer(frodo.inv)
# transfer is a method of inventory not chest. The from is chest.inv and to is frodo.inv


print(frodo.inv.__dict__)
print(frodo.inv.get_currency())
print(chest.inv.__dict__)


# FIGHT

saruman.battle(aragorn)
frodo.battle(aragorn)