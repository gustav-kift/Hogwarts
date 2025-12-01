import os
import shutil
import sys, tty, termios
import time
import duel_engine as de
from wand_quiz_engine import load_tables, compute_wand
import random

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def text(msg, speed=0.03):
    for line in msg.split("\n"):
        print(line)
        time.sleep(speed)

def center_print(lines):
    width = shutil.get_terminal_size().columns
    for line in lines:
        print(line.center(width))
        time.sleep(0.02)

# Boot up
cls()
text("MINISTRY MAGIC TERMINAL [v2.4]", 0.02)
text("(c) 1991 Department of Mysteries", 0.02)
time.sleep(0.5)
text("Connecting to Floo Network...", 0.05)
text("System Ready.\n")
input("Press [ENTER] to login... ")
cls()

# Setup
text("ENTER FIRST NAME")
fname = input("> ")
text("\nENTER LAST NAME")
lname = input("> ")
cls()

name = f"{fname} {lname}"

def get_pronouns():
    print("SELECT PRONOUNS")
    print("1. She/Her")
    print("2. He/Him")
    print("3. They/Them")
    return get_key()

print("Updating records...")
time.sleep(0.5)
cls()

while True:
    choice = get_pronouns()
    if choice == "1":
        pronouns = "Ms. "
        break
    elif choice == "2":
        pronouns = "Mr. "
        break
    elif choice == "3":
        pronouns = "Mx. "
        break

cls()

# The Owl
text("A barn owl swoops down and drops a thick yellowish envelope at your feet.\n")

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
center_print(owl_art)

text("\nIt's addressed to you. The ink is emerald green.")
print("\n1. Ignore it")
print("2. Pick it up")

if get_key() == "1":
    cls()
    text("You ignore it. But more come.")
    text("Hundreds of them. Through the chimney. Under the door.")
    text("Eventually, you have to pick one up.")
    time.sleep(1)

cls()
text("The seal is a coat of arms with a lion, an eagle, a badger, and a snake.\n")
input("Press [ENTER] to rip it open... ")
cls()

width = shutil.get_terminal_size().columns
print("HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY".center(width))
print("Headmaster: Albus Dumbledore".center(width))

text(f"""
Dear {pronouns}{lname},

We are pleased to inform you that you have been accepted at Hogwarts School of
Witchcraft and Wizardry.

Term begins on 1 September. We await your owl by no later than 31 July.

Yours sincerely,
Minerva McGonagall
Deputy Headmistress
""")

input("Press [ENTER] to see the supply list... ")
cls()

text("""
REQUIRED:
- 3 sets of plain work robes (black)
- 1 pointed hat (black) for day wear
- 1 pair of protective gloves (dragon hide)
- 1 winter cloak

BOOKS:
- Standard Book of Spells (Grade 1)
- A History of Magic
- Magical Theory
- A Beginner's Guide to Transfiguration
- One Thousand Magical Herbs and Fungi
- Magical Drafts and Potions
- Fantastic Beasts and Where to Find Them
- The Dark Forces: A Guide to Self-Protection

EQUIPMENT:
- 1 Wand
- 1 Cauldron (pewter, size 2)
- 1 Set of phials
- 1 Telescope
- 1 Set brass scales

(Students may bring an owl OR a cat OR a toad)
""")

text("\nPARENTS ARE REMINDED THAT FIRST YEARS ARE NOT ALLOWED THEIR OWN BROOMSTICK.")
input("\nPress [ENTER] continue... ")
cls()

# Hagrid
while True:
    text("BOOM.")
    text("Someone is knocking on the door. Hard.")
    print("\n1. Open the door")
    print("2. Hide")
    
    sel = get_key()
    cls()

    if sel == "1":
        text("You open the door.")
        text("A giant man almost fills the frame. He looks wild, but his eyes are kind.")
        text("\n'Sorjeh,' he says. 'Didn't mean to startle yeh.'")
        break
    if sel == "2":
        text("BOOM.")
        text("The door flies off its hinges.")
        text("A giant man steps over it. 'Sorjeh,' he grunts.")
        break

text("""
'Name's Rubeus Hagrid. Keeper of Keys and Grounds at Hogwarts.'

He looks at you and grins.

'Dumbledore sent me. Reckon you'll need help gettin' your things.'
""")

input("Press [ENTER]... ")
cls()

text("""
He leads you to a massive motorcycle parked on the street.

'Hop on,' he says.

The engine roars like a dragon. Suddenly, the wheels lift off the pavement.
You're flying. The city lights shrink below you.
""")

text("""
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
                                        	
""")
text("'Hang on tight!' Hagrid yells over the wind.")
input("\nPress [ENTER] to land... ")
cls()

text("You touch down in a dingy London alleyway.")
text("Hagrid leads you into a pub called 'The Leaky Cauldron'.")
text("It's dark and smells like sherry. Everyone seems to know Hagrid.")
input("Press [ENTER] to go out back... ")
cls()

