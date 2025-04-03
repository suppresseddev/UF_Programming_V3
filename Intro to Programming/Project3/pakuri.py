class Pakuri:
    pakuri_objects = []
    pakuri_names = []
    def __init__(self, species):
        self.species = species
        #Extremely silly logic, making increases in talent derive from your name.
        #If you want things to be balanced, make it depend on more random things for fairness.
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
        Pakuri.pakuri_objects.append(self)
        Pakuri.pakuri_names.append(species)
    def get_paku(species):
        for i, paku_species in enumerate(Pakuri.pakuri_names):
            if paku_species == species:
                return Pakuri.pakuri_objects[i]
    def get_species(self):
        return self.species
    def get_attack(self):
        return self.attack
    def get_defense(self):
        return self.defense
    def get_speed(self):
        return self.speed
    def set_attack(self, new_attack):
        self.attack = new_attack
    def evolve(self):
        #Just terribly game balance right here.
        #Late game is gonna be a shitty chip-damage game, like Genshin Impact.
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3