import turtle
import random
import time
import winsound
from walls import Walls
from coin import Coin
from door import Door
from crown import Crown
from enemy import Enemy
from start import StartPlayer
from sartpen import StartPen
from startmissile import StartMissile
from startwalls import StartWalls
from startlife import StartLife

wn = turtle.Screen()
wn.bgcolor("yellowgreen")
wn.title("Harry Potter And The Goblet Of Fire")
wn.setup(800, 800)
wn.tracer(0)

images = [".\\paint\\volan_left_111.gif", ".\\paint\\volan_down_111.gif", ".\\paint\\volan_up_111.gif",
          ".\\paint\\snitch_111.gif",
          ".\\paint\\avadakedavra.gif", ".\\paint\\harry_fire_111.gif", ".\\paint\\volan_right_111.gif",
          ".\\paint\\harry_hat_111.gif",
          ".\\paint\\harry_right111.gif", ".\\paint\\harry_left111.gif", ".\\paint\\landscape (1).gif",
          ".\\paint\\happy_up111.gif", ".\\paint\\happy_down111.gif"]

for image in images:
    turtle.register_shape(image)


Walls.levels.append(Walls.level_1)
Walls.levels.append(Walls.level_2)
Walls.levels.append(Walls.level_3)
Walls.levels.append(Walls.level_4)
Walls.levels.append(Walls.level_5)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                StartPen.pen.goto(screen_x, screen_y)
                StartPen.pen.shape(".\\paint\\landscape (1).gif")
                StartPen.pen.stamp()
                StartWalls.walls.append((screen_x, screen_y))

            if character == "P":
                StartPlayer.player.goto(screen_x, screen_y)

            if character == "C":
                Walls.coins.append(Coin(screen_x, screen_y))

            if character == "E":
                Walls.enemies.append(Enemy(screen_x, screen_y))

            if character == "D":
                Walls.doors.append(Door(screen_x, screen_y))

            if character == "M":
                Walls.crowns.append(Crown(screen_x, screen_y))


setup_maze(Walls.levels[1])
maze = "level1"
turtle.listen()
turtle.onkey(StartPlayer.player.go_left, "Left")
turtle.onkey(StartPlayer.player.go_right, "Right")
turtle.onkey(StartPlayer.player.go_up, "Up")
turtle.onkey(StartPlayer.player.go_down, "Down")
turtle.onkey(StartPlayer.player.headright, "d")
turtle.onkey(StartPlayer.player.headleft, "a")
turtle.onkey(StartPlayer.player.headdown, "s")
turtle.onkey(StartPlayer.player.headup, "w")
turtle.onkey(StartPlayer.player.headright, "D")
turtle.onkey(StartPlayer.player.headleft, "A")
turtle.onkey(StartPlayer.player.headdown, "S")
turtle.onkey(StartPlayer.player.headup, "W")

for enemy in Walls.enemies:
    turtle.ontimer(enemy.move, t=250)

while True:

    StartMissile.missile.move()

    for crown in Walls.crowns:

        if StartPlayer.player.is_collision(crown):
            StartPlayer.player.destroy()
            crown.destroy()
            Walls.crowns.remove(crown)
            Walls.lives = 3
            StartLife.game.win()
            winsound.PlaySound(".\\sound\\victory.wav", 0)

    for enemy in Walls.enemies:
        if StartMissile.missile.is_collision(enemy):
            Enemy.destroy(enemy)
            StartMissile.missile.status = "ready"
            bob = random.randint(20, 50)
            StartLife.game.gold += bob
            StartLife.game.show_gold()
            winsound.PlaySound(".\\sound\\volandeath.wav", winsound.SND_ASYNC)

    for coin in Walls.coins:
        if StartPlayer.player.is_collision(coin):
            StartLife.game.gold += coin.gold
            StartLife.game.show_gold()
            print("Player Gold: {}".format(StartLife.game.gold))
            coin.destroy()
            Walls.coins.remove(coin)
            winsound.PlaySound(".\\sound\\coin.wav", winsound.SND_ASYNC)

    for enemy in Walls.enemies:
        if StartPlayer.player.is_collision(enemy):
            Walls.lives += 1
            StartLife.life.lives -= 1
            winsound.PlaySound(".\\sound\\death.wav", winsound.SND_ASYNC)
            time.sleep(1)
            print("Player dies ")
            StartWalls.walls.clear()
            StartPen.pen.clear()
            for enemy in Walls.enemies:
                Enemy.destroy(enemy)
            for coin in Walls.coins:
                Coin.destroy(coin)
            for door in Walls.doors:
                Door.destroy(door)

            if Walls.lives == 3:
                StartLife.game.dead()
                # xp.lose()
                StartPlayer.player.destroy()
                setup_maze(Walls.levels[1])
                StartLife.life.show_lives()
                break

            StartLife.game.gold = 0
            StartLife.life.show_lives()
            StartLife.game.show_gold()
            setup_maze(Walls.levels[1])
            maze = "level1"
            for enemy in Walls.enemies:
                turtle.ontimer(enemy.move, t=250)

    for door in Walls.doors:
        if StartPlayer.player.is_collision(door):
            StartWalls.walls.clear()
            StartPen.pen.clear()
            for enemy in Walls.enemies:
                Enemy.destroy(enemy)
            for coin in Walls.coins:
                Coin.destroy(coin)
            for door in Walls.doors:
                Door.destroy(door)
            winsound.PlaySound(".\\sound\\unlock.wav", winsound.SND_ASYNC)

            if maze == "level1":

                setup_maze(Walls.levels[2])
                maze = "level2"

            elif maze == "level2":
                setup_maze(Walls.levels[3])
                maze = "level3"

            elif maze == "level3":
                setup_maze(Walls.levels[4])
                maze = "level4"

            elif maze == "level4":
                setup_maze(Walls.levels[5])
            else:
                pass
            for enemy in Walls.enemies:
                turtle.ontimer(enemy.move, t=250)

    wn.update()
