#!/usr/bin/env python3
import random

HOUSES = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

# Hatstall tie-break priority: earlier wins
HATSTALL_PRIORITY = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


# ---------- Question data structure ----------

# Each question:
# {
#   "id": "string",
#   "set": 1..8,
#   "prompt": "text",
#   "options": [
#       {"text": "answer text", "weights": {"Gryffindor": 3, "Ravenclaw": 0, ...}},
#       ...
#   ]
# }

questions_by_set = {
    1: [],  # first question group
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],  # pet
    8: [],  # last question group
}

# ---------- Set 1: Dawn/Dusk, Forest/River, Moon/Stars ----------

questions_by_set[1].extend([
    {
        "id": "dawn_dusk",
        "set": 1,
        "prompt": "Dawn or dusk?",
        "options": [
            {"text": "Dawn", "weights": {"Gryffindor": 2, "Ravenclaw": 2}},
            {"text": "Dusk", "weights": {"Hufflepuff": 2, "Slytherin": 2}},
        ],
    },
    {
        "id": "forest_river",
        "set": 1,
        "prompt": "Forest or river?",
        "options": [
            {"text": "Forest", "weights": {"Gryffindor": 2, "Ravenclaw": 2}},
            {"text": "River",  "weights": {"Hufflepuff": 2, "Slytherin": 2}},
        ],
    },
    {
        "id": "moon_stars",
        "set": 1,
        "prompt": "Moon or stars?",
        "options": [
            {"text": "Moon",  "weights": {"Ravenclaw": 2, "Slytherin": 2}},
            {"text": "Stars", "weights": {"Gryffindor": 2, "Hufflepuff": 2}},
        ],
    },
])

# ---------- Set 8: Black/White, Heads/Tails, Left/Right ----------

questions_by_set[8].extend([
    {
        "id": "black_white",
        "set": 8,
        "prompt": "Black or White?",
        "options": [
            {"text": "Black", "weights": {"Gryffindor": 2, "Slytherin": 2}},
            {"text": "White", "weights": {"Ravenclaw": 2, "Hufflepuff": 2}},
        ],
    },
    {
        "id": "heads_tails",
        "set": 8,
        "prompt": "Heads or Tails?",
        "options": [
            {"text": "Heads", "weights": {"Ravenclaw": 2, "Hufflepuff": 2}},
            {"text": "Tails", "weights": {"Gryffindor": 2, "Slytherin": 2}},
        ],
    },
    {
        "id": "left_right",
        "set": 8,
        "prompt": "Left or Right?",
        "options": [
            {"text": "Left",  "weights": {"Ravenclaw": 2, "Slytherin": 2}},
            {"text": "Right", "weights": {"Gryffindor": 2, "Hufflepuff": 2}},
        ],
    },
])

# ---------- Set 3: Goblets, Instrument, Magical Garden, Boxes, Flutterby ----------

questions_by_set[3].extend([
    {
        "id": "boxes",
        "set": 3,
        "prompt": "Four boxes are placed before you. Which would you try and open?",
        "options": [
            {
                "text": "The small tortoiseshell box, embellished with gold, inside which some "
                        "small creature seems to be squeaking.",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "The gleaming jet black box with a silver lock and key, marked with a "
                        "mysterious rune that you know to be the mark of Merlin.",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "The ornate golden casket, standing on clawed feet, whose inscription "
                        "warns that both secret knowledge and unbearable temptation lie within.",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "The small pewter box, unassuming and plain, with a scratched message "
                        "upon it that reads ‘I open only for the worthy.’",
                "weights": {"Gryffindor": 3},
            },
        ],
    },
    {
        "id": "flutterby",
        "set": 3,
        "prompt": (
            "Once every century, the Flutterby bush produces flowers that adapt their scent "
            "to attract the unwary. If it lured you, it would smell of:"
        ),
        "options": [
            {
                "text": "A crackling log fire",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "The sea",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "Fresh parchment",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "Home",
                "weights": {"Hufflepuff": 3},
            },
        ],
    },
    {
        "id": "enchanted_garden",
        "set": 3,
        "prompt": "You enter an enchanted garden. What would you be most curious to examine first?",
        "options": [
            {
                "text": "The silver leafed tree bearing golden apples",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "The fat red toadstools that appear to be talking to each other",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "The bubbling pool, in the depths of which something luminous is swirling",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "The statue of an old wizard with a strangely twinkling eye",
                "weights": {"Gryffindor": 3},
            },
        ],
    },
    {
        "id": "goblets",
        "set": 3,
        "prompt": "Four goblets are placed before you. Which would you choose to drink?",
        "options": [
            {
                "text": "The foaming, frothing, silvery liquid that sparkles as though "
                        "containing ground diamonds.",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "The smooth, thick, richly purple drink that gives off a delicious smell "
                        "of chocolate and plums.",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "The golden liquid so bright that it hurts the eye, and which makes "
                        "sunspots dance all around the room.",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "The mysterious black liquid that gleams like ink, and gives off fumes "
                        "that make you see strange visions.",
                "weights": {"Slytherin": 3},
            },
        ],
    },
    {
        "id": "instrument",
        "set": 3,
        "prompt": "What kind of instrument most pleases your ear?",
        "options": [
            {
                "text": "The violin",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "The trumpet",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "The piano",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "The drum",
                "weights": {"Gryffindor": 3},
            },
        ],
    },
])

