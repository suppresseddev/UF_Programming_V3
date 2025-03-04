#Standalone Menu
import console_gfx as gfx
valid = list(range(0,10))
current_load = [1, 1,
                gfx.CLEAR]
def commands(k):
    #Takes the prompt and does action, assuming k is valid.
    global current_load
    if k == 0:
        #Exit
        exit()
    if k == 1:
        #Load File
        _file = str(input("Enter the name of file to load: "))
        current_load = gfx.load_file(_file)
    if k == 2:
        #Load Test Image
        print("Test image data loaded")
        gfx.display_image(gfx.test_image)
    if k == 3:
        #Read RLE String
        RLEstring = input("Enter an RLE string to be decoded: ")
        hexes = RLEstring.split(":")
        k = []
        for t in hexes:
            k.append(int(t,16))
        current_load = k.copy()
    if k == 4:
        #Read RLE Hex String
        hexstring = input("Enter the hex string holding RLE data: ")
        hexes = list(hexstring)
        k = []
        for t, i in enumerate(hexes):
            if (((i+1) % 2) == 0):
                g = int(hexes[i-1:i+1], 16)
                k.append(g)
        current_load = k.copy()
    if k == 5:
        #Read Data Hex String
        print()
    if k == 6:
        #Display Image
        gfx.display_image(current_load)
    if k == 7:
        #Display RLE String
        print()
    if k == 8:
        #Display Hex RLE Data
        print()
    if k == 9:
        #Display Hex Flat Data
        print()
def main():
    global valid
    print(f"Welcome to the RLE image encoder!")
    print(f"Displaying Spectrum Image:")
    gfx.display_image(gfx.test_rainbow)
    while True:
        print("""
RLE Menu
--------
0. Exit
1. Load File
2. Load Test Image
3. Read RLE String
4. Read RLE Hex String
5. Read Data Hex String
6. Display Image
7. Display RLE String
8. Display Hex RLE Data
9. Display Hex Flat Data
        """)
        clear = False
        command = -1
        while not clear:
            command = int(input("Select a Menu Option: "))
            if command in valid:
                clear = True
            else:
                print("Invalid Option!")
        commands(command)
main()