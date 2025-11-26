import time, random
import os
import sys, tty, termios
import shutil

# ANSI colors
GOLD = "\033[38;5;220m"
RED = "\033[38;5;196m"
WHITE = "\033[97m"
CYAN = "\033[38;5;51m"
RESET = "\033[0m"

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

# --------------------------------------------------------
#  PRIORI INCANTATEM BEAM CLASH
# --------------------------------------------------------

def draw_magic_beam(pos, win=False):
    """Stable, centered magic beam with no flicker + only '*' debris."""
    
    columns = shutil.get_terminal_size().columns
    width = max(60, columns - 4)

    # Beam position mapping
    center = width // 2
    core_center = center + pos * 2
    core_center = max(8, min(width - 8, core_center))

    # Core (no flicker)
    core = f"{WHITE}[OOO||OOO]{RESET}"
    if win:
        core = f"{GOLD}[***]{RESET}"

    core_len = len("[OOO||OOO]")  # use raw length to center correctly

    # Compute beam lengths
    left_len = core_center - (core_len // 2) - 4
    right_len = width - (left_len + core_len + 4)

    left_len = max(1, left_len)
    right_len = max(1, right_len)

    # Build beams
    left_beam = GOLD + "0Oo+" + "-" * left_len + RESET
    right_beam = RED + "-" * right_len + "+oO0" + RESET

    beam_line = left_beam + core + right_beam

    # Orb lines
    orb = "[oOOo]"
    orb_offset = core_center - len(orb)//2
    orb_line_top = " " * orb_offset + CYAN + orb + RESET
    orb_line_bottom = " " * orb_offset + CYAN + orb + RESET

    # Debris line (all '*' only)
    debris = [" "] * len(beam_line)
    for _ in range(8):
        idx = random.randint(0, len(beam_line)-1)
        debris[idx] = "*"
    debris_line = "".join(debris)

    # Win explosion line
    if win:
        explosion = GOLD + " " * (core_center-5) + "⚡ BOOOOM ⚡" + RESET
        return orb_line_top + "\n" + beam_line + "\n" + orb_line_bottom + "\n" + debris_line + "\n" + explosion

    return orb_line_top + "\n" + beam_line + "\n" + orb_line_bottom + "\n" + debris_line




def priori_incatatem_clash(difficulty=12):
    clear()
    slow_print("Your wand locks with your opponent’s — twin beams of magic erupt!")
    slow_print("A violent golden core forms between them!\n")
    slow_print("PRIORI INCANTATEM!\n", delay=0.04)
    time.sleep(1)

    slow_print("Mash the keys that appear — CORRECT keys push the core forward!")
    slow_print("Miss or hesitate and the enemy pushes YOU back.\n")
    time.sleep(1)

    score = 0
    max_time = 1.15
    pos = 0          # -10 = enemy winning, +10 = player winning
    pos_limit = 10

    while score < difficulty:
        clear()

        # Draw beam
        print(draw_magic_beam(pos))
        print("\n")

        needed = random.choice("asdfjkl;")
        slow_print(f"Press:  {needed}\n")

        start = time.time()
        ch = getch()
        reaction = time.time() - start

        # Wrong key
        if ch != needed:
            slow_print("Wrong! Your beam falters!")
            pos -= 2
            if pos <= -pos_limit:
                slow_print("\nYour magic collapses — you are overwhelmed!")
                return "lose"
            time.sleep(0.3)
            continue

        # Too slow
        if reaction > max_time:
            slow_print("Too slow! Their beam surges!")
            pos -= 2
            if pos <= -pos_limit:
                slow_print("\nThe enemy beam devours your magic!")
                return "lose"
            time.sleep(0.3)
            continue

        # Success
        score += 1
        pos += 1
        if pos > pos_limit:
            pos = pos_limit

        max_time *= 0.92  # increase pressure

        slow_print("Your beam pushes forward! Sparks explode!\n")
        time.sleep(0.25)

    # WIN
    clear()
    print(draw_magic_beam(pos))
    slow_print("\nA final explosion of golden light erupts!")
    slow_print("Your beam overwhelms the opponent — they are blasted backwards!\n")
    slow_print("You WIN the beam struggle!\n")

    return "win"



# --------------------------------------------------------
#  EVENT-BASED DUEL ENGINE WITH PRIORI INCANTATEM FINALE
# --------------------------------------------------------

def duel_prototype(name="Malfoy"):
    clear()

    slow_print(f"{name} raises his wand, smirking.\n")
    slow_print("“Let’s see what you’ve got.”\n")
    time.sleep(1)

    # Duel internal state
    enemy_staggered = False
    player_staggered = False
    advantage = 0

    # Spell input validator
    def cast(prompt, valid_spells):
        slow_print(prompt)
        spell = input("> ").strip().lower()
        if spell not in valid_spells:
            slow_print("\nYour spell fizzles… incorrect incantation!")
            return None
        return spell

    # --------------------------------------------------------
    # BEAT 1 — OPENING ATTACK
    # --------------------------------------------------------
    clear()
    slow_print(f'{name} shouts: "STUPEFY!" A red blast rockets toward you!\n')

    spell = cast(
        "TYPE A SPELL QUICKLY! (protego / duck / expelliarmus)",
        ["protego", "duck", "expelliarmus"]
    )

    if spell is None:
        slow_print("\nThe spell hits you squarely — you lose the duel.")
        return "lose"

    if spell == "protego":
        slow_print("\nYour shield absorbs the hit! The ground ripples.")
        advantage += 1

    elif spell == "duck":
        slow_print("\nYou duck just in time — heat scorches above your head.")

    elif spell == "expelliarmus":
        slow_print("\nYour spell collides with theirs! They stumble backwards!")
        enemy_staggered = True
        advantage += 2

    time.sleep(1)

    # --------------------------------------------------------
    # BEAT 2 — ENEMY STAGGERED COUNTER WINDOW
    # --------------------------------------------------------
    if enemy_staggered:
        slow_print(f"\n{name} staggers — wand arm exposed!\n")

        spell = cast(
            "TAKE ADVANTAGE! (stupefy / expelliarmus / flipendo)",
            ["stupefy", "expelliarmus", "flipendo"]
        )

        if spell is None:
            slow_print("\nYou hesitate — they regain their footing!")
            enemy_staggered = False

        else:
            if spell == "expelliarmus":
                slow_print("\nYour spell blasts his wand away!")
                slow_print("You WIN the duel!\n")
                return "win"

            if spell == "stupefy":
                slow_print("\nYour bolt hits! He reels in pain!")
                advantage += 1

            if spell == "flipendo":
                slow_print("\nHe crashes backwards onto the platform!")
                advantage += 2

    time.sleep(1)
    clear()

    # --------------------------------------------------------
    # BEAT 3 — ENEMY COUNTERATTACK
    # --------------------------------------------------------
    slow_print(f"{name} snarls and snaps his wand in a vicious arc.\n")
    slow_print('"FLIPENDO!" A roaring shockwave tears toward you!\n')

    spell = cast(
        "COUNTER IT! (protego / sidestep / expelliarmus)",
        ["protego", "sidestep", "expelliarmus"]
    )

    if spell is None:
        slow_print("\nYou fail to react — the shockwave crushes you.")
        return "lose"

    if spell == "protego":
        if advantage > 0:
            slow_print("\nYour shield holds — the blast breaks around you.")
        else:
            slow_print("\nYour shield cracks! You hit the ground hard!")
            player_staggered = True
            advantage -= 1

    elif spell == "sidestep":
        if random.random() < 0.7:
            slow_print("\nYou dive to the side just in time!")
        else:
            slow_print("\nYou dodge too slow — the wave clips you!")
            return "lose"

    elif spell == "expelliarmus":
        if advantage >= 1:
            slow_print("\nYour spell hits mid-cast! He screams and stumbles!")
            enemy_staggered = True
            advantage += 1
        else:
            slow_print("\nYour spell loses the clash — you're launched backward!")
            return "lose"

    time.sleep(1)
    clear()

    # --------------------------------------------------------
    # FINAL BEAT — PRIORI INCANTATEM COLLISION
    # --------------------------------------------------------

    slow_print("Both of you raise your wands — beams of magic burst forth!")
    slow_print("They collide violently, locking together in mid-air.\n")
    slow_print("The duel erupts into a deadly beam struggle!\n")

    time.sleep(1)

    result = priori_incatatem_clash(
        difficulty=10 + max(0, 3 - advantage)  # advantage makes the clash easier
    )

    return result



result = duel_prototype("Draco Malfoy")

if result == "win":
    print("WIN")
else:
    print("LOSE")

