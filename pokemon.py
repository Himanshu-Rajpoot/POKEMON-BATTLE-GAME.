import os, json, random, time

class Pokemon:
    def __init__(self, name, maxhp, atk, defense):
        self.n = name
        self.mh = maxhp
        self.ch = maxhp
        self.a = atk
        self.d = defense
    def dead(self):
        return self.ch <= 0
    def fullheal(self):
        self.ch = self.mh
    def __repr__(self):
        p = int(self.ch / self.mh * 100)
        state = "Healthy" if p > 50 else ("Hurt" if p > 20 else "Critical")
        return f"{self.n} ({state}) — {self.ch}/{self.mh} HP | Atk {self.a} Def {self.d}"

    @staticmethod
    def wild():
        choices = [
            ("Charmander", 50, 12, 8), ("Bulbasaur", 55, 10, 10),
            ("Squirtle", 52, 11, 9), ("Pikachu", 48, 13, 7),
            ("Rattata", 40, 14, 5), ("Pidgey", 45, 9, 6)
        ]
        return Pokemon(*random.choice(choices))

class Trainer:
    def __init__(self, name, skip=False):
        self.name = name.strip().title() if name.strip() else "Ash"
        self.p = None if skip else self.choose()
    def choose(self):
        starters = [("Charmander",52,12,9), ("Bulbasaur",55,10,11),
                    ("Squirtle",54,11,12), ("Pikachu",50,14,8)]
        print("pick your starter:")
        for idx, poke in enumerate(starters, 1): print(f"  {idx}. {poke[0]}")
        while True:
            try:
                choice = int(input("> ")) - 1
                if 0 <= choice < 4:
                    print(f"You chose {starters[choice][0]}! Let's go!")
                    time.sleep(0.7)
                    return Pokemon(*starters[choice])
            except Exception:
                print("  type a number 1-4")
                continue

def dmg(att, defe):
    return max(1, att.a - defe.d + random.randint(-2, 3))

def battle(me, wild):
    print(f"A wild {wild.n} appeared!")
    time.sleep(1)
    print(f"Go {me.n}!")
    round_num = 0
    while me.ch > 0 and wild.ch > 0:
        round_num += 1
        print(f"Round {round_num}")
        if random.random() < 0.5:
            dealt = dmg(me, wild)
            wild.ch -= dealt
            print(f"{me.n} hits for {dealt}!")
        else:
            dealt = dmg(wild, me)
            me.ch -= dealt
            print(f"Wild {wild.n} hits for {dealt}!")
        print(me)
        print(f"Wild {wild.n}: {wild.ch}/{wild.mh} HP")
        time.sleep(1)
    print("="*45)
    if me.ch > 0:
        print("You won!")
        me.fullheal()
    else:
        print("You blacked out...")
    print("="*45 + "")

SAVE = "pokegame.json"

def save(trainer):
    try:
        with open(SAVE, "w") as f:
            json.dump({
                "name": trainer.name,
                "p": {
                    "n": trainer.p.n, "ch": trainer.p.ch, "mh": trainer.p.mh,
                    "a": trainer.p.a, "d": trainer.p.d
                }
            }, f)
        print("saved")
    except Exception:
        print("couldn't save")

def load():
    if not os.path.exists(SAVE): return None
    try:
        with open(SAVE) as f:
            data = json.load(f)
        trainer = Trainer(data["name"], skip=True)
        poke = data["p"]
        trainer.p = Pokemon(poke["n"], poke["mh"], poke["a"], poke["d"])
        trainer.p.ch = poke["ch"]
        print(f"welcome back {trainer.name}")
        return trainer
    except Exception:
        return None

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    cls()
    print("Pokémon Terminal Edition")
    # Always ask for trainer name and choice at start
    name = input("Trainer name: ")
    player = Trainer(name)
    while True:
        print(f"{player.name}'s Pokémon:")
        print(player.p, "")
        print("1. Wild battle")
        print("2. Status")
        print("3. Save")
        print("4. Quit")
        c = input("> ").strip()
        if c == "1":
            battle(player.p, Pokemon.wild())
        elif c == "2":
            print("", player.p, "")
        elif c == "3":
            save(player)
        elif c == "4":
            print("bye")
            break
        else:
            print("??")
        time.sleep(0.4)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("later")