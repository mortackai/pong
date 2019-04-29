# inputs needs to be sanitized
import os

def main_menu():
    print("Select Game Mode")
    print("1) Single Player")
    print("2) Multiplayer")
    print("98) Main Menu")
    print("99) Exit")
    choice = int(input())
    if choice == 1:
        difficulty_menu()
    if choice == 2:
        multiplayer_menu()
    if choice == 98:
        main_menu()
    if choice == 99:
        os._exit(0)
	

# single player - difficulty
def difficulty_menu():
    print("")
    difficulty = int(input("Enter a difficulty 1-9: "))
    done = False
    return difficulty

# multiplayer - mode
def multiplayer_menu():
    print("")
    print("Multiplayer")
    print("")
    print("1) Splitscreen")
    print("2) Host")
    print("3) Join")
    print("98) Main Menu")
    print("99) Exit")
    choice = int(input())
    if choice == 1:
        difficulty_menu()
        multi_local_done = False
    if choice == 2:
        host_menu()
    if choice == 3:
        join_menu()
    if choice == 98:
       main_menu()
    if choice == 99:
        os._exit(0)

# host
def host_menu():
    print("")
    print("Host")
    print("waiting for connection...")

# join
def join_menu():
    print("")
    print("Join")
    print("")
    host_ip = input("Enter host IP address: ")
    print("connecting...")

main_menu()