# ---------- Set 6: Bridge, Cheating, Muggle, Nightmare, Road, Street Cry ----------

questions_by_set[6].extend([
    {
        "id": "bridge_troll",
        "set": 6,
        "prompt": (
            "You and two friends need to cross a bridge guarded by a river troll who insists "
            "on fighting one of you before he will let all of you pass. Do you:"
        ),
        "options": [
            {
                "text": "Attempt to confuse the troll into letting all three of you pass "
                        "without fighting?",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "Suggest drawing lots to decide which of you will fight?",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "Suggest that all three of you should fight (without telling the troll)?",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "Volunteer to fight?",
                "weights": {"Gryffindor": 3},
            },
        ],
    },
    {
        "id": "cheating_exam",
        "set": 6,
        "prompt": (
            "One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling "
            "Quill. Now he has come top of the class in Charms, beating you into second place. "
            "Professor Flitwick is suspicious of what happened. He draws you to one side after "
            "his lesson and asks you whether or not your classmate used a forbidden quill. "
            "What do you do?"
        ),
        "options": [
            {
                "text": "Lie and say you don’t know (but hope that somebody else tells "
                        "Professor Flitwick the truth).",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "Tell Professor Flitwick that he ought to ask your classmate (and resolve "
                        "to tell your classmate that if he doesn’t tell the truth, you will).",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "Tell Professor Flitwick the truth. If your classmate is prepared to win "
                        "by cheating, he deserves to be found out. Also, as you are both in the "
                        "same house, any points he loses will be regained by you, for coming "
                        "first in his place.",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "You would not wait to be asked to tell Professor Flitwick the truth. "
                        "If you knew that somebody was using a forbidden quill, you would tell "
                        "the teacher before the exam started.",
                "weights": {"Slytherin": 3},
            },
        ],
    },
    {
        "id": "muggle_confronts",
        "set": 6,
        "prompt": (
            "A Muggle confronts you and says that they are sure you are a witch or wizard. "
            "Do you:"
        ),
        "options": [
            {
                "text": "Ask what makes them think so?",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "Agree, and ask whether they’d like a free sample of a jinx?",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "Agree, and walk away, leaving them to wonder whether you are bluffing?",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "Tell them that you are worried about their mental health, and offer to "
                        "call a doctor.",
                "weights": {"Hufflepuff": 3},
            },
        ],
    },
    {
        "id": "nightmare",
        "set": 6,
        "prompt": "Which nightmare would frighten you most?",
        "options": [
            {
                "text": "Standing on top of something very high and realizing suddenly that "
                        "there are no hand- or footholds, nor any barrier to stop you falling.",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "An eye at the keyhole of the dark, windowless room in which you are locked.",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "Waking up to find that neither your friends nor your family have any idea "
                        "who you are.",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "Being forced to speak in such a silly voice that hardly anyone can "
                        "understand you, and everyone laughs at you.",
                "weights": {"Slytherin": 3},
            },
        ],
    },
    {
        "id": "road",
        "set": 6,
        "prompt": "Which road tempts you most?",
        "options": [
            {
                "text": "The wide, sunny, grassy lane",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "The narrow, dark, lantern-lit alley",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "The twisting, leaf-strewn path through woods",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "The cobbled street lined with ancient buildings",
                "weights": {"Ravenclaw": 3},
            },
        ],
    },
    {
        "id": "street_cry",
        "set": 6,
        "prompt": (
            "Late at night, walking alone down the street, you hear a peculiar cry that you "
            "believe to have a magical source. Do you:"
        ),
        "options": [
            {
                "text": "Proceed with caution, keeping one hand on your concealed wand and an "
                        "eye out for any disturbance?",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "Draw your wand and try to discover the source of the noise?",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "Draw your wand and stand your ground?",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "Withdraw into the shadows to await developments, while mentally "
                        "reviewing the most appropriate defensive and offensive spells, "
                        "should trouble occur?",
                "weights": {"Ravenclaw": 3},
            },
        ],
    },
])

