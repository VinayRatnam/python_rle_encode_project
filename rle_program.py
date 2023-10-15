#Vinay Ratnam
#09/27/23

from console_gfx import ConsoleGfx

def menu():
    """function to print menu"""
    print("\nRLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")

def to_hex_string(data):
    """translates data into a hexadecimal string"""
    hex_string = ""
    for i in range(len(data)):
        if 0 <= data[i] <= 9:
            hex_string += str(data[i])
        elif data[i] == 10:
            hex_string += "a"
        elif data[i] == 11:
            hex_string += "b"
        elif data[i] == 12:
            hex_string += "c"
        elif data[i] == 13:
            hex_string += "d"
        elif data[i] == 14:
            hex_string += "e"
        elif data[i] == 15:
            hex_string += "f"
    return hex_string

def count_runs(flat_data):
    """returns number of runs of data in an image data set"""
    j = 1
    runs = 1
    for i in range(len(flat_data) - 1):
        if flat_data[i] == flat_data[i + 1]:
            j += 1
        else:
            runs += 1
        if j == 15:
            runs += 1
            j = 0
    return runs

def encode_rle(flat_data):
    """returns encoding of the raw data passed"""
    encoded_list = []
    j = 1
    for i in range(len(flat_data) - 1):
        if flat_data[i] == flat_data[i + 1]:
            j += 1
        else:
            encoded_list.append(j)
            encoded_list.append(int(flat_data[i]))
            j = 1
        if j == 15:
            encoded_list.append(j)
            encoded_list.append(int(flat_data[i]))
            j = 0
    if flat_data[-2] != flat_data[-1]:
        encoded_list.append(1)
        encoded_list.append(flat_data[-1])
    else:
        encoded_list.append(j)
        encoded_list.append(flat_data[-1])
    return encoded_list

def get_decoded_length(rle_data):
    """returns decompressed size RLE data"""
    length = 0
    for i in range(len(rle_data)):
        if i % 2 == 0:
            length += rle_data[i]
        else:
            continue
    return length

def decode_rle(rle_data):
    """returns the decoded data set from RLE encoded data"""
    decoded_list = []
    for i in range(0, len(rle_data), 2):
        for j in range(rle_data[i]):
            decoded_list.append(rle_data[i + 1])
    return decoded_list

def string_to_data(data_string):
    """translates a string in hexadeximal format into byte data"""
    rle_list = []
    for i in range(len(data_string)):
        if data_string[i].isdigit():
            rle_list.append(int(data_string[i]))
        else:
            num = 0
            if data_string[i].upper() == "A":
                num = 10
            elif data_string[i].upper() == "B":
                num = 11
            elif data_string[i].upper() == "C":
                num = 12
            elif data_string[i].upper() == "D":
                num = 13
            elif data_string[i].upper() == "E":
                num = 14
            elif data_string[i].upper() == "F":
                num = 15
            rle_list.append(num)
    return rle_list

def to_rle_string(rle_data):
    """translates RLE data into a human-readable representation"""
    rle_copy = []
    for i in range(len(rle_data)):
        if 0 <= rle_data[i] <= 9:
            rle_copy.append(str(rle_data[i]))
        elif rle_data[i] == 10:
            rle_copy.append("a")
        elif rle_data[i] == 11:
            rle_copy.append("b")
        elif rle_data[i] == 12:
            rle_copy.append("c")
        elif rle_data[i] == 13:
            rle_copy.append("d")
        elif rle_data[i] == 14:
            rle_copy.append("e")
        elif rle_data[i] == 15:
            rle_copy.append("f")
    list = [] #makes new list that pairs run length with value
    for j in range(0, len(rle_copy), 2):
        list.append(rle_copy[i] + rle_copy[i + 1])
    rle_string = ":".join(list)
    return rle_string

def string_to_rle(rle_string):
    """translates a string in human-readable RLE format into RLE byte data"""
    list1 = rle_string.split(":")
    string1 = "".join(list1)
    rle_list = string_to_data(string1)
    return rle_list

def main():
    #define variables
    file_name = ""
    loaded_file = ""
    #print non-looped statements
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print()

    #make loop
    condition = True
    while condition:
        menu()
        menu_option = int(input("\nSelect a Menu Option: "))

        #if-elif-else statement for selected option
        if menu_option == 0: #exits program
            break
        elif menu_option == 1: #loads inputed file
            file_name = input("Enter name of file to load: ")
            loaded_file = ConsoleGfx.load_file(file_name)
            continue
        elif menu_option == 2: #loads test image
            loaded_file = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif menu_option == 3: #reads RLE string
            rle_string = input("Enter an RLE string to be decoded: ")
            loaded_file = decode_rle(string_to_rle(rle_string))
        elif menu_option == 4: #reads RLE hex string
            rle_hex_string = input("Enter the hex string holding RLE data: ")
            loaded_file = decode_rle(string_to_data(rle_hex_string))
        elif menu_option == 5: #reads data hex string
            data_hex_string = input("Enter the hex string holding flat data: ")
            loaded_file = string_to_data(data_hex_string)
        elif menu_option == 6: #display image
            print("Displaying image...")
            ConsoleGfx.display_image(loaded_file)
        elif menu_option == 7: #displays RLE string
            print("RLE representation:", to_rle_string(encode_rle(loaded_file)))
        elif menu_option == 8: #display hex RLE data
            print("RLE hex values:", to_hex_string(encode_rle(loaded_file)))
        elif menu_option == 9: #display hex flat data
            print("Flat hex values:", to_hex_string(loaded_file))

if __name__ == "__main__":
    main()