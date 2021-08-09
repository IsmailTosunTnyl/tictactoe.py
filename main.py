import game, GUI



try:

        g = game.game()
        gui = GUI.GUI(g)
        gui.startGUI()

finally:
    print("run")




