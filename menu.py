# these inputs needs to be sanitized
import os

class menu:

    def __init__(self):
        self.game_mode = 0
        self.difficulty = 1

    def main_menu(self):
        print("Select Game Mode")
        print("1) Single Player")
        print("2) Multiplayer")
        print("98) Main Menu")
        print("99) Exit")
        chosen = int(input())
        if chosen == 1:
            self.difficulty_menu()
            self.game_mode = 1
        if chosen == 2:
            self.multiplayer_menu()
        if chosen == 98:
            menu.main_menu()
        if chosen == 99:
            os._exit(0)

    # single player - difficulty
    def difficulty_menu(self):
        print("")
        self.difficulty = int(input("Enter a difficulty 1-9: "))
        done = False

    # multiplayer - mode
    def multiplayer_menu(self):
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
            self.game_mode = 2
            self.difficulty_menu()
        if multi_mode_chosen == 2:
            self.game_mode = 3
            menu.host()
        if multi_mode_chosen == 3:
            self.game_mode = 4
            self.join()
        if multi_mode_chosen == 98:
            self.main_menu()
        if multi_mode_chosen == 99:
            os._exit(0)

    # host
    def host(self):
        print("")
        print("Host")
        print("waiting for connection...")
        print("press Esc to cancel")

    # join
    def join(self):
        print("")
        print("Join")
        print("")
        host_ip = input("Enter host IP address: ")
        print("connecting...")
