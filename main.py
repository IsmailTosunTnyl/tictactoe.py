import game
g = game.game()
def gameInput():
    rawinput = input(f"{g.player} enter your cordinat like '0 0' ")
    return [int(rawinput[0]),int(rawinput[2])]



inputForGame = gameInput()
condition = g.play(inputForGame[0],inputForGame[1])
while condition:
    inputForGame = gameInput()
    condition = g.play(inputForGame[0], inputForGame[1])



