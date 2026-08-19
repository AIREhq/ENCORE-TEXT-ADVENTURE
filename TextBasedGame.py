# Arielle Duncan
# IT 140 Project Two
# ENCORE: Text-Based Adventure Game

# Fixed width keeps the centered movie-screen look simple.
SCREEN_WIDTH = 120


def print_centered(text=""):
    print(str(text).center(SCREEN_WIDTH))


def print_lines(lines):
    for line in lines:
        print_centered(line)


def centered_input(message):
    spaces = (SCREEN_WIDTH - len(message)) // 2
    if spaces < 0:
        spaces = 0
    return input((" " * spaces) + message).strip()


def pause_game(message="Press Enter to continue..."):
    print()
    centered_input(message)


def big_space():
    print("\n" * 6)


def room_space():
    print("\n" * 2)


def show_main_menu(lore_unlocked):
    big_space()
    print_centered("ENCORE")
    print()
    print_centered("MAIN MENU")
    print()
    print_centered("Play")

    if lore_unlocked:
        print_centered("Lore")
    else:
        print_centered("Lore - Classified")

    print_centered("Exit")
    print()

    while True:
        choice = centered_input("Enter your selection: ").lower()

        if choice == "play" or choice == "lore" or choice == "exit":
            return choice

        print()
        print_centered('Type "play," "lore," or "exit."')
        print()


def show_instructions():
    big_space()
    print_centered("ENCORE")
    print()

    print_lines([
        "Five years after the Tattletale murders,",
        "the town of Mareshell hosts the world premiere",
        'of "Staring U."',
        "",
        "The final screening fills for the night.",
        "",
        "You lock the theater's front doors",
        "and return to the lobby.",
        "",
        "Tonight was supposed to be just another shift.",
        "",
        "It wasn't.",
        "",
        "A fellow employee is found unconscious",
        "near the lobby.",
        "",
        "Staff are told to clear the theaters,",
        "block off the lobby entrance,",
        "and move guests through the rear exits",
        "while police are on the way.",
        "",
        "Find everything you'll need.",
        "",
        "The Tattletale is still inside.",
        "",
        "Don't let him find you first.",
        "",
        "",
        "AVAILABLE GAME COMMANDS",
        "",
        "Move",
        "go North     go South     go East     go West",
        "",
        "Search",
        'Type "search" to look for hidden evidence.',
        "",
        "Collect",
        'Type "grab" followed by the exact item name shown in single quotes.',
        'Example: grab Flashlight',
        "",
        "Inventory",
        'Type "inventory" to review what you have collected.',
        "",
        "Help",
        'Type "help" to review the game commands.',
        "",
        'Type "exit" to end the game early.'
    ])

    print()
    choice = centered_input("Press Enter to begin...").lower()

    if choice == "exit":
        return False

    return True


def show_lore_locked():
    big_space()
    print_centered("LORE CLASSIFIED")
    print()
    print_lines([
        "The case file remains sealed.",
        "",
        "Complete the perfect showing",
        "to unlock the classified case file.",
        "",
        'Type "return" to go back.'
    ])
    print()

    while True:
        choice = centered_input("> ").lower()
        if choice == "return":
            return
        print()
        print_centered('Type "return" to go back.')


