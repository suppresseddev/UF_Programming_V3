from pakuri import Pakuri
class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.pakuri_db = []
        self.current_error = ""
    def get_size(self):
        return len(self.pakuri_db)
    def get_capacity(self):
        return self.capacity
    def get_species_array(self):
        k = []
        for paku in self.pakuri_db:
            k.append(paku.get_species())
        if k == []:
            return None
        else:
            return k
    def get_stats(self, species):
        try:
            for paku in self.pakuri_db:
                if paku.get_species() == species:
                    return [paku.get_attack(), paku.get_defense(), paku.get_speed()]
        except:
            return None
    def sort_pakuri(self):
        k = []
        for paku in self.pakuri_db:
            k.append(paku.get_species())
        k.sort()
        sorted_pakus = []
        for paku_species in k:
            sorted_pakus.append(Pakuri.get_paku(paku_species))
        self.pakuri_db = sorted_pakus
    def add_pakuri(self, species):
        if species not in Pakuri.pakuri_names:
            self.pakuri_db.append(Pakuri(species))
            return True
        else:
            self.current_error = "Error: Pakudex already contains this species!"
            return False
    def evolve_species(self, species):
        if species in Pakuri.pakuri_names:
            k = Pakuri.get_paku(species)
            k.evolve()
            return True
        else:
            self.current_error = "Error: No such Pakuri!"
            return False