# ---------- Set 2: Hate to be called, After you died, Known to history, Potion ----------

questions_by_set[2].extend([
    {
        "id": "hate_to_be_called",
        "set": 2,
        "prompt": "Which of the following would you most hate people to call you?",
        "options": [
            {"text": "Ordinary", "weights": {"Slytherin": 3}},
            {"text": "Ignorant", "weights": {"Ravenclaw": 3}},
            {"text": "Cowardly", "weights": {"Gryffindor": 3}},
            {"text": "Selfish",  "weights": {"Hufflepuff": 3}},
        ],
    },
    {
        "id": "after_you_died",
        "set": 2,
        "prompt": "After you have died, what would you most like people to do when they hear your name?",
        "options": [
            {
                "text": "Miss you, but smile",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "Ask for more stories about your adventures",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "Think with admiration of your achievements",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "I don't care what people think of me after I'm dead; it's what they "
                        "think of me while I'm alive that counts",
                "weights": {"Slytherin": 3},
            },
        ],
    },
    {
        "id": "known_to_history",
        "set": 2,
        "prompt": "How would you like to be known to history?",
        "options": [
            {"text": "The Wise",  "weights": {"Ravenclaw": 3}},
            {"text": "The Good",  "weights": {"Hufflepuff": 3}},
            {"text": "The Great", "weights": {"Slytherin": 3}},
            {"text": "The Bold",  "weights": {"Gryffindor": 3}},
        ],
    },
    {
        "id": "potion",
        "set": 2,
        "prompt": "Given the choice, would you rather invent a potion that would guarantee you:",
        "options": [
            {"text": "Love",   "weights": {"Hufflepuff": 3}},
            {"text": "Glory",  "weights": {"Gryffindor": 3}},
            {"text": "Wisdom", "weights": {"Ravenclaw": 3}},
            {"text": "Power",  "weights": {"Slytherin": 3}},
        ],
    },
])

# ---------- Set 5: Power, Looking forward to learning, Most like to study ----------