def show_lore():
    big_space()
    print_centered("CASE FILE #001")
    print_centered("CLASSIFIED")
    print()
    print_centered("Access Granted...")
    pause_game("Press Enter to open the case file...")

    pages = [
        (
            "CASE INFORMATION",
            [
                "Case Number: MSPD-05-417",
                "",
                "Location: Mareshell",
                "",
                "Primary Crime Scene: Mareshell Grand Cinema",
                "",
                "Primary Suspect: Owen Mills",
                "",
                'Alias: "The Tattletale"',
                "",
                "Case Status: Closed"
            ]
        ),
        (
            "BACKGROUND",
            [
                "The Mills family helped establish Mareshell",
                "generations ago.",
                "",
                "Their name became connected to the town's",
                "wealth, influence, and history.",
                "",
                "Owen Mills grew up surrounded by people",
                "who respected and trusted his family.",
                "",
                "That trust became his greatest disguise."
            ]
        ),
        (
            "THE TATTLETALE",
            [
                "For years, Owen staged each crime scene",
                "to tell a false story.",
                "",
                "Every scene shifted suspicion away from him",
                "and back onto the victim.",
                "",
                "There were no fingerprints.",
                "No DNA.",
                "No witnesses.",
                "",
                "The media eventually gave the unknown killer",
                "the name that haunted Mareshell for years.",
                "",
                "The Tattletale."
            ]
        ),
        (
            "THE BREAKTHROUGH",
            [
                'The premiere of "Staring U."',
                "gave Owen the perfect chance to return.",
                "",
                "It also became the night his story collapsed.",
                "",
                "Engraved Cufflink",
                "Torn Mask Strap",
                "Bloodstained Movie Ticket",
                "",
                "Together, the evidence exposed",
                "the man behind The Tattletale."
            ]
        ),
        (
            "CASE CLOSED",
            [
                "Owen Mills has been identified",
                "as The Tattletale.",
                "",
                "Recovered evidence has been secured.",
                "",
                "The investigation is officially closed.",
                "",
                "For five years, The Tattletale controlled the story.",
                "",
                "You were the first person to uncover the truth."
            ]
        )
    ]

    for title, lines in pages:
        big_space()
        print_centered(title)
        print()
        print_lines(lines)
        print()
        pause_game()


def build_rooms():
    # North points toward the front entrance.
    # South points deeper into the theater.
    # Lists are used when more than one door is in the same direction.
    rooms = {
        "Lobby": {
            "North": [],
            "South": ["Hallway"],
            "East": ["Concession Stand"],
            "West": ["Arcade"],
            "item": "",
            "collectible": "",
            "description": [
                "The front entrance is locked for the night.",
                "Employees hurry guests toward the rear exits.",
                "The lobby no longer feels safe."
            ]
        },

        "Arcade": {
            "North": [],
            "South": [],
            "East": ["Lobby"],
            "West": [],
            "item": "Flashlight",
            "collectible": "",
            "description": [
                "Arcade cabinets flash against the dark walls.",
                "One machine keeps playing with nobody near it."
            ]
        },

        "Concession Stand": {
            "North": [],
            "South": ["Storage Room", "Employee Room"],
            "South doors": {"storage room": "Storage Room", "storage": "Storage Room", "labeled": "Storage Room", "unlabeled": "Employee Room", "unlabeled door": "Employee Room", "employee room": "Employee Room", "employee": "Employee Room"},
            "East": [],
            "West": ["Lobby"],
            "item": "Walkie-Talkie",
            "collectible": "",
            "description": [
                "The popcorn machines have gone quiet.",
                "Two staff doors sit behind the counter.",
                "One says STORAGE ROOM. The other has no label."
            ]
        },

        "Storage Room": {
            "North": ["Concession Stand"],
            "South": [],
            "East": [],
            "West": [],
            "item": "First Aid Kit",
            "collectible": "",
            "description": [
                "Boxes and cleaning supplies crowd the shelves.",
                "The room smells like bleach and dust."
            ]
        },

        "Employee Room": {
            "North": ["Concession Stand"],
            "South": [],
            "East": [],
            "West": ["Hallway"],
            "item": "Master Keys",
            "collectible": "",
            "description": [
                "Half-open lockers line the walls.",
                "Someone left in enough of a hurry",
                "that the room was never secured."
            ]
        },

        "Hallway": {
            "North": ["Lobby"],
            "South": ["Theater 1", "Theater 2", "Theater 3", "Bathroom"],
            "South doors": {"1": "Theater 1", "theater 1": "Theater 1", "2": "Theater 2", "theater 2": "Theater 2", "3": "Theater 3", "theater 3": "Theater 3", "bathroom": "Bathroom", "restroom": "Bathroom"},
            "East": ["Employee Room"],
            "West": [],
            "item": "",
            "collectible": "Engraved Cufflink",
            "description": [
                "The hallway stretches across the theater wing.",
                "Several doors line the south wall.",
                "The ceiling lights flicker one after another."
            ]
        },

        "Theater 1": {
            "North": ["Hallway"],
            "South": ["Projection Room"],
            "East": [],
            "West": [],
            "item": "",
            "collectible": "Torn Mask Strap",
            "description": [
                "This is one of the theater's older auditoriums.",
                "The movie has stopped, but the projector",
                "still paints a pale rectangle across the screen."
            ]
        },

        "Theater 2": {
            "North": ["Hallway"],
            "South": [],
            "East": [],
            "West": [],
            "item": "",
            "collectible": "Bloodstained Movie Ticket",
            "description": [
                "Forgotten drinks remain in the cup holders.",
                "A shadow crosses the screen and disappears."
            ]
        },

        "Theater 3": {
            "North": ["Hallway"],
            "South": ["Emergency Exit"],
            "East": [],
            "West": [],
            "item": "",
            "collectible": "",
            "description": [
                "The auditorium is empty.",
                "A trailer starts playing even though",
                "the system should already be shut down."
            ]
        },

        "Bathroom": {
            "North": ["Hallway"],
            "South": [],
            "East": [],
            "West": [],
            "item": "Employee ID Badge",
            "collectible": "",
            "description": [
                "The restroom area is almost empty.",
                "Near the family restroom is the employee restroom.",
                "You remember leaving your badge near the sink."
            ]
        },

        "Projection Room": {
            "North": ["Theater 1"],
            "South": [],
            "East": [],
            "West": [],
            "item": "Emergency Evacuation Plan",
            "collectible": "",
            "description": [
                "The projectors hum above Theater 1.",
                "Film light cuts through the dusty room."
            ]
        },

        "Emergency Exit": {
            "North": ["Theater 3"],
            "South": [],
            "East": [],
            "West": [],
            "item": "",
            "collectible": "",
            "description": [
                "The rear exit waits at the end of the aisle.",
                "Police sirens are finally getting closer."
            ]
        }
    }

    return rooms


