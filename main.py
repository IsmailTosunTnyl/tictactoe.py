import game , GUI
g = game.game()
def gameInput():
    rawinput = input(f"{g.player} enter your cordinat like '0 0' ")
    return [int(rawinput[0]),int(rawinput[2])]


gui = GUI.GUI(g)
gui.startGUI()



