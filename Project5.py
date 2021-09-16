import time, random, os
room_items_dictionary = {"1": "Wedding Ring", "2": "Tylenol", "3": "Haunted Doll", "4": "Cross", "5": "Pacifier"}
inventory_list = []
items_list = ["Wedding Ring", "Tylenol", "Haunted Doll", "Cross", "Pacifier"]

def main():
    choice = play_game()
    while True:
        if choice == "1":
            choice = enter_porch()
        elif choice == "2":
            choice = enter_living_room()
        elif choice == "3":
            choice = enter_bathroom()
        elif choice == "4":
            choice = enter_bedroom()
        elif choice == "5":
            choice = enter_storage_room()
        elif choice == "6":
            choice = enter_prayer_room()
        elif choice == "7":
            choice = enter_baby_room()
        else:
            break
    print("Thanks for playing!\nGoodbye!")

def play_game():
    print("""
    Hi! Welcome to the Amazingly Spooky Haunted House.
    There are 6 rooms in the house and you will be told directions in each one.
    The object of the game is to collect every single item, however there is a slight problem with that.
    There's a chance that even when you search for an item you will be unable to find it, so never give up!
    You can move each direction, North (N) South (S) East (E) or West (W) by typing the corresponding letter.
    Type 'Q' to end the program.
    Type 'S' to start the game!""")
    while True:
        choice = input("\nEnter your choice!\n>> ").upper()
        if choice in ["S", "Q"]:
            break
        else:
            print("Please enter a valid choice: 'S' or 'Q'\n")
    if choice == "S":
        return "1"
    else:
        return "Q"

def print_room_header(room):
    line = '=' * 25
    print(f"\n{line}{room}{line}")

def check_inventory():
    if set(inventory_list) == set(items_list):
        print("\n\nCongratulations! You've found all the items!")
        os._exit(0)

def enter_porch():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Porch")
    print("""
    Your Options:
    Press 'N' to enter the house
    Press 'Q' to quit the game\n""")
    while True:
        choice = input("Enter your choice!\n>> ").upper()
        if choice in ["N", "Q"]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice == "N":
        return "2"
    else:
        return "Q"

def enter_living_room():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Living Room")
    print("""
    Press 'B' to go through the door to the door to the Bathroom
    Press 'E' to go through passageway to the East which leads to the Bedroom
    Press 'U' to go up the stairs to the 2nd floor Storage Room!.\n""")
    while True:
        choice = input("Enter your choice!\n>> ").upper()
        if choice in ["B", "E", "U", "Q"]:
            break
        else:
            print("You can't go that way!\n")
    if choice == "B":
        return "3"
    elif choice == "E":
        return "4"
    elif choice == "U":
        return "5"
    else:
        return "Q"

def enter_bathroom():
    print_room_header("Bathroom")
    print("""
    Press "N" to go North into the Bedroom
    Press "W" to go West into the Living Room
    There's a special item in this room!\n""")
    option = input("Enter T to search for an item or N to not: ")
    if option == 'T':
        if "2" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("2")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["2"]
                check_inventory()
            else:
                print("You didn't find any items!")
        else:
            print("No items in room.")	
    while True:
        choice = input("Enter your choice!\n>> ").upper()
        if choice in ["N", "W", "Q"]:
            break
        else:
            print("You can't go that way!\n")
    if choice == "N":
        return "4"
    elif choice == "W":
        return "2"
    else:
        return "Q"

def enter_bedroom():
    print_room_header("Bedroom")
    print("""
    Press "S" to go South to the Bathroom
    Press "W" to go West into the Living Room
    There is a special item in this room, press T to search for it!\n""")
    option = input("Enter T to search or L to not: ")
    if option == 'T':
        if "1" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("1")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["1"]
                check_inventory()
            else:
                print("You didn't find any items!")
        else:
            print("No items in room.")
    while True:
        choice = input("Enter your choice!\n>> ").upper()
        if choice in ["S", "W", "Q"]:
            break
        else:
            print("You can't go that way!\n")
    if choice == "S":
        return "3"
    if choice == "W":
        return "2"
    else:
        return "Q"

def enter_storage_room():
    print_room_header("Storage Room")
    print("""
    Press "E" to go East into the prayer room
    Press "D" to go back down into the Living Room
    There is a special item in this room!\n""")
    option = input("Enter T to search for an item or N to not: ")
    if option == 'T':
        if "3" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("3")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["3"]
                check_inventory()
            else:
                print("You didn't find any items!")
        else:
            print("No items in room.")	
    while True:
        choice = input("Enter your choice!\n>> ").upper()
        if choice in ["E", "D", "Q"]:
            break
        else:
            print("You can't go that way!\n")
    if choice == "E":
        return "6"
    if choice == "D":
        return "2"
    else:
        return "Q"

def enter_prayer_room():
    print_room_header("Prayer Room")
    print("""
    Press "S" to go to the door to the South into the Baby's Room
    Press "W" to go through the door to the West of you into the Storage Room
    There is a special item in this room!\n""")
    option = input("Enter T to seach for an item or N to not: ")
    if option == 'T':
        if "4" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("4")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["4"]
                check_inventory()
            else:
                print("You didn't find any items!")
        else:
            print("No items in room.")	
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["S", "W", "Q"]:
            break
        else:
            print("You can't go that way!\n")
    if choice == "S":
        return "7"
    elif choice == "W":
        return "5"
    else:
        return "Q"

def enter_baby_room():
    print_room_header("Baby Room")
    print("""
    Press "N" to go back through the door to the North into the prayer room
    There is a special item in this room!\n""")
    option = input("Enter T to search for an item or N to not: ")
    if option == 'T':
        if "5" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("5")
                print(f"You found an {item}")
                inventory_list.append(item)
                del room_items_dictionary["5"]
                check_inventory()
            else:
                print("You didn't find any items!")
        else:
            print("No items in room.")	
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["N", "Q"]:
            break
        else:
            print("You can't go that way!")
    if choice == "N":
        return "6"
    else:
        return "Q"

main()