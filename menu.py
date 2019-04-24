# these inputs needs to be sanitized
import os

def menu():
    game_mode_chosen = 0
    multi_mode_chosen = 0
    print("Select Game Mode")
    print("1) Single Player")
    print("2) Multiplayer")
    print("98) Main Menu")
    print("99) Exit")
    game_mode_chosen = int(input())
    if game_mode_chosen == 98:
        menu()
    if game_mode_chosen == 99:
        os._exit(0)

# single player - difficulty
    if game_mode_chosen == 1:
        print("")
        difficulty = int(input("Enter a difficulty 1-9: "))
        done = False

# multiplayer - mode
    if game_mode_chosen == 2:
        print("")
        print("Multiplayer")
        print("")
        print("1) Splitscreen")
        print("2) Host")
        print("3) Join")
        print("98) Main Menu")
        print("99) Exit")
        multi_mode_chosen = int(input())
        if multi_mode_chosen == 1:
            multi_local_done = False
        if multi_mode_chosen == 98:
            menu()
        if multi_mode_chosen == 99:
            os._exit(0)

# host
    if multi_mode_chosen == 2:
        print("")
        print("Host")
        print("waiting for connection...")

# join
    if multi_mode_chosen == 3:
        print("")
        print("Join")
        print("")
        host_ip = input("Enter host IP address: ")
        print("connecting...")