text("You stand facing a brick wall in the trash area.")
text("'Stand back, Harry... er, sorry, force of habit. Stand back.'")
text("\nHagrid taps a specific brick with his pink umbrella.")
time.sleep(0.5)
text("\nThe bricks wiggle, then rotate. A hole appears and grows wider.")
text("Suddenly, you're looking through an archway onto a cobbled street.")

diagon_art = [
"⠀⠀⢠⡤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⠀⠀",
"⠀⠀⣼⡜⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢞⣇⠀",
"⢀⡾⡍⠀⠀⠀⠀⠀⣦⠤⡀⢠⡄⠀⣄⠀⢀⠤⢤⠀⡠⢤⡀⣆⠀⣤⠀⠀⠀⡄⠀⣤⠀⠰⡄⠀⢠⡤⠆⢢⡀⡰⠀⠀⠀⠀⠀⢋⣧",
"⢸⣷⠀⢀⠀⠀⠀⠀⣿⠀⣿⢸⡇⢀⢻⠀⣾⠀⣀⢼⠇⠀⡇⣿⠄⣯⠀⠀⠸⡇⠀⣻⠀⠀⡇⠀⢸⣇⡀⠀⣧⠃⠀⠀⠀⠀⡀⢸⢸",
"⢸⡿⠀⠈⠀⠀⠀⠀⣿⠀⣿⢸⡇⠸⢼⡆⢿⠀⣿⢸⡆⠀⡇⣿⠰⡿⠀⠀⡦⣷⠀⣻⠀⠀⡇⠀⢸⡏⢁⠀⣽⠀⠀⠀⠀⠀⠁⢸⢸",
"⠈⢷⣣⠀⠀⠀⠀⠀⠛⠒⠁⠘⠃⠄⠀⠣⠈⠂⠋⠀⠑⠚⠁⠛⠀⠘⠀⠐⠀⠘⠂⠛⠐⠰⠓⠚⠘⠃⠊⠀⠛⠀⠀⠀⠀⠀⢀⣬⡟",
"⠀⠀⢻⢣⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⢮⠏⠀",
"⠀⠀⠈⠓⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠚⠀⠀",
]
center_print(diagon_art)

text(f"\nIt's packed. Cauldrons, owls, broomsticks. Magic everywhere.")
text(f"'Welcome,' Hagrid beams. 'To Diagon Alley.'")
input("\nPress [ENTER] to walk in... ")
cls()