questions_by_set[5].extend([
    {
        "id": "power_choice",
        "set": 5,
        "prompt": "If you could have any power, which would you choose?",
        "options": [
            {
                "text": "The power to read minds",
                "weights": {"Ravenclaw": 1, "Slytherin": 1},
            },
            {
                "text": "The power of invisibility",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "The power of superhuman strength",
                "weights": {"Hufflepuff": 3, "Slytherin": 1},
            },
            {
                "text": "The power to speak to animals",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "The power to change the past",
                "weights": {"Slytherin": 3, "Gryffindor": 1},
            },
            {
                "text": "The power to change your appearance at will",
                "weights": {"Ravenclaw": 3},
            },
        ],
    },
    {
        "id": "learning_at_hogwarts",
        "set": 5,
        "prompt": "What are you most looking forward to learning at Hogwarts?",
        "options": [
            {
                "text": "Apparition and Disapparition (being able to materialize and "
                        "dematerialize at will)",
                "weights": {"Slytherin": 3, "Gryffindor": 1},
            },
            {
                "text": "Transfiguration (turning one object into another object)",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "Flying on a broomstick",
                "weights": {"Gryffindor": 2, "Hufflepuff": 2},
            },
            {
                "text": "Hexes and jinxes",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "All about magical creatures, and how to befriend/care for them",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "Secrets about the castle",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "Every area of magic I can",
                "weights": {"Ravenclaw": 3},
            },
        ],
    },
    {
        "id": "study_creatures",
        "set": 5,
        "prompt": "Which of the following would you most like to study?",
        "options": [
            {
                "text": "Centaurs",
                "weights": {"Gryffindor": 3, "Ravenclaw": 1},
            },
            {
                "text": "Goblins",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "Merpeople",
                "weights": {"Hufflepuff": 2, "Slytherin": 2},
            },
            {
                "text": "Ghosts",
                "weights": {"Gryffindor": 3, "Ravenclaw": 1},
            },
            {
                "text": "Vampires",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "Werewolves",
                "weights": {"Gryffindor": 3, "Hufflepuff": 1},
            },
            {
                "text": "Trolls",
                "weights": {"Hufflepuff": 3, "Slytherin": 1},
            },
        ],
    },
])

# ---------- Set 7: Pet ----------

questions_by_set[7].append(
    {
        "id": "pet",
        "set": 7,
        "prompt": "If you were attending Hogwarts, which pet would you choose to take with you?",
        "options": [
            {"text": "Tabby cat",            "weights": {"Gryffindor": 3, "Slytherin": 1}},
            {"text": "Siamese cat",          "weights": {"Slytherin": 3}},
            {"text": "Ginger cat",           "weights": {"Slytherin": 3}},
            {"text": "Black cat",            "weights": {"Slytherin": 3}},
            {"text": "White cat",            "weights": {"Slytherin": 3}},
            {"text": "Tawny owl",            "weights": {"Ravenclaw": 3}},
            {"text": "Screech owl",          "weights": {"Ravenclaw": 2}},
            {"text": "Brown owl",            "weights": {"Ravenclaw": 3}},
            {"text": "Snowy owl",            "weights": {"Hufflepuff": 2, "Ravenclaw": 1}},
            {"text": "Barn owl",             "weights": {"Ravenclaw": 3}},
            {"text": "Common toad",          "weights": {"Hufflepuff": 3}},
            {"text": "Natterjack toad",      "weights": {"Hufflepuff": 3}},
            {"text": "Dragon toad",          "weights": {"Gryffindor": 2, "Hufflepuff": 1}},
            {"text": "Harlequin toad",       "weights": {"Hufflepuff": 3}},
            {"text": "Three toed tree toad", "weights": {"Hufflepuff": 2, "Ravenclaw": 1}},
        ],
    }
)

# ---------- Set 4: Difficult to deal with, Troll, Would you rather be ----------

