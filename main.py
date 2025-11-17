import os
import shutil
import sys, tty, termios
import time

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

def slow_print(text, delay=0.04):
    for line in text.split("\n"):
        print(line)
        time.sleep(delay)

# ---------------------------------------------------------------------
# BOOT SEQUENCE (retro terminal style)
# ---------------------------------------------------------------------
clear()
slow_print("MAGICAL TERMINAL SYSTEM v2.3 — MINISTRY OF MAGIC", 0.03)
slow_print("COPYRIGHT (C) 1984 — ALL RIGHTS RESERVED\n", 0.03)
time.sleep(0.5)

slow_print("INITIALIZING...", 0.05)
time.sleep(0.4)
slow_print("LOADING SPELL MODULES... OK", 0.05)
slow_print("CHECKING OWL POST CONNECTION... OK", 0.05)
slow_print("PREPARING USER INTERFACE... OK", 0.05)
slow_print("\nSYSTEM READY.\n", 0.04)
input("Press [ENTER] to begin... ")
clear()

# ---------------------------------------------------------------------
# PLAYER SETUP
# ---------------------------------------------------------------------

slow_print("PLEASE ENTER YOUR FIRST NAME")
fname = input("> ")

slow_print("\nPLEASE ENTER YOUR LAST NAME")
lname = input("> ")

clear()

name = fname + " " + lname

def pronoun_choice():
    slow_print("""
SELECT PRONOUNS
    (1) SHE / HER
    (2) HE / HIM
    (3) THEY / THEM

> """)
    return getch()

slow_print("LOADING USER PROFILE...\n")
time.sleep(0.6)
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

# ---------------------------------------------------------------------
# OWL ARRIVAL + ART
# ---------------------------------------------------------------------

columns = shutil.get_terminal_size().columns

slow_print("AN OWL APPROACHES WITH UNUSUAL SPEED...\n", 0.04)

owl_art = [
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠠⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣇⠀⠀⠀⣷⠈⣿⣿⡇⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⢨⣿⡀⣿⣿⡇⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡆⠀⢸⣿⣇⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⢠⠀⠀⠀⠀⠀⠀⣿⣿⣿⠁⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⣾⡄⠀⠀⠀⠀⠀⣿⣿⣿⡆⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢀⣦⠀⠀⠀⠀⠀⠀",
"⢰⣿⡇⢰⡆⠀⢀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣾⣿⠀⠀⠀⠰⠆⠀",
"⣸⡿⣇⣸⣟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀"
]

for line in owl_art:
    slow_print(line.center(columns), 0.02)

slow_print("\nTHE OWL DROPS A LETTER AT YOUR FEET.\n")
slow_print("""
    (1) IGNORE THE LETTER
    (2) PICK UP THE LETTER

> 
""")
char = getch()

clear()

if char == "1":
    slow_print("As you open the door, a letter slides under it with a soft *hoot*.\n")
    while True:
        slow_print("""
    (1) IGNORE THE LETTER
    (2) PICK UP THE LETTER

> """)
        sel = getch()
        clear()
        if sel == "1":
            slow_print("Another letter slides under the door, adding to the pile.\n")
        if sel == "2":
            break

clear()

# ---------------------------------------------------------------------
# LETTER SEAL + CONTENT
# ---------------------------------------------------------------------

slow_print("The letter is sealed with a red wax stamp bearing four creatures and a large 'H'.\n")
input("Press [ENTER] to break the seal... ")
clear()

slow_print("You unfold the letter and read:\n")

slow_print("HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY".center(columns))
slow_print("Headmaster: Albus Dumbledore".center(columns))
slow_print("(Order of Merlin, First Class, Grand Sorc., Chf. Warlock,".center(columns))
slow_print("Supreme Mugwump, International Confed. of Wizards)".center(columns))

slow_print(f"""
Dear {pronouns}{lname},

We are pleased to inform you that you have been accepted at Hogwarts School of
Witchcraft and Wizardry. Please find enclosed a list of all necessary books
and equipment.

Term begins on 1 September. We await your owl by no later than 31 July.

Yours sincerely,
Minerva McGonagall
Deputy Headmistress
""")