def run_ollivanders():
    cls()
    text("'Makers of Fine Wands since 382 B.C.'")
    text("The shop is tiny. Thousands of narrow boxes are piled to the ceiling.")
    
    ollivander_art = [
        "⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿",
        "⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠶⠖⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⠀⠀⠀⠀⢀⡀⠤⠤⣀⡀⠀⢀⣀⣠⠤⠿⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⠀⠀⡠⠊⢀⣀⠠⠄⠒⠋⢫⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⠀⢶⠅⡨⠒⠀⠻⠁⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⢸⡗⣦⠂⠀⢲⡔⠀⠐⢢⠒⣔⠀⠲⠀⢰⡄⠐⠦⡀⠐⠂⠲⠒⠢⡀⢒⠐⠢⠐⡒⠢⡄⢠⠒⠄⠀⣿",
        "⣿⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⢀⣿⠁⣿⠀⢀⢸⡆⢀⡀⠤⠀⠸⡄⠁⢀⠁⢳⡀⡁⠘⢦⠀⢸⠀⢀⡟⢘⠀⢃⡀⡄⠲⡅⢠⠙⢲⠀⣿",
        "⣿⠀⠀⠀⠹⣦⣀⠀⠀⣀⣤⠟⠁⠀⢈⡈⠀⢁⠀⠁⠀⠉⠀⠀⠁⠀⠁⠀⠀⠁⠈⠀⠀⠀⠁⠀⠁⠀⠈⠁⠀⢈⠁⠀⣈⣀⡁⠀⠀⣿",
        "⣿⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⢰⠀⢹⣥⡞⣶⡖⡆⣶⡇⣦⢸⣴⡖⡆⠘⣼⢡⣦⣶⠀⣷⡄⡆⣶⡆⡆⢱⠃⠊⡎⡌⢣⠀⠀⠀⣿",
        "⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿",
        "⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿",
    ]
    center_print(ollivander_art)

    text("\nAn old man slides out from behind a shelf.")
    text(f"'Hello,' he says softly. 'I wondered when I'd be seeing you, {name}.'")
    text("'Mr. Ollivander, at your service.'")

    input("\nPress [ENTER]... ")
    cls()

    tables = load_tables()

    text("'Hold out your arm. Which is your wand arm?'")
    text("(Let's assume it's the right).")
    text("\n'Now... tell me.'")

    # Quiz - simplified
    print("\nWhat is your eye color?")
    eyes = tables["eyes"]
    eyes_list = [e for e in eyes if e.lower() != "other"] + (["Other"] if "Other" in eyes else [])
    
    for i, e in enumerate(eyes_list, 1):
        print(f"{i}) {e}")
    
    while True:
        ch = get_key()
        if ch.isdigit() and 1 <= int(ch) <= len(eyes_list):
            eye = eyes_list[int(ch)-1]
            break
    cls()

    print("What trait do you value most?")
    traits = tables["traits"]
    for i, t in enumerate(traits, 1):
        print(f"{i}) {t}")
    
    while True:
        ch = get_key()
        if ch.isdigit() and 1 <= int(ch) <= len(traits):
            trait = traits[int(ch)-1]
            break
    cls()

    print("Where does your mind go when it wanders?")
    paths = ["The Sea", "The Forest", "The Castle"]
    for i, p in enumerate(paths, 1):
        print(f"{i}) {p}")
    
    while True:
        ch = get_key()
        if ch in ["1","2","3"]:
            path = paths[int(ch)-1]
            break
    cls()

    print("Pick an object from the shelf:")
    artefacts = tables["artefacts"]
    # Reorder just for display cleanliness
    top_picks = ["dusty bottle","old black glove","golden key","bound-up scroll","glittering jewel","silver dagger","ornate mirror"]
    display_arts = [a for a in top_picks if a in artefacts] + [a for a in artefacts if a not in top_picks]

    for i, a in enumerate(display_arts, 1):
        print(f"{i}) {a}")
    
    while True:
        ch = get_key()
        if ch.isdigit() and 1 <= int(ch) <= len(display_arts):
            artefact = display_arts[int(ch)-1]
            break
    cls()

    print("What are you afraid of?")
    fears = ["Darkness", "Fire", "Heights", "Tight Spaces", "Isolation"]
    for i, f in enumerate(fears, 1):
        print(f"{i}) {f}")
    
    while True:
        ch = get_key()
        if ch in ["1","2","3","4","5"]:
            fear_index = int(ch)-1
            break
    cls()

    print("How tall are you?")
    heights = [("Short", "short"), ("Average", "average"), ("Tall", "tall")]
    for i, (label, _) in enumerate(heights, 1):
        print(f"{i}) {label}")
    
    while True:
        ch = get_key()
        if ch in ["1","2","3"]:
            height_cat = heights[int(ch)-1][1]
            break
    cls()

    print("Date of birth - Even or Odd day?")
    print("1) Even")
    print("2) Odd")
    while True:
        ch = get_key()
        if ch == "1":
            parity = "even"
            break
        if ch == "2":
            parity = "odd"
            break
    cls()

    # Calculate
    answers = {
        "eye": eye, "trait": trait, "path": path, 
        "artefact": artefact, "fear_index": fear_index, 
        "height_cat": height_cat, "parity": parity
    }
    wand = compute_wand(answers, tables)

    # Result
    text("Ollivander disappears into the back.")
    text("He tries a few wands on you. 'No, no, definitely not that one.'")
    text("Finally, he hands you a plain box.")
    
    text(f"\n'{wand['wood']}. {wand['length']}. {wand['core']} core.'")
    text("'Give it a wave.'")

    input("\nPress [ENTER] to wave wand... ")
    cls()

    text("A stream of gold sparks shoots from the end.")
    text("The shop lights up. It feels warm in your hand.")
    text("\nOllivander claps quietly.")
    text(f"'Curious... {wand['flexibility']}. Very curious.'")
    text("'The wand chooses the wizard, remember that.'")

    global player_wand
    player_wand = wand

    input("\nPress [ENTER] to leave... ")
    cls()

