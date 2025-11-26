import time
import random
import os
import sys
import tty
import termios
import shutil

GOLD = "\033[38;5;220m"
RED = "\033[38;5;196m"
WHITE = "\033[97m"
CYAN = "\033[38;5;51m"
RESET = "\033[0m"

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.04):
    for line in text.split("\n"):
        print(line)
        time.sleep(delay)

def draw_magic_beam(pos, win=False):
    columns = shutil.get_terminal_size().columns
    width = max(60, columns - 4)
    center = width // 2
    core_center = center + pos * 2
    core_center = max(8, min(width - 8, core_center))
    core = f"{WHITE}[OOO||OOO]{RESET}"
    if win:
        core = f"{GOLD}[***]{RESET}"
    core_len = len("[OOO||OOO]")
    left_len = core_center - (core_len // 2) - 4
    right_len = width - (left_len + core_len + 4)
    left_len = max(1, left_len)
    right_len = max(1, right_len)
    left_beam = GOLD + "0Oo+" + "-" * left_len + RESET
    right_beam = RED + "-" * right_len + "+oO0" + RESET
    beam_line = left_beam + core + right_beam
    orb = "[oOOo]"
    orb_offset = core_center - len(orb) // 2
    orb_line_top = " " * orb_offset + CYAN + orb + RESET
    orb_line_bottom = " " * orb_offset + CYAN + orb + RESET
    debris = [" "] * len(beam_line)
    for _ in range(8):
        debris[random.randint(0, len(beam_line) - 1)] = "*"
    debris_line = "".join(debris)
    if win:
        explosion = GOLD + " " * (core_center - 4) + "BOOM" + RESET
        return orb_line_top + "\n" + beam_line + "\n" + orb_line_bottom + "\n" + debris_line + "\n" + explosion
    return orb_line_top + "\n" + beam_line + "\n" + orb_line_bottom + "\n" + debris_line

def priori_incantatem_clash(difficulty=12):
    clear()
    slow_print("Your wand connects with the opponent. Energy beams appear.")
    slow_print("A bright core forms between the beams.\n")
    slow_print("PRIORI INCANTATEM!\n")
    time.sleep(1)
    slow_print("Press the keys that appear. Correct keys push the core forward.")
    slow_print("Mistakes or slow input push the core back.\n")
    time.sleep(1)
    score = 0
    max_time = 1.15
    pos = 0
    limit = 10
    while score < difficulty:
        clear()
        print(draw_magic_beam(pos))
        print("\n")
        needed = random.choice("asdfjkl;")
        slow_print(f"Press: {needed}\n")
        start = time.time()
        ch = getch()
        reaction = time.time() - start
        if ch != needed:
            slow_print("Incorrect key.")
            pos -= 2
            if pos <= -limit:
                slow_print("\nYou lose control of the beam.")
                return "lose"
            time.sleep(0.3)
            continue
        if reaction > max_time:
            slow_print("Too slow.")
            pos -= 2
            if pos <= -limit:
                slow_print("\nThe enemy beam overpowers yours.")
                return "lose"
            time.sleep(0.3)
            continue
        score += 1
        pos += 1
        if pos > limit:
            pos = limit
        max_time *= 0.92
        slow_print("Progress.\n")
        time.sleep(0.25)
    clear()
    print(draw_magic_beam(pos, win=True))
    slow_print("\nFinal surge of energy.")
    slow_print("You overpower the opponent.\n")
    slow_print("You win the beam clash.\n")
    return "win"

# Examples
SPELLS = {
    "protego": {"type": "shield"},
    "expelliarmus": {"type": "disarm"},
    "stupefy": {"type": "attack"},
    "flipendo": {"type": "knockback"},
    "sidestep": {"type": "dodge"},
    "lumos": {"type": "useless", "message": "Your wand glows. It does not help in this duel."},
    "nox": {"type": "useless", "message": "You put out your light. Nothing changes."},
    "reparo": {"type": "useless", "message": "There is nothing here that needs repairing."},
    "alohomora": {"type": "useless", "message": "There are no locks to open here."},
    "wingardium leviosa": {
        "type": "utility",
        "chance_to_affect_enemy": 0.10,
        "chance_to_affect_environment": 0.40,
        "enemy_message": "Malfoy rises slightly into the air and flails.",
        "environment_message": "A nearby chair floats into the air.",
        "nothing_message": "The spell lifts nothing useful."
    },
    "aguamenti": {
        "type": "utility",
        "chance_to_affect_enemy": 0.05,
        "chance_to_affect_environment": 0.30,
        "enemy_message": "A jet of water hits Malfoy in the face.",
        "environment_message": "Water spills across the floor.",
        "nothing_message": "A small stream of water arcs away harmlessly."
    }
}

PLAYER_SPELLBOOK = [
    "protego",
    "expelliarmus",
    "stupefy",
    "flipendo",
    "sidestep",
    "wingardium leviosa",
    "lumos",
    "reparo",
    "aguamenti",
    "alohomora"
]

def cast_spell(prompt, player_spellbook):
    slow_print(prompt)
    slow_print("\nAvailable spells:")
    for s in player_spellbook:
        slow_print(f" - {s}")
    print()
    spell = input("> ").strip().lower()
    if spell not in player_spellbook:
        slow_print("You have not learned that spell.")
        return None, None
    return spell, SPELLS.get(spell, {"type": "useless"})

def handle_non_duel_spell(sdata):
    t = sdata["type"]
    if t == "useless":
        slow_print(sdata.get("message", "The spell has no useful effect."))
        return "no_effect"
    if t == "utility":
        rnd = random.random()
        enemy_chance = sdata.get("chance_to_affect_enemy", 0)
        env_chance = sdata.get("chance_to_affect_environment", 0)
        if rnd < enemy_chance:
            slow_print(sdata.get("enemy_message", "It affects the opponent."))
            return "enemy_effect"
        if rnd < enemy_chance + env_chance:
            slow_print(sdata.get("environment_message", "Something nearby reacts."))
            return "environment_effect"
        slow_print(sdata.get("nothing_message", "The spell fizzles."))
        return "no_effect"
    return "no_effect"

def duel_prototype(name, player_spellbook):
    clear()
    slow_print(f"{name} raises his wand.\n")
    time.sleep(1)
    advantage = 0
    enemy_staggered = False
    clear()
    slow_print(f"{name} casts Stupefy.\n")
    spell, sdata = cast_spell("Choose a spell to respond:", player_spellbook)
    if spell is None:
        slow_print("\nYou fail to respond in time.")
        return "lose"
    stype = sdata["type"]
    if stype == "shield":
        slow_print("\nYou block the spell.")
        advantage += 1
    elif stype == "dodge":
        slow_print("\nYou avoid the spell.")
    elif stype == "disarm":
        slow_print("\nYour spell collides with his. He staggers.")
        enemy_staggered = True
        advantage += 2
    elif stype in ("useless", "utility"):
        result = handle_non_duel_spell(sdata)
        if result == "enemy_effect":
            advantage += 1
        else:
            slow_print("You do not counter the attack properly.")
            return "lose"
    else:
        slow_print("That spell does not counter Stupefy.")
        return "lose"
    time.sleep(1)
    if enemy_staggered:
        slow_print(f"\n{name} is off balance.\n")
        spell, sdata = cast_spell("Cast a follow up spell:", player_spellbook)
        if spell:
            stype = sdata["type"]
            if stype == "disarm":
                slow_print("\nYou disarm your opponent. You win the duel.")
                return "win"
            elif stype == "attack":
                slow_print("\nYour attack lands.")
                advantage += 1
            elif stype == "knockback":
                slow_print("\nThe spell knocks him back.")
                advantage += 2
            elif stype in ("useless", "utility"):
                if handle_non_duel_spell(sdata) == "enemy_effect":
                    advantage += 1
            else:
                slow_print("The spell has little effect.")
        else:
            slow_print("You hesitate. He recovers.")
    time.sleep(1)
    clear()
    slow_print(f"{name} casts Flipendo.\n")
    spell, sdata = cast_spell("Counter the spell:", player_spellbook)
    if spell is None:
        slow_print("\nYou are hit by the blast.")
        return "lose"
    stype = sdata["type"]
    if stype == "shield":
        if advantage > 0:
            slow_print("\nYour shield holds.")
        else:
            slow_print("\nYour shield breaks.")
            return "lose"
    elif stype == "dodge":
        if random.random() < 0.7:
            slow_print("\nYou dodge.")
        else:
            slow_print("\nYou are hit.")
            return "lose"
    elif stype == "disarm":
        if advantage >= 1:
            slow_print("\nYou disrupt his spell.")
            advantage += 1
        else:
            slow_print("\nYour spell is overpowered.")
            return "lose"
    elif stype in ("useless", "utility"):
        if handle_non_duel_spell(sdata) != "enemy_effect":
            slow_print("You fail to counter the spell.")
            return "lose"
    else:
        slow_print("That spell does not counter Flipendo.")
        return "lose"
    time.sleep(1)
    clear()
    slow_print("Both of you raise your wands.")
    slow_print("The beams collide.\n")
    time.sleep(1)
    difficulty = 10 + max(0, 3 - advantage)
    return priori_incantatem_clash(difficulty)


if __name__ == "__main__":
    result = duel_prototype("Draco Malfoy", PLAYER_SPELLBOOK)
    print("WIN" if result == "win" else "LOSE")