def show_room(current_room, rooms, visited_rooms, searched_rooms):
    room_space()
    print_centered(current_room.upper())
    print()

    # Full room descriptions only appear the first time through.
    if current_room not in visited_rooms:
        print_lines(rooms[current_room]["description"])
        visited_rooms.append(current_room)

    if rooms[current_room]["item"] != "":
        print()
        print_centered("You notice '" + rooms[current_room]["item"] + "'.")

    if current_room in searched_rooms and rooms[current_room]["collectible"] != "":
        print()
        print_centered("Your search uncovered '" + rooms[current_room]["collectible"] + "'.")

    print()


def show_inventory(inventory, score):
    print()
    print_centered("INVENTORY")
    print()

    if len(inventory) == 0:
        print_centered("Nothing collected yet.")
    else:
        for item in inventory:
            print_centered("'" + item + "'")

    print()
    print_centered("Score: " + str(score))
    print()


def show_help(inventory):
    print()
    print_centered("GAME COMMANDS")
    print()
    print_centered("go North     go South     go East     go West")
    print_centered('search')
    print_centered('grab + exact item name')
    print_centered('inventory')
    print_centered('help')

    if "Emergency Evacuation Plan" in inventory:
        print_centered('read plan')

    print_centered('exit')
    print()
    print_centered('Example: grab Flashlight')
    print()


def choose_door(current_room, direction, choices, rooms):
    # Some parts of the theater have more than one door in the same direction.
    # The dictionary stores those choices so movement still uses one system.
    print()

    if current_room == "Concession Stand":
        print_centered("Two doors are ahead.")
        print()
        print_centered("'Storage Room'")
        print_centered("'Unlabeled Door'")
    elif current_room == "Hallway":
        print_centered("Several doors are ahead.")
        print()
        for room_name in choices:
            print_centered("'" + room_name + "'")
    else:
        print_centered("More than one door is ahead.")
        print()
        for room_name in choices:
            print_centered("'" + room_name + "'")

    print()
    door_key = direction + " doors"
    door_choices = rooms[current_room][door_key]

    while True:
        choice = centered_input("Enter a door: ").lower()

        if choice == "exit":
            return "EXIT"

        if choice in door_choices:
            return door_choices[choice]

        print()
        print_centered("That door is not available here.")
        print()