def run_gringotts():
    cls()
    text("You approach a snowy white building that towers over the little shops.")
    text("A goblin in a scarlet and gold uniform bows as you walk in.\n")
    time.sleep(0.5)

    gringotts_art = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠶⠟⠛⠛⠛⠛⠻⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⣠⡴⠛⣋⠄⢒⠫⠁⠰⡀⠐⡄⠈⡉⠒⠠⢙⠛⣶⣀⡀⠀⠀⠀⠀",
        "⠀⠀⠀⣠⡾⢋⠅⢈⢠⠀⠀⣎⠴⠂⠡⠀⠉⠠⢹⠀⠀⡠⢨⠢⠙⢷⡄⠀⠀⠀",
        "⠀⠀⣴⠛⠠⢂⠢⡀⠩⠔⠀⠀⠀⢀⣀⡀⠀⡄⠀⠀⠈⠔⢁⣜⠨⢂⠙⣧⠀⠀",
        "⠀⣼⠋⠴⢑⡀⠁⠆⠁⣀⠔⡚⠉⠍⠉⢉⠙⠻⣆⠀⠀⠀⠁⠀⢀⣾⠀⠘⣷⠀",
        "⢸⡇⠀⣅⡁⠈⠑⢀⠜⠥⠄⢉⠈⠀⠀⠀⠑⠀⠘⣷⡄⠀⠀⠀⠀⠈⠆⠀⢸⡇",
        "⣿⠁⠀⡙⠁⠀⠉⣶⠒⠢⡈⢱⡄⠀⠀⠀⠒⠐⠂⠀⡈⠭⣐⡀⠀⢀⣧⣀⠈⣷",
        "⣿⠀⠀⢀⠀⠀⠀⣿⡀⠀⢠⡀⠋⠐⠀⠀⢀⡀⠀⠉⢌⠁⠀⠀⠀⠈⠘⠀⠀⣿",
        "⣿⡀⠀⠺⠓⠀⠀⢻⣟⣦⣀⠙⠉⠋⠀⢸⡿⠉⢻⣿⠋⠀⠀⠀⡐⢀⡤⢄⢀⡿",
        "⠸⣇⠀⠀⣁⡠⠄⠀⢻⣿⢷⣄⡈⠘⠀⠀⠉⠀⣸⣿⡀⠀⠀⠠⢐⠋⠄⠜⢸⠇",
        "⠀⢿⣄⠘⣁⠄⠀⠀⡀⠙⠻⠯⣷⣦⣤⣤⡶⠞⢡⠿⠧⠄⡀⢋⠲⢄⡀⢠⡿⠀",
        "⠀⠀⠻⣤⠀⠀⡤⢫⡸⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⡐⢌⠀⠀⠀⣡⡟⠀⠀",
        "⠀⠀⠀⠙⢷⣌⠀⠊⠀⢰⠃⠀⢶⠀⠂⡀⠒⠄⢸⠀⢣⠀⠈⠱⣠⡾⠏⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠙⠿⣤⣀⠃⠀⠀⠀⡞⠀⢣⠐⡆⠀⠣⠔⣁⣤⠾⠋⠀⠀⠀⠀ ",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠶⠶⣦⣤⣤⣤⣥⣴⠶⠞⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀"
    ]
    center_print(gringotts_art)

    text("\nThe Head Goblin looks over his wire-rimmed glasses.")
    text("'And does the young witch or wizard have their vault key?'")

    input("\nPress [ENTER]... ")
    cls()

    text("Hagrid begins rifling through his enormous pockets.")
    text("Dog biscuits... moldy sausages... a half-knitted tea cozy...")
    time.sleep(1)
    text("\n'Aha! Here yeh go,' he says, triumphantly holding up a small bronze key.")
    text("'This'll get yeh into yer vault.'")

    input("\nPress [ENTER]... ")
    cls()

    text("A goblin named Griphook leads you to a rattling cart.")
    text("You climb in beside Hagrid. The cart jerks forward with alarming speed.")

    width = shutil.get_terminal_size().columns

    ride_frames = [
        "[  CART  ]  >> ------------------",
        "----- [  CART  ]  >> ------------",
        "--------- [  CART  ]  >> --------",
        "------------- [  CART  ]  >> ----",
        "----------------- [  CART  ]  >> ",
    ]

    for f in ride_frames:
        cls()
        print(f.center(width))
        time.sleep(0.15)

    text("\nThe wind stings your face as you descend deeper into the tunnels.")
    text("The cart slows to a halt at the first stop.\n")

    input("Press [ENTER] to open your vault... ")
    cls()

    # ——— PLAYER VAULT (GETTING RICHES) ———
    text("Vault 129.")
    text("Griphook unlocks the door. A plume of cool air rushes out.\n")

    galleons = random.randint(80, 160)
    sickles = random.randint(20, 60)
    knuts = random.randint(20, 99)

    text("Inside, piles of coins shimmer in the torchlight.")
    time.sleep(0.5)
    coins_art = [
        "⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⡎⠼⢠⠀⠀⠈⠂⠀⠀⡠⠐⠂⠁⠐⢄⡀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⢰⣧⣚⠐⠙⢀⣄⡶⠀⠰⡀⠆⣳⣉⠍⠀⣴⠀⠀⠀",
        "⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣷⣦⣄⣿⣶⣶⣶⣿⡿⣿⣇⠀⠀",
        "⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣟⣽⣿⢿⣿⣿⣿⣿⣿⣿⡏⠀⠀",
        "⠀⠀⠀⠀⡖⡹⣿⣿⣿⣿⣾⣽⣿⣯⣻⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀",
        "⠀⠀⠀⢰⣿⢦⣼⣿⣿⣟⣻⣿⣿⣷⣿⣽⣿⣿⠟⢛⠟⣻⡇⠀⠀",
        "⠀⠀⣀⣸⣯⣿⣿⣿⣿⣿⣿⣯⠾⠿⠿⣿⣿⡷⠶⢤⠕⠺⠰⣺⡄",
        "⠀⣾⢽⣷⠟⣻⣿⣿⣿⣿⣿⣿⠿⠿⠾⡿⣿⣿⣥⣁⣄⣤⣴⣯⣿",
        "⢠⣿⣧⠿⣷⡿⠉⠻⣿⡿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⢿⣿⣿",
        "⠈⣿⣾⣿⣿⣿⣢⣻⣞⣉⣽⣿⣿⡾⢿⢿⣿⣿⣿⣿⣿⢿⣿⡿⣿",
        "⠀⣿⢿⣿⣿⣿⣿⣫⡷⢿⣿⣿⣯⣗⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿",
        "⠀⣟⣛⠿⢟⣿⣿⣿⣭⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿",
        "⠀⢸⣟⡚⣺⣿⣿⡻⠭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣿⣿",
        "⠀⢸⣿⣗⣍⣿⣿⣿⣷⣚⣿⣿⣿⡿⠛⣷⣿⠍⣿⣿⣷⣿⣷⣾⣿",
        "⠀⠀⠉⠙⠛⠉⢿⣮⠽⠯⢿⡿⢿⣍⣭⣴⠟⠀⠈⠻⢿⣽⣾⡿⠟",
        "⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
    ]
    center_print(coins_art)
    text(f"You collect: {galleons} Galleons, {sickles} Sickles, {knuts} Knuts.\n")

    global player_money
    player_money = {"g": galleons, "s": sickles, "k": knuts}

    text("'Right then,' Hagrid says. 'Now we’ve got one more stop.'")
    text("'Vault 713. Hogwarts business. Top secret.'")

    input("\nPress [ENTER] to continue deeper... ")
    cls()

    # ——— MYSTERIOUS 713 ———
    ride_frames_2 = [
        "------------------ << [  CART  ]",
        "------------ << [  CART  ] -----",
        "-------- << [  CART  ] ---------",
        "---- << [  CART  ] -------------",
        " << [  CART  ] -----------------",
    ]

    for f in ride_frames_2:
        cls()
        print(f.center(width))
        time.sleep(0.15)

    text("\nThe air grows colder. The tunnel walls tighten around you.")
    text("The cart stops in front of a massive, darkened vault door.\n")

    text("Vault 713.")
    text("The number glows faintly — like it's alive.\n")
    text("You feel a pull in your chest. The vault is… calling to you.\n")

    input("Press [ENTER]... ")
    cls()

    text("Griphook stiffens.")
    text("'No customer has business with Vault 713,' he says sharply.")
    text("'It is among the most heavily protected vaults in Gringotts.'\n")

    text("Hagrid clears his throat nervously.")
    text("'Er — best not get too interested. Hogwarts business.'\n")

    question = input("You can't help yourself. What do you ask Hagrid about Vault 713? > ")

    cls()
    text(f"You ask: \"{question}\"")
    text("\nHagrid nearly chokes on his own spit.")
    text("'Now now — no need t' worry yerself about THAT,' he says quickly.")
    text("But he doesn't look convinced by his own words.\n")

    input("Press [ENTER] to return to the surface... ")
    cls()

