import gui_menu as M
import socket
import singleplayer
import splitscreen

host_ip = socket.gethostbyname(socket.gethostname())

m1 = M.menu("Main Menu", "Single Player", "Multi-Player", "blah")
m2 = M.menu("Difficulty", "Normal", "Hard", "null")
m3 = M.menu("Multiplayer", "Splitscreen", "Host", "Join")
m4 = M.menu("Host " + str(host_ip), "", "", "")
m5 = M.menu("Join", "", "", "")

m1.two_option_menu()

if m1.selection == 0:
    m2.two_option_menu()
    p1 = singleplayer.game(1000, 500, M.difficulty)
    p1.run()

if m1.selection == 1:
    m3.three_option_menu()

if m3.selection == 0:
    m2.two_option_menu()
    p2 = splitscreen.game(1000, 500, M.difficulty)
    p2.run()

if m3.selection == 1:
    m4.two_option_menu()

if m3.selection == 2:
    m4.two_option_menu()
    
m5.two_option_menu()


'''main menu
game mode
single player
multi player
'''

'''single player
difficulty
normal
fast
'''

'''multiplayer
splitscreen
host
join
'''

'''Splitscreen
difficulty
normal
fast
'''

'''host
"now hosting"
'''

'''join
"enter IP of host"
"connecting"
'''