def show_tattletale_sighting():
    print("\n" * 2)
    print_centered("A figure stands near the screen.")
    print()
    print_centered("The mask is wrong.")
    print()
    print_centered("It isn't the one from the movie.")
    print()
    print_centered("He turns toward you.")


def show_employee_room_failure():
    room_space()
    print_centered("The unlabeled door clicks shut behind you.")
    print()
    print_centered("A badge reader flashes red.")
    print()
    print_centered("You reach for your Employee ID Badge.")
    print_centered("It isn't there.")
    print()
    print_centered("Footsteps stop on the other side of the door.")


def show_projection_room_failure():
    room_space()
    print_centered("The Projection Room door is locked.")
    print()
    print_centered("You pull at the handle again.")
    print()
    print_centered("It won't move.")
    print()
    print_centered("Someone is standing behind you.")


def show_emergency_exit_failure():
    room_space()
    print_centered("You push toward the Emergency Exit.")
    print()
    print_centered("Cold air slips through the edge of the door.")
    print_centered("You're almost outside.")
    print()
    print_centered("A hand closes around your shoulder.")


def has_required_items(inventory, required_items):
    for item in required_items:
        if item not in inventory:
            return False
    return True


def count_hidden_items(inventory, hidden_items):
    count = 0

    for item in hidden_items:
        if item in inventory:
            count += 1

    return count


def show_rating(stars, title):
    big_space()
    print_centered("FINAL RATING")
    print()
    print_centered(stars + "  " + title)
    print()

    if stars == "★★★★★":
        print_lines([
            "You escaped with every required item",
            "and uncovered every hidden collectible.",
            "",
            "Police flood the rear of the building.",
            "The Tattletale is finally taken into custody.",
            "",
            "The crowd has only one thing to say...",
            "",
            "Encore!",
            "",
            "Encore!",
            "",
            "LORE UNLOCKED",
            "",
            "The classified case file",
            "is now available from the main menu."
        ])

    elif stars == "★★★★☆":
        print_lines([
            "You escaped with every required item.",
            "",
            "Some evidence was left behind.",
            "",
            "The critics loved your performance...",
            "the audience wasn't sold on the ending.",
            "",
            "BREAKING NEWS",
            "",
            "The Tattletale vanished before",
            "police could identify him.",
            "",
            "Authorities have no leads."
        ])

    elif stars == "★★★☆☆":
        print_lines([
            "You escaped...",
            "",
            "But most of the evidence stayed hidden.",
            "",
            "BREAKING NEWS",
            "",
            "Police have closed their investigation",
            "into the theater incident.",
            "",
            "No suspect has been identified."
        ])

    elif stars == "★★☆☆☆":
        print_lines([
            "This wasn't in the script.",
            "",
            "Maybe improv isn't your thing.",
            "",
            "BREAKING NEWS",
            "",
            "Police responded to reports of a disturbance",
            "inside the Mareshell theater.",
            "",
            "No further information has been released."
        ])

    elif stars == "★☆☆☆☆":
        print_lines([
            "That's a wrap.",
            "",
            "Unfortunately...",
            "not the one you were hoping for.",
            "",
            "BREAKING NEWS",
            "",
            "A local theater employee was found dead",
            'following the premiere of "Staring U."',
            "",
            "Authorities have not ruled out suicide.",
            "The investigation remains ongoing."
        ])


