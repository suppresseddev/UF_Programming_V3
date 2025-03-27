debug = False
#Standalone Menu
import console_gfx as gfx
#valid index inputs for console navigation
valid = list(range(0,10))
current_load = [1, 1,
                gfx.CLEAR]
def to_hex_string(data):
    k = ""
    return k.join(hex(t)[2:] for t in data)
def count_runs(flat_data):
    k = 1
    #keeps track to make sure no RLE is greater than 15
    j = 1
    for i, rl in enumerate(flat_data):
        if i == len(flat_data) - 1:
            break
        if rl != flat_data[i+1]:
            k += 1
        else:
            j += 1
        if j == 15:
            k += 1
            j = 1
    return k
def encode_rle(flat_data):
    #RLE takes the count of consecutive equivalent values and makes 'runs'
    #For example, 5 5 5 5 6 6 2, would be come 4 5 2 6 1 2
    #Compression is cool :>
    k = 1
    new_rle = []
    for i, pt in enumerate(flat_data):
        if i == len(flat_data) - 1:
            new_rle.append(k)
            new_rle.append(pt)
            break
        if (flat_data[i+1] != pt):
            new_rle.append(k)
            new_rle.append(pt)
            k = 1
        else:
            k += 1
        if k == 15:
            new_rle.append(k)
            new_rle.append(pt)
            k = 0
    return(new_rle)
def get_decoded_length(rle_data):
    j = 1
    k = 0
    if debug:
        print("Running get_decoded_length()...")
    for pt in rle_data:
        if j == 1:
            #Odd term logic
            if debug:
                print(f"Odd term: {pt}!")
            k = k + pt
            if debug:
                print(f"Performing {k} + {pt}, result is {k+pt}!")
        if j == 2:
            #Even term logic
            if debug:
                print(f"Even term: {pt}!")
            j = 0
        if debug:
            print(f"Current 'k' is {k}!")
        j += 1
    return k
def decode_rle(rle_data):
    #takes a list, no run logic needed
    expanded_data = []
    for i, pt in enumerate(rle_data):
        if i == len(rle_data) - 1:
            break
        if i % 2 != 0:
            continue
        else:
            rl = pt
            color = rle_data[i+1]
            for k in range(rl):
                expanded_data.append(color)
    if debug:
        print("Ran decode_rle()!")
        if len(expanded_data) == get_decoded_length(rle_data):
            print(f"The expanded data length and the predicted length match up @ {len(expanded_data)}!")
        else:
            print(f"WARN: The expanded data length and the predicted length do not match up.")
            print(f"The predicted length is {get_decoded_length(rle_data)}.")
            print(f"The expanded data length is {len(expanded_data)}.")
    return expanded_data
def string_to_data(data_string):
    data = list(data_string)
    k = []
    for pt in data:
        k.append(int(pt, 16))
    return k
def to_rle_string(rle_data):
    k = ""
    h = 1
    for pt in rle_data:
        k += str(pt)
        if h == 2:
            k += ":"
            h = 1
        else:
            h += 1
    return k[:-1]
def string_to_rle(rle_string):
    rle_data = rle_string.split(":")
    new_data = []
    for pt in rle_data:
        run_length = int(pt[:-1])
        color = int(pt[-1], 16)
        new_data.append(run_length)
        new_data.append(color)
    return new_data
def commands(c):
    #Takes the prompt and does action, assuming k is valid.
    global current_load
    if c == 0:
        #Exit
        exit()
    if c == 1:
        #Load File
        _file = str(input("Enter the name of file to load: "))
        current_load = gfx.load_file(_file)
    if c == 2:
        #Load Test Image
        print("Test image data loaded.")
        current_load = gfx.test_image.copy()
    if c == 3:
        #Read RLE String
        k = input("Enter an RLE string to be decoded: ")
        k = string_to_rle(k)
        current_load = k.copy()
    if c == 4:
        #Read RLE Hex String
        hexstring = input("Enter the hex string holding RLE data: ")
        hexstring_list = []
        for pt in list(hexstring):
            hexstring_list.append(int(pt, 16))
        k = decode_rle(hexstring_list)
        current_load = k.copy()
    if c == 5:
        #Read Data Hex String
        hex_string = input("Enter the hex string holding flat data: ")
        k = string_to_data(hex_string)
        k = encode_rle(k)
        current_load = k.copy()
    if c == 6:
        #Display Image
        print("Displaying image...")
        gfx.display_image(current_load)
    if c == 7:
        #Display RLE String
        print(f"RLE representation: {to_rle_string(encode_rle(current_load))}")
    if c == 8:
        #Display Hex RLE Data
        print(f"RLE hex values: {to_hex_string(current_load)}")
    if c == 9:
        #Display Hex Flat Data
        print(f"Flat hex values: {to_hex_string(decode_rle(current_load))}")
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
if __name__ == "__main__":
    main()