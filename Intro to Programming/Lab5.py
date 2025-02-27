#Number Computer Thingie
def option_screen():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
def normalize(n):
    k = str(n).upper()
    prefix = ['0B', '0X']
    if len(k) > 2:
        if k[0:2] in prefix:
            k = k[2:]
    return k
    #returns normalized input, ergo list conversion must still come after.
def hex_char_decode(digit):
    #Decodes a single hexadecimal digit and returns its decimal value.
    return int(digit, 16)

def hex_string_decode(term):
    #Decodes an entire hexadecimal string and returns its decimal value.
    digit = normalize(term)
    return int(digit, 16)

def binary_string_decode(binary):
    #Decodes a binary string and returns its decimal value.
    binary = normalize(binary)
    return int(binary, 2)

def binary_to_hex(binary):
    #Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.
    b_int = int(binary, 2)
    h_int = normalize(hex(b_int))
    return h_int

while True:
    option_screen()
    print()
    choice = int(input("Please enter an option: "))
    if choice == 1:
        t = input("Please enter the numeric string to convert: ")
        k = hex_string_decode(t)
        print(f"Result: {k}")
    if choice == 2:
        t = input("Please enter the numeric string to convert: ")
        k = binary_string_decode(t)
        print(f"Result: {k}")
    if choice == 3:
        t = input("Please enter the numeric string to convert: ")
        k = binary_to_hex(t)
        print(f"Result: {k}")
    if choice == 4:
        print("Goodbye!")
        exit()