def run_malkins():
    text("Madam Malkin's Robes for All Occasions.")
    madam_malkins_art = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠚⠉⢡⡞⣹⣯⣻⡌⠉⠓⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⣀⣈⣫⣽⣿⣝⣁⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⠇⠀⠠⣾⣿⣻⡯⢩⣿⣿⣩⣵⢾⣽⣗⠄⠀⠘⣇⣀⡀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀",
        "⠀⠀⣠⣴⣒⣒⣳⣦⣄⣀⣀⣀⣀⣘⣢⣿⣧⣀⡐⣛⣡⣾⢇⡿⣾⣻⢾⡘⣧⣭⣙⣋⣀⣼⣻⣔⣃⣀⣀⣀⣀⣠⣴⣞⣓⣒⣦⣄⠀⠀",
        "⢀⡎⢉⣹⡯⣉⡉⠛⢻⣿⣿⣿⣿⣿⠿⠧⠖⢺⢿⣿⠿⣿⠟⠁⡽⣿⠭⠷⠾⢛⣽⣻⢿⠒⢻⠿⢿⣯⣭⣉⣛⠛⠛⠉⠛⢻⢏⡉⢱⡀",
        "⠘⣇⠫⠌⣻⠇⢲⣶⣽⠭⣋⣸⣥⡾⠶⠞⠒⠉⠁⠀⠀⠈⠀⡈⢡⠎⠉⠀⠀⠀⠐⠒⠋⠛⢚⠓⠶⠦⡽⣈⠩⣿⣶⡀⢜⣞⠡⠹⢸⠇",
        "⠀⠈⢳⡚⠿⠤⣿⣯⣧⣺⢋⣉⠉⣁⠀⠈⠀⠀⠀⠉⠀⠀⢠⣽⢯⡆⠀⣤⠂⠀⢠⡄⣶⢁⣘⡄⣴⣲⠙⣿⠻⣦⡻⣿⠈⡯⢓⡟⠁⠀",
        "⠀⠀⠀⠈⢸⣉⣿⣽⣿⢭⣤⠀⢠⡠⠀⠀⠀⢭⠁⠀⡀⢠⡠⣄⢘⢻⡌⣿⢀⢠⡔⡇⢹⣇⢸⡇⣧⢹⣪⣹⠃⠹⣿⢻⠕⡇⠁⠀⠀⠀",
        "⠀⠀⠀⠀⢸⣩⣷⢿⠤⠀⡿⣦⢹⡇⣀⡀⡄⣾⠘⣹⢸⣸⡏⣿⢨⢠⢻⣿⢠⣾⡇⣧⠸⡘⠾⠃⠁⠀⠁⠀⠈⠀⣿⢿⣟⡇⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠸⣀⣿⠾⣇⠀⠇⢿⢸⠇⣁⣿⡇⣷⢹⣸⡸⠇⠁⠉⢸⠸⠇⠏⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⢿⠰⡆⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢸⢺⣻⠰⢿⢬⠱⠎⡼⠿⠗⠧⠙⠙⠂⠀⠀⠀⠀⠄⠛⠦⠀⠀⠀⠁⠈⠀⠀⠀⠁⠈⠀⠀⠀⠀⣠⡯⠞⢸⠛⡇⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢸⠨⢽⠣⠤⢟⢤⠂⠠⠖⣿⠀⠸⡇⡾⡠⢿⢾⠑⡇⢸⠱⡩⢾⢅⠀⡴⣌⢤⣇⡄⢺⠛⠖⠈⣹⢫⡽⣼⣟⢒⡇⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢸⣉⣻⣶⣶⡉⢌⢗⡅⠁⡟⣇⠈⢉⣤⠄⡄⢠⠄⣰⠀⢄⢠⢠⣄⣠⣠⠠⡉⠀⣠⢻⡀⢀⣼⢣⣻⠿⢻⣟⡛⡇⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢈⢧⣽⡺⡘⣿⠎⣪⢺⡾⡛⠈⠓⣄⠁⠃⠁⠈⠀⠉⠁⠀⠈⠈⠈⠀⠈⢁⣡⢾⡥⢜⣷⡻⡳⣿⡏⣷⣿⣗⣶⡇⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠸⠦⢼⣷⣕⣾⣁⣂⢡⡹⣿⡳⢤⡨⠔⢶⣄⣀⣀⣀⡀⣀⢀⢀⣀⣠⣖⠋⢀⣄⠲⢷⢎⣕⣼⣽⣮⣿⣟⡗⣂⡇⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠠⣿⣻⡽⠺⣉⣃⣬⡦⣵⠘⢹⡻⣗⡟⠉⢐⣈⣉⣉⣿⣿⣿⣉⣑⣨⡽⢏⡟⢯⡋⠃⢮⠶⣡⣀⠹⠱⢮⣷⠴⡃⠀⠀⠀⠀",
        "⠀⠀⠀⠀⣸⡠⣾⣵⣶⣻⣻⠷⠾⣆⣶⣿⠵⠞⠚⢛⡭⢝⣛⣂⣈⣡⣉⣒⡶⠿⣉⣙⢻⠺⢽⡲⣦⠿⠶⠿⡽⣶⣦⣿⣭⢳⠀⠀⠀⠀",
        "⠀⠀⠀⣴⣹⣢⣬⣿⣿⣿⣿⣿⣯⣉⣨⣽⣿⣮⡝⢡⣾⣿⣟⣿⣿⡿⣿⣿⣿⢵⠄⠱⣭⣽⣭⣿⣿⣿⣿⣿⣿⣿⣯⣤⣼⣷⣷⠄⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠿⣿⣿⣿⣿⣿⣿⡿⠟⠣⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
    ]
    center_print(madam_malkins_art)
    text("\nA squat witch measures you up.")
    text("In the back, a pale boy is getting fitted.")
    text("'Hogwarts too?' he asks. 'Father's buying my books.'")
    text("He smirks. You decide you don't like him much.")
    input("Press [ENTER]... ")