questions_by_set[4].extend([
    {
        "id": "difficult_to_deal_with",
        "set": 4,
        "prompt": "Which of the following do you find most difficult to deal with?",
        "options": [
            {
                "text": "Hunger",
                "weights": {"Ravenclaw": 2, "Hufflepuff": 2},
            },
            {
                "text": "Cold",
                "weights": {"Hufflepuff": 2, "Slytherin": 2},
            },
            {
                "text": "Loneliness",
                "weights": {"Gryffindor": 3, "Hufflepuff": 1},
            },
            {
                "text": "Boredom",
                "weights": {"Gryffindor": 3, "Slytherin": 1},
            },
            {
                "text": "Being ignored",
                "weights": {"Ravenclaw": 3, "Slytherin": 1},
            },
        ],
    },
    {
        "id": "troll_headmaster_study",
        "set": 4,
        "prompt": (
            "A troll has gone berserk in the Headmaster’s study at Hogwarts. It is about to "
            "smash, crush and tear several irreplaceable items and treasures. In which order "
            "would you rescue these objects from the troll’s club, if you could?"
        ),
        "options": [
            {
                "text": "First, a nearly perfected cure for dragon pox. Then student records "
                        "going back 1000 years. Finally, a mysterious handwritten book full "
                        "of strange runes.",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "First, student records going back 1000 years. Then a mysterious "
                        "handwritten book full of strange runes. Finally, a nearly perfected "
                        "cure for dragon pox.",
                "weights": {"Slytherin": 3},
            },
            {
                "text": "First, a mysterious handwritten book full of strange runes. Then a "
                        "nearly perfected cure for dragon pox. Finally, student records "
                        "going back 1000 years.",
                "weights": {"Ravenclaw": 3},
            },
            {
                "text": "First, a nearly perfected cure for dragon pox. Then a mysterious "
                        "handwritten book full of strange runes. Finally, student records "
                        "going back 1000 years.",
                "weights": {"Gryffindor": 3},
            },
            {
                "text": "First student records going back 1000 years. Then, a nearly perfected "
                        "cure for dragon pox. Finally, a mysterious handwritten book full of "
                        "strange runes.",
                "weights": {"Hufflepuff": 3},
            },
            {
                "text": "First, a mysterious handwritten book full of strange runes. Then "
                        "student records going back 1000 years. Finally, a nearly perfected "
                        "cure for dragon pox.",
                "weights": {"Ravenclaw": 3, "Slytherin": 1},
            },
        ],
    },
    {
        "id": "rather_be",
        "set": 4,
        "prompt": "Which would you rather be:",
        "options": [
            {"text": "Envied",   "weights": {"Ravenclaw": 1, "Slytherin": 1}},
            {"text": "Imitated", "weights": {"Ravenclaw": 3}},
            {"text": "Trusted",  "weights": {"Gryffindor": 1, "Hufflepuff": 1}},
            {"text": "Praised",  "weights": {"Gryffindor": 3}},
            {"text": "Liked",    "weights": {"Hufflepuff": 3}},
            {"text": "Feared",   "weights": {"Slytherin": 3}},
        ],
    },
])


# ---------- Helper functions ----------

def ask_question(question, scores):
    print("\n" + "-" * 72)
    print(question["prompt"])
    print()
    for idx, opt in enumerate(question["options"], start=1):
        print(f"  ({idx}) {opt['text']}")
    print()

    while True:
        choice = input("Your choice (enter the number): ").strip()
        if not choice.isdigit():
            print("Please enter a number corresponding to your choice.")
            continue
        choice_idx = int(choice)
        if 1 <= choice_idx <= len(question["options"]):
            break
        print("Please choose a valid option number.")

    selected = question["options"][choice_idx - 1]
    for house, value in selected["weights"].items():
        scores[house] += value


def choose_quiz_questions():
    # First question: one from set 1
    first_q = random.choice(questions_by_set[1])

    # Middle questions: one from each of sets 2–7
    middle_questions = []
    for set_id in range(2, 8):
        if set_id == 8:
            continue
        q = random.choice(questions_by_set[set_id])
        middle_questions.append(q)

    random.shuffle(middle_questions)

    # Last question: one from set 8
    last_q = random.choice(questions_by_set[8])

    return [first_q] + middle_questions + [last_q]


def choose_house(scores):
    # Max score
    max_score = max(scores.values())
    winners = [h for h in HOUSES if scores[h] == max_score]
    if len(winners) == 1:
        return winners[0]

    # Hatstall: Gryffindor > Hufflepuff > Ravenclaw > Slytherin
    for house in HATSTALL_PRIORITY:
        if house in winners:
            return house
    # Fallback (shouldn't happen)
    return winners[0]


def main():
    print("Welcome to the Sorting Hat Quiz!\n")
    print("Answer honestly, and the Hat will do its work...\n")

    while True:
        scores = {h: 0 for h in HOUSES}
        quiz_questions = choose_quiz_questions()

        for q in quiz_questions:
            ask_question(q, scores)

        print("\n" + "=" * 72)
        print("Calculating your house...")
        print("=" * 72)

        house = choose_house(scores)

        print("\nYour final scores:")
        for h in HOUSES:
            print(f"  {h}: {scores[h]}")

        print("\nThe Sorting Hat shouts:")
        print(f"  *** {house.upper()}! ***\n")

        again = input("Would you like to take the quiz again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nThanks for playing! Mischief managed.\n")


if __name__ == "__main__":
    main()
