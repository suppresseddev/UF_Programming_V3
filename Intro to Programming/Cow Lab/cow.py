class Cow():
    #Global Cow.var Setups
    All_Cows = []
    All_Cows_Names = []
    def __init__(self, name):
        self.name = name
        self.image = None
        Cow.All_Cows.append(self)
        Cow.All_Cows_Names.append(self.name)
    def get_name(self):
        #Bro we don't need set/get in Python, but okay, go off.
        return self.name
    def get_cow(name):
        for i, cow_name in enumerate(Cow.All_Cows_Names):
            if cow_name == name:
                return Cow.All_Cows[i]
    def get_image(self):
        #Again, no need for set/get IF there are no set conditions.
        return self.image
    def set_image(self, image):
        #Rewriting the image code now that I understand what this is doing.
        self.image = image