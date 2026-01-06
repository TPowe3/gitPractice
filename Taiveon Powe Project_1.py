# Display Inventory
def inventoryDisplay(inventory):
    print("Inventory: ", end= "")
    for i in inventory:
        print(i, end = ", ")
    print()
# Combat Simulation
def combatSimulation(player_info, guardian_strength):
    turns = 3
    info={"turns": 3, "strength": 5}
    while turns > 0:
         if player_info["strength"] > guardian_strength:
             return True
         else:
             player_info["strength"] += 2
             turns -= 1
             if turns <= 0:
                return False
# Puzzle Answer Checker
def puzzleAnswer(answer, correct):
    if answer == correct and type(answer) == type(correct):
        return True
    else:
        return False
# Display Health
def playerHealth (player_info):
    health = player_info["health"]
    stars = "*" * (health//10)
    print(f"Health: {health} ({stars})")
# Main Function
def main():
    #Starting the Game
    name = input("Please create a username: ")
    name = name.strip().capitalize()
    print(name)
    player_info={}
    player_info["Name"] = name
    player_info["health"] = 100
    player_info["strength"] = 10
    player_info["score"] = 0
    print(type(player_info))
    print(player_info)
    # when naming variables don't start with a number
    # or a hyphen
    inventory=[]
    gems={}
    room_coord=((1,1), (2,1), (3,1), (4,1), (5,1))
    # Room 1: Collecting Items (Lists):
    inventory.append("torch")
    inventory.extend(["map", "rope"])
    inventory_amount=len(inventory)
    print(f"You have: {inventory_amount} items in your inventory.")
    inventoryDisplay(inventory)
    print()
    for coord in room_coord:
        # Room 1
        if coord == (1,1):
            print(f"Hello {name}, welcome to room 1!")
            question=input("Are you ready to enter room 2?(Y/N): ")
            if question.lower() == "y":
                continue
            else:
                break
        # Room 2
        if coord == (2,1):
            puzzle = "Remember 'YOUR' Mother"
            print(f"congrats {name}, welcome to room 2")
            print("In this room you will have to answer a question to a riddle. If you get it right you may pass, otherwise...")
            playerHealth(player_info)
            while True:
                answer=input("Your mother has 4 children, there is North, South, East, what is the name of the last child?: ")
                if puzzleAnswer(answer.strip().capitalize(), name):
                    print("Congragulations on getting the riddle correct. You may proceed")
                    player_info["score"] += 10
                    print(f"Player score = {player_info["score"]}")
                    inventory.insert(1, "Key")
                    print("You've aquired" + " " + "a key!")
                    print("You've awoken the guardian, prepare for a fight!")
                    if "Key" in inventory:
                        action = input("Do you choose to attack or flee?: ").strip().lower()
                        if action == "attack":
                            if player_info["health"] > 50 or player_info["strength"] >= 10:
                                player_info["health"] -= 20
                                player_info["strength"] *= 2
                                removedItem=inventory.pop()
                                print(f"{name}, you attacks are impressive as you lunge forward.")
                                print("You attack fiercely, losing 5 health but doubling your strength as the angels are with you.")
                                print(f"{removedItem} has been removed from players inventory")
                            # Gurdian combat
                            guardian_strength = 15
                            if combatSimulation(player_info, guardian_strength):
                                print("You've defeated the guardian, but a vengeful spirit watches you.")
                            else:
                                print("The guardian is overpowering you.")
                                player_info["health"] -= 20
                                playerHealth(player_info)
                                if player_info["health"] <= 0:
                                    print("You have fallen in battle. Game Over.")
                                    return
                        elif action == "flee":
                            print("You fled the battle safely, but one must wonder what the outcome would be for such a fight.")
                            break
                        else:
                            print("Invalid choice. The guardian strikes you due to your hesitation")
                            player_info["health"] -= 20
                            inventory.pop()
                            playerHealth(player_info)
                    break
                else:
                    print("Your answer is wrong")
                    player_info["health"] -= 10
                    playerHealth(player_info)
                    error=input("Would you like to try again?(Y/N): ")
                    if player_info["health"] <= 0:
                        print(f"{name} has died, Game Over")
                        return
                    if error.strip().lower() == "y":
                        hint=input("Would you like a hint before you try again?(Y/N): ")
                        if hint.strip().lower() == "y":
                            print("\nHere is your clue: ")
                            print("First Letter:", name[0])
                            print("Last letter:", name[-1])
                            print(name[:3])
                            print(puzzle.center(40, "*"))
                            print(puzzle.swapcase())
                            print()
                        continue
                    elif error.strip().lower() == "n":
                        print("You have decided to quit.")
                        return
                    else:
                        print("Please enter Y/N")
                        continue
        # Room 3
        if coord == (3,1):
            print(f"Congragulations {name}, you've entered the third room.")
            print("In this room you will have to solve a math problem to continue")
            while True:
                try:
                    math_problem = int(input("What is 5x2 + (4)^2 ?: "))
                except ValueError:
                    print("Invalid input, your answer will be defaulted to zero.")
                    math_problem=0
                if math_problem == 5*2 + pow(4,2):
                    print("Correct!!!")
                    player_info["score"] += 15
                    print(f"Player total score: {player_info["score"]}")
                    inventory.extend([5, 10])
                    print("You gained 10 bronze and 5 silver coins!")
                    numeric_values = []
                    for item in inventory:
                        if type(item) == int:
                            numeric_values.append(item)
                    if len(numeric_values) > 0:
                        print(f"Sum of numeric items in inventory: {sum(numeric_values)}")
                        print(f"Minimum Numeric value: {min(numeric_values)}")
                        print(f"Maximum numeric value: {max(numeric_values)}")
                    else:
                        print("No numeric items in inventory yet.")
                    print(f"For fun, rounding 3.6 gives: {round(3.6)}")
                    break
                else:
                    print("Incorrect")
                    player_info["health"] -= 10
                    playerHealth(player_info)
                    if player_info["health"] <= 0:
                        print(f"{name} has died, Game Over")
                        return
                    continue
        # Room 4
        if coord == (4,1):
            gemstone=set()
            print(f"Congragulations {name}, you've made it to room 4.")
            gemstone.add("sapphire")
            gemstone.update(["alexandrite", "ruby", "jade"])
            print(f"Gems collected on your travels: {gemstone}")
            requiredGems = {"sapphire", "alexandrite", "ruby"}
            print(f"Gems required: {requiredGems}")
            if requiredGems.issubset(gemstone):
                print("All required gems are present.")
                print(gemstone.difference(requiredGems))
                print("Special gemstone 'jade' is present in inventory.")
                player_info["score"] += 20
            print("Using gemstones to progress to next stage.")
            gemstone.clear()
            print(f"Gemstones: {gemstone}")
        if coord == (5,1):
            code = "GOLD"
            attempts = 3
            print(f"Hello {name}, and welcome to the final room!")
            print("You will have to figure out the answer based on the hint.")
            lastHint="it is a precious metal"
            print(f"The hint is: {lastHint}")
            while attempts > 0:
                letterCode=(input("Enter the 4-letter code: ")).strip().upper()
                letter_list = list(letterCode)
                letter_tuple = tuple(letter_list)
                correct_flag = True
                for i in range(len(letter_tuple)):
                    for j in range(len(code)):
                        if i == j:
                            if letter_tuple[i] != code[i]:
                                correct_flag = False
                                break
                    if not correct_flag:
                        attempts -= 1
                        player_info["health"] -= 10
                        print(f"{name}, you have {attempts} attempts left.")
                        playerHealth(player_info)
                        if attempts <= 0:
                            print("No attempts left. Game Over.")
                            return
                        break
                if correct_flag:
                    if set(letterCode).issubset(set(code)):
                        print("The input is a subset of the code!")
                        print("Correct code!, You passed the final test!")
                        player_info["score"] += 30
                        print("Select one of the three stats: luck, intellect, endurance.")
                        newStat=input("Stat of choice: ").strip().lower()
                        if newStat == "luck":
                            print("You've selected luck as your new stat.")
                            player_info["luck"] = 10
                            print(player_info)
                            del player_info["luck"]
                        elif newStat == "intellect":
                            print("You've selected intellect as your new stat.")
                            player_info["intellect"] = 10
                            print(player_info)
                            del player_info["intellect"]
                        elif newStat == "endurance":
                            print("You've selected endurance as your new stat.")
                            player_info["endurance"] = 10
                            print(player_info)
                            del player_info["endurance"]
                        else:
                            print("Please select one of the stats listed.")
                            continue
                break
            print(f"Congragts {name}, You've beat the game with your score being: {player_info["score"]}.")
            string_items = []
            for item in inventory:
                if type(item) == str:
                    string_items.append(item)
            string_items.sort()
            print("Sorted inventory: ", string_items)
            print("Inventory is now being cleared.")
            inventory.clear()
            print(inventory)
main()