def show_emergency_plan():
    # The plan gives the player a simple reminder of where the rear exit is.
    room_space()
    print_centered("EMERGENCY EVACUATION PLAN")
    print()
    print_lines([
        "Rear Emergency Exit:",
        "Theater 3",
        "",
        "Once inside Theater 3,",
        "use the door on the SOUTH side",
        "to reach the Emergency Exit."
    ])
    print()


def show_early_exit():
    big_space()
    print_centered("ENCORE")
    print()
    print_centered("See you next shift.")
    print()
    print_centered("Thanks for playing.")


def move_player(current_room, direction, rooms, inventory):
    # Returns the next room, or special words for game-ending situations.
    choices = rooms[current_room][direction]

    if len(choices) == 0:
        print()
        print_centered("There isn't a door in that direction.")
        return current_room

    if len(choices) == 1:
        next_room = choices[0]
    else:
        next_room = choose_door(current_room, direction, choices, rooms)

    if next_room == "EXIT":
        return "EXIT"

    if next_room == "Employee Room" and "Employee ID Badge" not in inventory:
        show_employee_room_failure()
        return "EMPLOYEE FAILURE"

    if next_room == "Projection Room" and "Master Keys" not in inventory:
        show_projection_room_failure()
        return "PROJECTION FAILURE"

    return next_room



def show_arcade_injury():
    # This scene gives the Flashlight a story consequence.
    print()
    print_centered("You pull the Flashlight free.")
    print()
    print_centered("CLANG.")
    print()
    print_centered("Something crashes behind you.")
    print_centered("You turn too quickly and catch your shoulder")
    print_centered("on the broken edge of an arcade cabinet.")
    print()
    print_centered("Pain shoots down your arm.")
    print_centered("When you touch your shoulder, your hand comes back bloody.")
    print()
    print_centered("Whatever made the noise is gone.")



def show_jimbo_injury_hint(player_name, inventory):
    # This works whether the player gets hurt before or after finding the radio.
    print()
    print_centered("The Walkie-Talkie crackles.")
    print()
    print_centered("JIMBO: " + player_name + "? You still with me?")
    print_centered(player_name.upper() + ": Yeah. I cut my shoulder in the Arcade.")
    print_centered(player_name.upper() + ": I don't remember where the first aid kit is.")
    print()
    print_centered("JIMBO: Storage Room. Behind concession.")
    print_centered("JIMBO: Get that shoulder wrapped.")
    print()

    if "Employee ID Badge" not in inventory:
        print_centered("JIMBO: And your badge is still in the employee restroom.")
        print_centered("JIMBO: You left it by the sink.")
        print()


def show_vicky_first_aid_scene(player_name, inventory):
    # The Walkie-Talkie changes how the player gets help with the injury.
    print()
    print_centered("You open the First Aid Kit.")
    print_centered("The cut is deeper than you thought.")
    print()
    print_centered("Maybe I should ask someone for help with this.")
    print()

    if "Walkie-Talkie" in inventory:
        print_centered("You raise the Walkie-Talkie.")
        print()
        print_centered(player_name.upper() + ": Jimbo, I found the first aid kit.")
        print_centered("JIMBO: Good. I'm still helping a kid in the bathroom.")
        print_centered("JIMBO: I'll send Vicky to you.")
        print()
        print_centered("A moment later, footsteps hurry toward the room.")
        print()
        print_centered("VICKY: " + player_name + "?")
        print_centered(player_name.upper() + ": In here.")
        print()
        print_centered("Vicky looks at your shoulder and opens the kit.")
        print()
        print_centered("VICKY: Sit down. Let me see.")
        print_centered("VICKY: This is going to sting.")
        print()
        print_centered("She cleans the cut and starts wrapping your shoulder.")
        print()
        print_centered("Vicky is quieter than usual.")
        print_centered("You notice the worried look on her face.")
        print()
        print_centered(player_name.upper() + ": You okay?")
        print_centered("VICKY: I'm trying to be.")
        print()
        print_centered("VICKY: I can't stop thinking about Zack.")
        print_centered("VICKY: They said he still had a pulse when we found him.")
        print_centered("VICKY: He's seventeen, " + player_name + ".")
        print_centered("VICKY: He was just talking about graduation the other day.")
        print()
        print_centered(player_name.upper() + ": I hope he makes it.")
        print_centered("VICKY: Me too.")
        print()
        print_centered("Vicky secures the bandage.")
        print()
        print_centered("VICKY: There. That should hold.")
        print()

        if "Emergency Evacuation Plan" not in inventory:
            print_centered("VICKY: I think the evacuation plan is in the Projection Room.")
            print_centered("VICKY: Might be worth grabbing.")
            print()

        if "Employee ID Badge" not in inventory:
            print_centered("VICKY: Jimbo said your badge is still")
            print_centered("by the sink in the employee restroom.")
            print()

        encouragement = centered_input("Say something encouraging to Vicky: ").strip()

        if encouragement != "":
            print()
            print_centered(player_name.upper() + ": " + encouragement)
            print()
            print_centered("VICKY: Thanks. I needed that.")
        else:
            print()
            print_centered("VICKY: Thanks for checking on me.")

        print_centered("VICKY: Be careful out there.")
        return True

    print_centered("You pull out your phone.")
    print()
    print_centered("The screen stays black.")
    print_centered("Dead.")
    print()
    print_centered("Looks like you're doing this yourself.")
    print()
    print_centered("You clean the cut and wrap your shoulder")
    print_centered("as tightly as you can.")
    print_centered("It will have to hold.")
    return False


