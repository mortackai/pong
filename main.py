import singleplayer
import splitscreen
import menu as M

# Run the menu script to get the game mode and ball speed
m1 = M.menu()
m1.main_menu()
print("ball speed chosen is " + str(m1.difficulty))
print("game mode chosen is " + str(m1.game_mode))

# set the classes as shorter addressable variables
p1 = singleplayer.game(1000, 500, m1.difficulty)
p2 = splitscreen.game(1000, 500, m1.difficulty)

# if game mode is 1 run singleplayer
if m1.game_mode == 1:
    p1.run()
if m1.game_mode == 2:
    p2.run()
if m1.game_mode == 3:
    p3.run()
if m1.game_mode == 4:
    p4.run()
