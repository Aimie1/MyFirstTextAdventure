import random


class Character():
    def __init__(self):
        self.name = "gergerge"
        self.hp = 100
        self.ap = 120

    def take_dmg(self, dmg):
        self.hp -= dmg  # self.hp = self.hp - dmg
        if self.hp < 0:
          self.hp = 0
        return self.hp

    def is_dead(self):
        if self.hp < 0:
            self.hp = 0
            return True
        else:
            return False


pc = Character()
print(pc.name)

dmg_amt = random.randint(0, pc.ap)
print("The pc took " + str(dmg_amt) + " damage.")
print(f"The pc has {pc.take_dmg(dmg_amt)} health.")
print(f"The character is dead? {pc.is_dead()}")