def show_blackout_scene(inventory):
    print()
    print_centered("The projector dies.")
    print()
    print_centered("Then the hallway lights.")
    print()
    print_centered("Then everything.")
    print()
    print_centered("The theater falls quiet.")
    print()
    print_centered("Emergency lights flicker on.")
    print_centered("Guests line the hallway walls while employees")
    print_centered("try to keep everyone calm.")
    print()
    print_centered("CUSTOMER: Why aren't we moving?")
    print_centered("CUSTOMER: What's happening?")
    print()
    print_centered("JIMBO: Stay against the wall. We're getting everyone out.")
    print()

    if "Flashlight" in inventory:
        print_centered("You switch on your 'Flashlight'.")
        print_centered("A clean beam cuts through the darkness.")
        return True

    print_centered("You reach for a light that isn't there.")
    print()
    print_centered("The emergency lights barely reach the theater doors.")
    print_centered("Moving deeper into the building like this is too dangerous.")
    return False


def show_missing_exit_items(inventory, player_injured):
    print()
    print_centered("You reach the Emergency Exit.")
    print()

    if "Master Keys" not in inventory:
        print_centered("The final lock will not release.")
        print_centered("You need the 'Master Keys'.")
        return

    if "Emergency Evacuation Plan" not in inventory:
        print_centered("You found the rear exit, but you are not ready")
        print_centered("to move everyone through it yet.")
        return

    if "Flashlight" not in inventory:
        print_centered("The hallway behind you is almost completely dark.")
        print_centered("You still need a reliable light.")
        return

    if "Walkie-Talkie" not in inventory:
        print_centered("You have no way to coordinate with the other employees.")
        return

    if player_injured and "First Aid Kit" not in inventory:
        print_centered("Your untreated shoulder is still bleeding.")
        print_centered("You cannot keep going like this.")
        return

    print_centered("You are still missing something you need.")



