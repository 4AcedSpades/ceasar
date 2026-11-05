"""
This houses the main functions that this program uses.
It's important to keep this file, otherwise the main program will not function properly.
"""
import os
import time

filePath = ''
alphabet = []
result = ''
reply = False

def mainMenuPrintout(): # Contains the menu for the program.
    """<h2>Displays a menu containing 3 options:</h2>
    <p>1 - Start a message: Creates a message with an alphabet, shift, and starting message, before saving it.</p>
    <p>2 - Read & Reply to a message: Prompts for a file, decoding the message before asking if the user would like to reply.</p>
    <p>3 - Quit: Runs exit(), closing the program.
    <p>Anything other than 1 - 3 will not be validated, displaying the menu again.</p>"""

    print("CAESAR CIPHER MESSAGING")
    print("-----------------------")
    print("1. Start a message")
    print("2. Read & Reply to a message")
    print("3. Quit")


def MainMenu(choice):
    """<h2>Validates the choice.</h2>"""
    while True: 
        mainMenuPrintout()   
        choice = input("> ")
        if int(choice) == 1:
            filePath = createFile(filePath)
            alphabet = getAlpha(filePath)
            shift = getShift(filePath)
            createMsg(filePath, alphabet, shift)
            
        elif int(choice) == 2:
            readMsg(filePath)
            replyMsg(filePath, alphabet, shift)
    
        elif int(choice) == 3:
            exit()
    
        else:
            print("Please provide a valid action.")
        

def getAlpha(path):
    """<h2>Prompts the user to type an alphabet to be stored in a .txt file.</h2>"""
    print("Please type the alphabet that will be used for decoding (case-sensitive)")
    choice = input("> ")
    with open(path, "a") as file:         
        file.write(choice)
    alphabet = [char for char in choice]
    return alphabet

def getShift(path):
    """<h2>Prompts the user to type a shift to be stored in a .txt file.</h2>"""
    print("Please type the shift that will be used for decoding")
    choice = input("> ")
    with open(path, "a") as file:          
        file.write(f"\n{choice}")
    shift = choice; shift = int(shift)
    return shift

def encrypt(msg:str,mode:int,shift:int,alphabet:list):
    """<h2>Encrypts or decrypts a given message.</h2>
    <p>This function takes the given message, and then translates it through the provided shift & alphabet given.</p>"""
    result = ""
    message = [char for char in msg]
    if mode == 0:
        pass
    else:
        shift = shift * -1
    for char in message:
        try:
            result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        except IndexError:
            print(f"Letter {char} is out of range. Skipping...")
        except ValueError:
            print(f"Letter {char} is not in the specified alphabet. Skipping...")
    return result

def createMsg(filePath:str, alphabet:str, shift:int):
    """<h2>Creates a message and stores it in the filepath provided.<h2>
    <p>Uses encrypt() to shift the message.</p>"""
    msg = input("In one line, please type the message you'd like to send: ")
    result = encrypt(msg, 0, shift, alphabet)
    with open(filePath, "a") as file:
        file.write(f"\n{result}")
    print(f"Original Text: {msg}")
    print(f"Modified Text: {result}")

def readMsg(filePath):
    """Reads message(s) from a file."""
    clr()
    filePath = input("Please type the file you'd like to read: ")
    readmsgs = []
    with open(filePath, "r") as file:
        content = file.readlines()
    alphabet = list(content[0].rstrip("\n"))
    print(alphabet) #DEBUG
    shift = int(content[1].strip())
    messages = content[2:]
    for msg in messages:
        result = encrypt(msg.strip(), 1, shift, alphabet)
        readmsgs.append(result)
    print("Decoded Messages:")
    for msg in readmsgs:
        print(msg)
    choice = input("Would you like to add a message to the decoded file? (y/n) ")
    reply = choice.lower() == "y"
    return filePath, reply, alphabet, shift



def replyMsg(filePath, alphabet, shift, reply):
    """<h2>Appends a message to an already existing file.</h2>"""
    print("In one line, please type the message you'd like to send.")
    msg = input("> ")
    encrypt(msg, 0, shift, alphabet)
    with open(filePath, "a") as file:
        file.write(f"\n{result}")
    print(f"Original Text: {msg}")
    print(f"Modified Text: {result}")

def clr():
    os.system("cls" if os.name == "nt" else "clear")

def createFile(filePath):
    """Creates a file to house the data."""
    while True:
        clr()
        print("What would you like to call your file? (fullname.txt)")
        choice = input("> ")
        try:
            with open(choice, "x") as file:
                file.write("")
                filePath = choice
                return filePath
        except FileExistsError:
            print("File already exists.")
            time.sleep(2)
        except FileNotFoundError:
            print("Could not find the directory specified.")
            time.sleep(2)

if __name__ == "__main__":
    # filePath = createFile(filePath)
    # alphabet = getAlpha(filePath)
    # shift = getShift(filePath)
    # message = createMsg(filePath, alphabet, shift)
    filePath, reply, alphabet, shift = readMsg(filePath)
    print(alphabet)