def run_flourish():
    text("Flourish & Blotts.")
    flourish_blotts_art = [
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⢀⡾⡩⠹⢒⡶⠦⣤⣤⣤⣤⣤⡤⠤⠶⣚⠫⠐⠐⠩⢛⠶⢤⣤⣀⣀⣀⣀⣠⣤⠴⠖⡛⡹⣆⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⢀⣠⠶⠫⠈⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠒⠒⠒⠂⠀⠀⠉⠀⠀⠈⠨⠳⣄⡀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠊⠐⠂⠄⠠⡤⣍⠵⣱⡀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⡀⢠⢀⠅⡐⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⡰⣰⠒⡠⢀⠨⠡⠤⡀⠄⠀⠀",
             "⠀⢨⠱⠀⠚⠗⠀⡶⡀⡐⠀⠁⣇⢣⠀⠀⠀⠀⠀⠀⠀⠀⢱⢂⢀⠀⠀⢲⠈⠀⠀⠀⠀⠀⠀⠀⢀⢃⡅⠂⠪⠐⢠⡄⠰⠲⠀⡆⡒⠀",
             "⠀⠀⠴⢁⢒⢠⠐⠘⡇⠐⠀⣄⠌⢧⠓⢠⠀⠀⠀⠀⠸⠄⠰⠀⢨⠀⡜⣦⠠⠖⠀⠀⠀⠀⠠⢀⢊⠖⠀⠄⠐⠐⣣⠑⢀⠰⡀⠄⠡⠀",
             "⠈⠀⠁⡨⣭⠘⡂⢠⠙⠈⢀⡐⠄⡈⠠⠈⠰⡄⠀⠀⠀⠀⣈⠤⣈⡀⡧⠲⠀⠀⠀⠀⠀⡔⠈⠠⠈⠀⠁⠂⠀⡸⠁⠀⡃⢎⡡⠈⢁⠃",
             "⠀⠀⠀⠀⡗⠀⡴⠈⣀⠀⠪⠭⣐⠂⠠⠃⠇⡑⡄⠀⠀⠀⠀⠀⠠⠡⠁⠀⠀⠀⠀⠀⡐⠄⡁⠃⠀⠐⡈⡍⠀⠁⠃⢀⠁⠰⠈⠀⠀⠀",
             "⠀⠀⠀⠀⠘⠀⠀⠀⢸⡆⠒⠄⢣⡓⠦⠄⠁⢃⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠁⠀⠄⠃⢂⠀⢠⠁⠀⠀⠀⠘⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⡇⠠⣀⢍⠪⢗⣥⠸⠀⡶⠀⢸⠁⡔⠀⡀⣠⠡⢰⠀⠀⠆⠠⢁⡑⠆⢈⠁⡠⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠃⠀⠠⡌⢳⣀⠈⠃⢈⡁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⢈⠀⠂⢁⢀⠋⡠⠀⢀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⣤⣀⣤⠞⠔⠀⠀⠀⠀⠀⡈⢙⢶⠄⠇⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⠂⢔⠀⠃⡀⠈⠀⠀⠈⢌⢧⣀⣀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⣼⠃⠒⠀⠁⠀⠀⠀⠀⠀⠀⠢⣑⢂⡌⡀⣅⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠄⠂⡁⠀⠀⠀⠀⠀⠀⠑⠊⢉⢷⡀⠀⠀⠀⠀",
             "⠀⠀⠀⢰⡇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⣧⠀⠀⠀⠀",
             "⠀⠀⠀⢸⢰⠀⠀⢀⠄⠢⢂⡤⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠠⡀⣤⠀⣠⠀⠀⢀⡀⣀⠄⠀⠀⠰⢸⡄⠀⠀⠀",
             "⠀⠀⠀⢺⢸⠀⠀⢼⡇⠀⠀⡇⢠⢦⢠⡄⡄⣴⠄⢸⠁⠀⠄⡇⡄⠀⠠⡲⠀⠀⢀⣹⠇⢨⡀⡇⢠⢠⠀⡓⢸⠂⡄⡂⠀⢸⡇⠀⠀⠀",
             "⠀⠀⠀⢸⡈⠀⢠⠮⠒⠀⠠⡧⠸⠼⠠⡧⣤⢸⣤⢸⡄⠀⡧⣇⢇⠀⢠⠱⡒⡀⠀⣸⣬⡰⠃⢧⠸⣼⠀⡧⢸⡆⠤⠟⢠⢸⠃⠀⠀⠀",
             "⠀⠀⠀⠀⢧⠁⠙⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠠⡌⠀⠀⠁⠁⠁⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢄⡟⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠈⢧⡡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢌⡾⠁⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠳⣬⡂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣠⠏⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⣄⣂⠠⠀⣀⠀⠠⠄⠤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠤⠤⠤⠀⡀⢀⠀⠄⣂⡵⠚⠁⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠒⠖⠋⠉⠉⠉⠒⢥⡠⡀⠀⠀⠀⡠⢀⡵⠚⠉⠉⠉⠓⠦⠶⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡠⡀⢄⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣎⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
             "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"

    ]
    center_print(flourish_blotts_art)
    text("\nShelves stacked to the ceiling with spellbooks.")
    text("You buy your Standard Book of Spells.")
    text("You almost buy 'Curses and Counter-Curses', but Hagrid drags you away.")
    input("Press [ENTER]... ")

