import os
import shutil
import sys, tty, termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print("What is your first name?")
fname = input("↪ ")

print("What is your last name?")
lname = input("↪ ")

clear()

name = fname + " " + lname
def pronoun_choice():
    print("""
    What are your pronouns?
    1. She/Her
    2. He/Him
    3. They/Them
    (Enter number)
    """)
    return getch()

clear()

pronouns_choice = pronoun_choice()

if pronouns_choice == "1":
    pronouns = "Ms. "

elif pronouns_choice == "2":
    pronouns = "Mr. "

elif pronouns_choice == "3":
    pronouns = "Mx. "

else:
    pronoun_choice()

clear()

columns = shutil.get_terminal_size().columns

print("⠀⠀⠀⢀⠀⢀⣀⡀⢠⠤⠄⢤⢠⠀⡄⡠⡄⠠⡤⣄⣀⠀⡀⠀⠀⠀".center(columns))
print("⠀⠀⢰⣈⢧⢺⣀⡹⠸⠤⠇⠸⠃⠛⠴⠏⠹⢠⡛⣇⢁⡏⢱⡲⠀⠀".center(columns))
print("⠀⠀⠀⠗⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠓⠋⠀⠀".center(columns))
print("⠀⠀⠈⠀⠀⢀⠤⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠤⡀⠀⠀⠁⠀⠀".center(columns))
print("⠠⠀⠀⠀⠐⠁⢀⣄⠀⠁⠠⠀⠀⠀⠀⠄⣈⣀⡀⠀⠈⠂⠀⠀⠀⠄".center(columns))
print("⠀⠀⠀⠈⠂⢄⠹⣿⢰⣿⣷⡄⠈⠁⠼⠟⠉⣹⡇⠀⡠⠐⠁⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⠀⠀⠆⡎⢸⣿⣿⠴⠒⠈⣠⡶⠟⠉⠀⠰⠀⠀⠀⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⠀⠀⡄⠹⣿⡟⠋⣑⠂⢐⣋⠁⣤⣾⣿⢧⠀⠀⠀⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⠀⢠⣀⣯⣹⣄⡆⢸⠤⠼⡇⢰⣙⣻⣟⣀⡄⠀⠀⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⡠⠁⣴⣶⣦⠄⠁⠸⠄⠠⠇⠈⣺⣿⣄⣸⣿⣄⠀⠀⠀⠀".center(columns))
print("⠀⠀⡀⠊⠈⣧⣿⣿⣶⣤⡁⠀⠀⠀⣶⣾⣿⣿⣿⣿⣿⡇⠁⢀⠀⠀".center(columns))
print("⠀⠀⠀⢄⠀⢠⡿⠛⢿⣿⣿⡆⠀⠀⣿⣿⣿⣿⡟⠻⢿⡿⡠⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⠁⣀⠤⠙⢛⣽⠟⠓⠀⠀⢻⡟⢸⠉⣧⠤⣀⠈⠀⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠄⡀⠀⠀⢈⠠⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀".center(columns))
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⡠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀".center(columns))


input("Press [ENTER] to start...")

text1 = "HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY"
text2 = "Headmaster: Albus Dumbledore"
text3 = "(Order of Merlin, First Class, Grand Sorc., Chf. Warlock,"
text4 = "Supreme Mugwump, International Confed. of Wizards)"

text5 = "PARENTS ARE REMINDED THAT FIRST YEARS"
text6 = "ARE NOT ALLOWED THEIR OWN BROOMSTICK"

columns = shutil.get_terminal_size().columns

print("As you walk to your front door, an owl swoops down and drops a letter at your feet.")
print("""
    1. Ignore the letter
    2. Pick up the letter
""")
char = getch()
if char == "1":
    pass
if char == "2":
    pass

input("Press [ENTER] to pick up the letter...")
print("The letter is sealed with a red wax stamp bearing a lion, a serpent, a badger, and an eagle surrounding a large letter 'H'.")
input("Press [ENTER] to break the seal and open the letter...")
print("You unfold the letter and read:")

print(text1.center(columns))
print(text2.center(columns))
print(text3.center(columns))
print(text4.center(columns))
print(f"""
Dear {pronouns} {lname},
We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry. Please find enclosed a list of all necessary books and equipment.
Term begins on 1 September. We await your owl by no later than 31 July.

Yours sincerely,
Minerva McGonagall

Deputy Headmistress
""")
input("Press [ENTER] to flip the page...")
print("""
UNIFORM

First-year students will require:
    1. Three sets of plain work robes (black)
    2. One plain pointed hat (black) for day wear
    3. One pair of protective gloves (dragon hide or similar)
    4. One winter cloak (black, with silver fastenings)
Please note that all pupil's clothes should carry name tags.

COURSE BOOKS

All students should have a copy of each of the following:

    1. The Standard Book of Spells (Grade 1) by Miranda Goshawk
    2. A History of Magic by Bathilda Bagshot
    3. Magical Theory by Adalbert Waffling
    4. A Beginner's Guide to Transfiguration by Emeric Switch
    5. One Thousand Magical Herbs and Fungi by Phyllida Spore
    6. Magical Drafts and Potions by Arsenius Jigger
    7. Fantastic Beasts and Where to Find Them by Newt Scamander
    8. The Dark Forces: A Guide to Self-Protection by Quentin Trimble
      
OTHER EQUIPMENT
    1 wand
    1 cauldron (pewter, standard size 2)
    1 set glass or crystal phials
    1 telescope
    1 set brass scales
Students may also bring, if they desire, an owl OR a cat OR a toad.
      """)
print(text5.center(columns))
print(text6.center(columns))
print("""

Yours sincerely,

Lucinda Thomsonicle-Pocus
Chief Attendant of Witchcraft Provisions
""")
