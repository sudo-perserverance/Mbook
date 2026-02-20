import time
import subprocess
import platform

#Menu
mode = input("Welcome User, Please select option 1 or 2\nOption 1: Program creates a text file with every page\nOption 2: Program copies the next page to your clipboard every few seconds\nSelection: ")

#Wiping old processed txt file (if applicable)
processed = open("MineProc.txt", "w", encoding="utf-8")
processed.write("")
processed.close()

#Opening text files
try:
    raw = open("MineRaw.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("The file 'MineRaw.txt' does not exist\nThis file should contain the text you wish to put into the book")
    try:
        open("MineRaw.txt", "w", encoding="utf-8")
        print("The program has created the file for you, Please fill it with text.")
    except Exception:
        print("The program has failed to create 'MineRaw.txt' Please create the file yourself")
    exit(1)
processed = open("MineProc.txt", "a", encoding="utf-8")
raw_data = raw.read()

#Determining the

#Setting book variables
line_max = 114
book_lines = 14
line_dots = 0
word_dots = 0
line = 1
item_dots = 0
word = ""
iteration = -1
skips = 0
max_page = 100
pages = 0
page_data = ""
page_list = []

#Setting how many pixels each letter uses up
alphabet = {
    " ": 4,
    "!": 2,
    '"': 4,
    "'": 2,
    "(": 4,
    ")": 4,
    "*": 4,
    ",": 2,
    ".": 2,
    ":": 2,
    ";": 2,
    "<": 5,
    ">": 5,
    "@": 7,
    "I": 4,
    "[": 4,
    "]": 4,
    "`": 3,
    "f": 5,
    "i": 2,
    "k": 5,
    "l": 3,
    "t": 4,
    "{": 4,
    "}": 4,
    "|": 2,
    "~": 7,
}


#Main loop to index each character
for item in raw_data:
    iteration += 1

#Determining the dots of the current character in the array
    if not (alphabet.get(item) is None):
        item_dots = alphabet.get(item)
    else:
        item_dots = 6

#Detecting skips
    if skips > 0:
        skips -= 1
        continue

#Detecting a new line and clearing the line
    if item == "\n":
        processed.write(word + "\n")
        page_data += (word + "\n")
        line_dots = 0
        word_dots = 0
        word = ""
        line += 1
        continue

#Detecting the @NEW command
    if item == "@":
        if raw_data[(iteration+1):(iteration+4)] == "NEW":
            processed.write(word)
            page_data += word
            processed.write("\n\n\n\nNEW PAGE COMMAND\n\n")
            page_list.append([pages, page_data])
            page_data = ""
            line_dots = 0
            word_dots = 0
            word = ""
            line = 1
            skips = 3
            pages += 1
            continue

    #Detecting Spaces
    if item == " ":
        if item_dots + word_dots + line_dots > line_max:
            processed.write(word + "\n")
            page_data += (word + "\n")
            line_dots = 0
            word_dots = 0
            word = ""
            line += 1
            continue
        word += " "
        word_dots += item_dots
        line_dots += word_dots
        processed.write(word)
        page_data += word
        word = ""
        word_dots = 0
        continue

#adding item as a new character of word
    word += item
    word_dots += item_dots

#Dectecting page overflow
    if line > 14 or (word_dots + line_dots > line_max and line == 14):
        processed.write("\n\n\n\nNEW PAGE\n\n")
        page_list.append([pages, page_data])
        page_data = ""
        line_dots = 0
        line = 1
        pages += 1

    if line_dots + word_dots > line_max:
        processed.write("\n")
        page_data += "\n"
        line_dots = 0
        line += 1

raw.close()
processed.close()

print("\a", end="")
print("Script has completed. Please check MineProc.txt")

if pages >= max_page:
    print("TEXT EXCEEDS MINECRAFT PAGE LIMIT, PLEASE EITHER SHORTEN THE TEXT OR TRY SOMETHING ELSE")
    processed = open("MineProc.txt", "w", encoding="utf-8")
    processed.write("TEXT EXCEEDS MINECRAFT PAGE LIMIT, PLEASE EITHER SHORTEN THE TEXT OR TRY SOMETHING ELSE")
    processed.close()
    for x in range(3):
        print("\a", end="")
        time.sleep(0.5)
    exit(1)


#Copying pages to clipboard
elif mode == "2":
    time.sleep(3)
    for item in page_list:

# Windows clipboard
        if platform.system() == "Windows":
            subprocess.run(["clip"], input=item[1].encode("utf-16"), check=True)

# Mac clipboard
        elif platform.system() == "Darwin":
            subprocess.run(["pbcopy"], input=item[1].encode(), check=True)

#Linux clipboard
        elif platform.system() == "Linux":
            try:
                subprocess.run( ["wl-copy"], input=item[1], text=True, check=True)
            except FileNotFoundError:
                for x in range(3):
                    print("\a", end="")
                    time.sleep(0.5)
                print("\nWayland clip board not found.\nPlease install wayland and try again\n\nsudo apt update\nsudo apt install wl-clipboard")
                exit(1)

        else:
            print("OS NOT SUPPORTED FOR OPTION 2")
            exit(1)


#Timer before next page
        print("Page " + str(item[0]+1) + " copied")
        print("\a", end="")
        time.sleep(3)

# Windows clipboard
        if platform.system() == "Windows":
            subprocess.run(["clip"], input="END OF BOOK".encode("utf-16"), check=True)

# Mac clipboard
        elif platform.system() == "Darwin":
            subprocess.run(["pbcopy"], input="END OF BOOK".encode(), check=True)

#Linux clipboard
        elif platform.system() == "Linux":
            try:
                subprocess.run( ["wl-copy"], input="END OF BOOK", text=True, check=True)
            except FileNotFoundError:
                for x in range(3):
                    print("\a", end="")
                    time.sleep(0.5)
                print("\nWayland clip board not found.\nPlease install wayland and try again\n\nsudo apt update\nsudo apt install wl-clipboard")
                exit(1)