places = []

while True:
    text("\nYou're standing in the middle of the street.")
    text("Where do you want to go?")
    print("1. Ollivanders (Wand)")
    print("2. Gringotts (Bank)")
    print("3. Madam Malkin's (Robes)")
    print("4. Flourish & Blotts (Books)")
    print("5. Follow Hagrid (Continue)")

    sel = get_key()
    cls()

    if sel == "1":
        if "ollivanders" in places:
            text("You've already been to Ollivanders.")
            continue
        else:
            run_ollivanders()
            places.append("ollivanders")
    elif sel == "2":
        if "gringotts" in places:
            text("You've already been to Gringotts.")
            continue
        else:
            run_gringotts()
            places.append("gringotts")
    elif sel == "3":
        if "malkins" in places:
            text("You've already been to Madam Malkin's.")
            continue
        else:
            run_malkins()
            places.append("malkins")
    elif sel == "4":
        if "flourish" in places:
            text("You've already been to Flourish & Blotts.")
            continue
        else:
            run_flourish()
            places.append("flourish")
    elif sel == "5":
        text("'Right then,' says Hagrid. 'Time to get you a pet.'")
        break
    else:
        text("Invalid choice.")

import house_quiz
import duel_engine

cls()
text("Eeylops Owl Emporium.")
text("Hagrid says: Pick a pet. My treat.")