def run_game():
    rooms = build_rooms()

    required_items = [
        "Flashlight",
        "Walkie-Talkie",
        "Employee ID Badge",
        "Master Keys",
        "First Aid Kit",
        "Emergency Evacuation Plan"
    ]

    hidden_items = [
        "Engraved Cufflink",
        "Torn Mask Strap",
        "Bloodstained Movie Ticket"
    ]

    current_room = "Lobby"
    inventory = []
    visited_rooms = []
    searched_rooms = []
    theater_one_seen = False
    player_injured = False
    shoulder_treated = False
    vicky_helped = False
    jimbo_injury_talk = False
    score = 0

    big_space()
    print_centered("EMPLOYEE SIGN-IN")
    print()
    player_name = centered_input("First name: ").strip()

    if player_name == "":
        player_name = "Employee"

    print()
    print_centered("Welcome back, " + player_name + ".")
    print()

    if not show_instructions():
        return "exit"

    show_room(current_room, rooms, visited_rooms, searched_rooms)

    while True:
        command = centered_input("Enter your command: ")
        command_lower = command.lower()

        if command_lower == "exit":
            return "exit"

        elif command_lower == "search":
            hidden_item = rooms[current_room]["collectible"]

            if hidden_item == "":
                print()
                print_centered("You search the room.")
                print_centered("Nothing useful is hidden here.")

            elif current_room in searched_rooms:
                print()
                print_centered("You already searched this room.")

            else:
                searched_rooms.append(current_room)
                print()
                print_centered("You carefully search the room.")
                print()
                print_centered("You uncovered '" + hidden_item + "'.")

        elif command_lower.startswith("go "):
            direction = command[3:].strip().title()

            if direction != "North" and direction != "South" and direction != "East" and direction != "West":
                print()
                print_centered("That is not a valid direction.")
                continue

            result = move_player(current_room, direction, rooms, inventory)

            if result == "EXIT":
                return "exit"

            elif result == "EMPLOYEE FAILURE" or result == "PROJECTION FAILURE":
                show_rating("★★☆☆☆", "Lost the Plot")
                return "two"

            elif result == current_room:
                continue

            current_room = result

            if current_room == "Theater 1" and theater_one_seen == False:
                theater_one_seen = True
                show_tattletale_sighting()
                flashlight_ready = show_blackout_scene(inventory)

                if not flashlight_ready:
                    print()
                    print_centered("You back into the Hallway until you can see again.")
                    current_room = "Hallway"

            if current_room == "Emergency Exit":
                if not has_required_items(inventory, required_items):
                    show_missing_exit_items(inventory, player_injured)
                    print()
                    print_centered("You step back into Theater 3.")
                    current_room = "Theater 3"
                    show_room(current_room, rooms, visited_rooms, searched_rooms)
                    continue

                score += 10

                if player_injured:
                    print()
                    if vicky_helped:
                        print_centered("The Tattletale grabs your bandaged shoulder.")
                        print_centered("Pain shoots through your arm, but Vicky's wrap holds.")
                    elif shoulder_treated:
                        print_centered("The Tattletale grabs your injured shoulder.")
                        print_centered("Your rushed bandage pulls loose, but you keep moving.")
                    else:
                        print_centered("The Tattletale grabs your injured shoulder.")
                        print_centered("The untreated cut tears open again.")

                print()
                print_centered("You force the lock with the 'Master Keys'.")
                print_centered("The rear door opens.")
                print_centered("Sirens fill the parking lot.")

                hidden_count = count_hidden_items(inventory, hidden_items)

                if hidden_count == 3:
                    show_rating("★★★★★", "Standing Ovation")
                    return "five"
                elif hidden_count == 2:
                    show_rating("★★★★☆", "Critics' Choice")
                    return "four"
                else:
                    show_rating("★★★☆☆", "Straight to Streaming")
                    return "three"

            show_room(current_room, rooms, visited_rooms, searched_rooms)

        elif command_lower == "inventory":
            show_inventory(inventory, score)

        elif command_lower == "help":
            show_help(inventory)

        elif command_lower == "read plan" or command_lower == "read emergency evacuation plan":
            if "Emergency Evacuation Plan" in inventory:
                show_emergency_plan()
            else:
                print()
                print_centered("You do not have the Emergency Evacuation Plan yet.")

        elif command_lower.startswith("grab "):
            requested_item = command[5:].strip()
            room_item = rooms[current_room]["item"]
            hidden_item = rooms[current_room]["collectible"]

            if requested_item == "":
                print()
                print_centered('Type "grab" followed by the exact item name.')
                print_centered('Example: grab Flashlight')

            elif room_item != "" and requested_item.lower() == room_item.lower():
                inventory.append(room_item)
                score += 10
                rooms[current_room]["item"] = ""

                print()
                print_centered("'" + room_item + "' added to your inventory.")
                print_centered("+10 points")

                if room_item == "Flashlight" and player_injured == False:
                    player_injured = True
                    show_arcade_injury()

                    if "Walkie-Talkie" in inventory and jimbo_injury_talk == False:
                        show_jimbo_injury_hint(player_name, inventory)
                        jimbo_injury_talk = True

                    if "First Aid Kit" in inventory and shoulder_treated == False:
                        vicky_helped = show_vicky_first_aid_scene(player_name, inventory)
                        shoulder_treated = True

                elif room_item == "First Aid Kit" and player_injured:
                    vicky_helped = show_vicky_first_aid_scene(player_name, inventory)
                    shoulder_treated = True

                elif room_item == "Master Keys":
                    print()
                    print_centered("These should open the theater's secured locks.")

                elif room_item == "Employee ID Badge":
                    print()
                    print_centered("You can access the employee-only rooms again.")

                elif room_item == "Walkie-Talkie":
                    print()
                    print_centered("The radio crackles to life.")
                    print_centered("JIMBO: " + player_name + "? If you can hear me, keep this channel open.")

                    if player_injured and jimbo_injury_talk == False:
                        show_jimbo_injury_hint(player_name, inventory)
                        jimbo_injury_talk = True

                elif room_item == "Emergency Evacuation Plan":
                    print()
                    print_centered('(Type "read plan" at any time to review the evacuation route.)')


            elif hidden_item != "" and current_room in searched_rooms and requested_item.lower() == hidden_item.lower():
                inventory.append(hidden_item)
                score += 10
                rooms[current_room]["collectible"] = ""

                print()
                print_centered("'" + hidden_item + "' added to your inventory.")
                print_centered("+10 points")

            elif room_item == "" and hidden_item == "":
                print()
                print_centered("There is nothing to collect in this room.")

            else:
                print()
                print_centered("That item is not available in this room.")

        elif command_lower == "go":
            print()
            print_centered('Type "go" followed by North, South, East, or West.')

        elif command_lower == "grab":
            print()
            print_centered('Type "grab" followed by the exact item name.')
            print_centered('Example: grab Flashlight')

        else:
            print()
            print_centered("That command is not recognized.")
            print()
            print_centered('Type "help" to review the available commands.')

        print()


