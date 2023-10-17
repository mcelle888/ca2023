class Character:
    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race

        self.health = health 
        self.attack = attack
        
        # self.gold = 0
        # self.silver = 0
        # self.copper = 0
        # wasteful, lets store copper and caluclate the rest

        # self.copper = 0

        # we have a inventory to calculate copper now instead: 
        self.inv = Inventory([], 0, 0, 0)

    def battle(self, other):
       print(f'{self.name} attacks {other.name}!')
    # wont go to the mechanics of how the battle works for now, just print this

# INHERITENCE, the ranger class will get all the character attributes

class Ranger(Character): 
    def battle (self, other): 
        print (f'{self.name} launches a brutal melee attack on {other.name}!')
    
    def recruit_undead(self):
        pass

class Mage(Character): 
    def __init__(self, name, race, health, attack):
        #Call the super class constructor to set up the character class attributes first (everything except what we need to add to Mage which is mana)
        super().__init__(name, race, health, attack)
        self.mana = 100
        def battle (self, other): 
            print (f'{self.name} casts a wicked spell at {other.name}!')



class Burglar(Character): 
    def battle (self, other): 
        print (f'{self.name} sneaks in a stealth attack on {other.name}!')


class Wizard(Character): 
    def battle (self, other): 
        print (f'{self.name} summons a orc minion, which attacks {other.name}!')



class Chest: 
    def __init__(self, items, gold, silver, copper):
        self.inv = Inventory(items, gold, silver, copper)
        
# inventory consists of items and currency items
class Inventory:    
    def __init__(self, items, gold, silver, copper):
        self.items = items # list
        self.set_currency(gold, silver, copper) #Delegation : delegated the work to another method rather than letting innit do it. So methods can call other methods in the same class.

    # Setter: so you can set one or more attributes on the object

    def set_currency(self, gold, silver, copper):
        self.copper = gold * 10000 + silver * 100 + copper
    
    # from_inv and to_inv are instances of Inventory
    def transfer(self, from_inv, to_inv):
        # add all items from from_inv to to_inv
        to_inv.items.extend(from_inv.items)
        # delete all items from from_inv
        from_inv.items = []
        # add the curremcu from from_inv to to_inv
        to_inv.copper += from_inv.copper
        # Set currency of from_inv to 0
        from_inv.copper = 0


# SELF CAN BE USED INSTEAD OF from_inv (point 34 in main) TO MAKE CODE MORE DRY

   # from_inv and to_inv are instances of Inventory
    def transfer(self, to_inv):
        # add all items from from_inv to to_inv
        to_inv.items.extend(self.items)
        # delete all items from self
        self.items = []
        # add the curremcu from self to to_inv
        to_inv.copper += self.copper
        # Set currency of self to 0
        self.copper = 0




    # Getter
    def get_currency(self):
        # return the currency back to user in the form of gold, silver and copper
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = (self.copper % 100) 
        return gold, silver, copper