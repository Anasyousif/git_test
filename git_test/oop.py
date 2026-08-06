def main():
    Aragorn= Brawler("Aragorn",4,4)
    Gimli= Brawler("Gimli",2,7)
    Legolas= Brawler("Legolas",7,7)
    Frodo= Brawler("Frodo",3,2)
    fight(Aragorn,Gimli)
    fight(Legolas,Frodo)

# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker, defender):
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")

main()

