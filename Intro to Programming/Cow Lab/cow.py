class Cow():
    #Global Cow.var Setups
    All_Cows = []
    All_Cows_Names = []
    #Stuff from heifer_generator.py that I truly do not understand.
    quote_lines = "    \\\n"
    quote_lines += "     \\\n"
    quote_lines += "      \\\n"

    cow_images = [
        "        ^__^\n"
        + "        (oo)\\_______\n"
        + "        (__)\\       )\\/\\\n"
        + "            ||----w |\n"
        + "            ||     ||\n",
        "       (\"`-'  '-/\") .___..--' ' \"`-._\n"
        + "         ` *_ *  )    `-.   (      ) .`-.__. `)\n"
        + "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n"
        + "      _.. `--'_..-_/   /--' _ .' ,4\n"
        + "   ( i l ),-''  ( l i),'  ( ( ! .-'\n",
    ]
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
        #Image is an index for the cow list.
        try:
            self.image = Cow.quote_lines + Cow.cow_images[image]
        except:
            print(f"{image} is not a valid cow image! {len(Cow.All_Cows) - 1} is the current limit.")