def show_post_game_menu(lore_unlocked):
    print()
    print_centered("WHAT WOULD YOU LIKE TO DO?")
    print()
    print_centered("Play Again")

    if lore_unlocked:
        print_centered("Lore")

    print_centered("Return")
    print_centered("Exit")
    print()

    while True:
        choice = centered_input("Enter your selection: ").lower()

        if choice == "play again" or choice == "return" or choice == "exit":
            return choice

        if lore_unlocked and choice == "lore":
            return choice

        print()
        print_centered('Type "play again," "return," or "exit."')

        if lore_unlocked:
            print_centered('You may also type "lore."')


def main():
    lore_unlocked = False
    program_running = True

    while program_running:
        menu_choice = show_main_menu(lore_unlocked)

        if menu_choice == "exit":
            show_early_exit()
            program_running = False

        elif menu_choice == "lore":
            if lore_unlocked:
                show_lore()
            else:
                show_lore_locked()

        elif menu_choice == "play":
            playing = True

            while playing:
                ending = run_game()

                if ending == "exit":
                    show_early_exit()
                    program_running = False
                    playing = False

                else:
                    if ending == "five":
                        lore_unlocked = True

                    post_choice = show_post_game_menu(lore_unlocked)

                    if post_choice == "play again":
                        playing = True

                    elif post_choice == "lore":
                        show_lore()
                        playing = False

                    elif post_choice == "return":
                        playing = False

                    elif post_choice == "exit":
                        show_early_exit()
                        program_running = False
                        playing = False

    pause_game("Press Enter to exit...")


if __name__ == "__main__":
    main()