input("Press [ENTER] to view the supply list... ")
clear()

slow_print("""
UNIFORM
-------
(1) Three sets of plain work robes (black)
(2) One plain pointed hat (black)
(3) Gloves (dragon hide or similar)
(4) One winter cloak (black, silver fastenings)
All clothing must be labeled with student's name.

COURSE BOOKS
------------
A copy of each of the following:
- The Standard Book of Spells (Grade 1)
- A History of Magic
- Magical Theory
- A Beginner's Guide to Transfiguration
- One Thousand Magical Herbs and Fungi
- Magical Drafts and Potions
- Fantastic Beasts and Where to Find Them
- The Dark Forces: A Guide to Self-Protection

OTHER EQUIPMENT
---------------
1 wand
1 cauldron (pewter, standard size 2)
1 set phials (glass or crystal)
1 telescope
1 set brass scales

Students may bring an owl OR a cat OR a toad.
""")

slow_print("PARENTS ARE REMINDED THAT FIRST YEARS".center(columns))
slow_print("ARE NOT ALLOWED THEIR OWN BROOMSTICK".center(columns))

input("\nPress [ENTER] to continue... ")
clear()

# ---------------------------------------------------------------------
# KNOCK AT THE DOOR
# ---------------------------------------------------------------------

while True:
    slow_print("""
THERE IS A HEAVY KNOCK AT YOUR DOOR.

    (1) OPEN THE DOOR
    (2) IGNORE IT

> """)
    sel = getch()
    clear()

    if sel == "1":
        slow_print("""
A very large man with a wild beard ducks inside.

"Ah! There yeh are," he says. "I've been sent ter guide yeh to Diagon Alley.
Got yer Hogwarts letter, did yeh?"
""")
        break

    if sel == "2":
        slow_print("""
Your door is blown off its hinges.

A very large man with a wild beard steps through the dust.

"Ah! There yeh are," he says. "I've been sent ter guide yeh to Diagon Alley.
Got yer Hogwarts letter, did yeh?"
""")
        break

# ---------------------------------------------------------------------
# NEXT CHOICE
# ---------------------------------------------------------------------

while True:
    slow_print("""
    (1) GO WITH THE MAN
    (2) STAY WHERE YOU ARE

> """)
    sel = getch()

    if sel == "1":
        clear()
        slow_print("You follow the large man outside.\n")
        break

    if sel == "2":
        clear()
        slow_print("""
You decide to stay where you are.

The man sighs deeply. "Right. Stubborn one, eh?"

Before you can react, he gently—but firmly—picks you up under one arm
and starts walking toward the street.

"Come on now. Diagon Alley won't wait all day."
""")
        break

slow_print("""
A giant blue motorcycle is parked outside. 
The man props you up on the seat and settles in behind you.

The engine growls like a dragon waking up.

Before you can ask a single question, the bike lifts off the ground —
slowly at first, then rising higher and higher.

You, the large man, and the motorcycle are suddenly flying.
""")
slow_print("""
              .
               					
              |					
     .               /				
      \       I     				
                  /
        \  ,g88R_
          d888(`  ).                   _
 -  --==  888(     ).=--           .+(`  )`.
)         Y8P(       '`.          :(   .    )
        .+(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .=(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.:(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'
                                        	
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.
""")
slow_print("""
The wind whips past your ears as the motorcycle climbs higher.

The man pats your shoulder gently. 
"Reckon I should introduce meself. Name’s Rubeus Hagrid."

He gives a small, proud nod.

"Keeper of Keys and Grounds at Hogwarts. 
Dumbledore sent me ter fetch yeh. Figured yeh might need a bit o’ guidance
gettin’ to Diagon Alley and all."
""")
input("\nPress [ENTER] to continue... ")
slow_print("""
The motocycle slows to a halt, landing safely on the ground. In front of you, you see a large 
""")