pets = ["Snowy Owl", "Barn Owl", "Tawny Owl", "Black Cat", "Ginger Cat", "Toad"]
for i, p in enumerate(pets, 1):
    print(f"{i}. {p}")

while True:
    c = get_key()
    if c in "123456":
        pet = pets[int(c)-1]
        break

text(f"You got a {pet}.")
input("Press ENTER...")

cls()
text("September 1st. King's Cross.")
text("You run at the wall between platforms 9 and 10.")
time.sleep(1)
cls()
text("Hogwarts Express.")
text("You find a seat.")
text("A redhead boy joins you. I'm Ron Weasley.")

text("Trolley lady comes by.")
print("1. Buy snacks")
print("2. Don't")

if get_key() == "1":
    text("You buy everything. Ron is happy.")
    player_money["g"] -= 2
else:
    text("You eat nothing.")

text("Three boys enter.")
text("It's Draco Malfoy.")
text("Malfoy: You'll find some families are better than others.")
print("1. Shake hand")
print("2. Refuse")

if get_key() == "1":
    text("You shake hands. Ron looks mad.")
else:
    text("You refuse. Malfoy sneers.")

input("Press ENTER to arrive...")

cls()
text("Hogsmeade Station.")
text("Boats take you to the castle.")
text("Great Hall.")
text("Sorting Ceremony.")

scores = {h: 0 for h in house_quiz.HOUSES}
questions = house_quiz.choose_quiz_questions()

for q in questions:
    cls()
    print(q["prompt"])
    for i, opt in enumerate(q["options"], 1):
        print(f"{i}) {opt['text']}")
    
    while True:
        k = get_key()
        if k.isdigit() and 1 <= int(k) <= len(q["options"]):
            sel = q["options"][int(k)-1]
            for h, v in sel["weights"].items():
                scores[h] += v
            break

house = house_quiz.choose_house(scores)
cls()
text(f"Sorting Hat shouts: {house.upper()}!")
input("Press ENTER...")

spells = ["lumos", "nox"]
times = ["Morning", "Afternoon", "Evening"]

for t in times:
    cls()
    print(f"Time: {t}")
    print("1. Charms (Flitwick)")
    print("2. Potions (Snape)")
    print("3. Defense Against Dark Arts (Quirrell)")
    print("4. Explore")
    
    c = get_key()
    cls()

    if c == "1":
        text("Charms.")
        text("Flitwick: Swish and flick.")
        print("1. Wingardium Leviosa")
        print("2. Wingardium Leviosar")
        if get_key() == "1":
            text("Correct.")
            if "wingardium leviosa" not in spells: spells.append("wingardium leviosa")
        else:
            text("Wrong.")

    elif c == "2":
        text("Potions.")
        text("Snape: What does asphodel and wormwood make?")
        print("1. Polyjuice")
        print("2. Draught of Living Death")
        if get_key() == "2":
            text("Correct.")
            if "aguamenti" not in spells: spells.append("aguamenti")
        else:
            text("Wrong. 5 points from Gryffindor.")

    elif c == "3":
        text("DADA.")
        text("Quirrell: Deflect the hex!")
        print("Press P now!")
        s = time.time()
        if get_key().lower() == 'p' and time.time() - s < 1:
            text("Blocked.")
            if "protego" not in spells: spells.append("protego")
            if "stupefy" not in spells: spells.append("stupefy")
        else:
            text("Too slow.")
            if "protego" not in spells: spells.append("protego")

    elif c == "4":
        text("You explore.")
        text("Found a book.")
        if "flipendo" not in spells: spells.append("flipendo")
        if "sidestep" not in spells: spells.append("sidestep")

cls()
text("Midnight.")
text("You hear voices.")
text("Corvus Yaxley and the Carrow twins are there.")
text("Yaxley: You have something we want.")
input("DUEL START...")

if "stupefy" not in spells and "flipendo" not in spells:
    spells.append("flipendo")

res = duel_engine.duel_prototype("Corvus Yaxley", spells)

cls()
if res == "lose":
    text("Yaxley laughs.")
    text("Avada Kedavra.")
    print("YOU DIED")
else:
    text("Yaxley falls.")
    text("But the Carrows are still standing.")
    text("They cast Sectumsempra together.")
    text("You can't block two spells.")
    text("You fall.")
    print("YOU DIED (But you won the duel)")

input()