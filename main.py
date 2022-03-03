
import random

from game.actor import Actor
from game.artifact import Artifact
from game.cast import Cast

from game.gamestart import Game

from game.keyboard_service import KeyboardService
from game.video_service import VideoService

from game.color import Color 
from game.point import Point


FRAME_RATE = 12  
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 15


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("Score")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = 580 #int(MAX_Y / 2)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("robots", player)
    
    # create the Gems
    x = int(MAX_X / 2)
    y = 0
    position = Point(x, y)
    #position = position.scale(CELL_SIZE)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r, g, b)

    gem = Artifact()
    gem.set_text("*")
    gem.set_font_size(FONT_SIZE)
    gem.set_color(color)
    gem.set_position(position)
    cast.add_actor("gems", gem)

    

    # Create Rocks
    list_rocks = []

    for i in range(DEFAULT_ARTIFACTS):
        x = random.randint(0, COLS - 1)   #random.randint(0,MAX_X)     
        y = random.randint(0, ROWS - 1)   #random.randint(0,MAX_Y)    
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        rock = Artifact()
        rock.set_text("@")
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        list_rocks.append(rock)
        rock.set_lists(list_rocks)
        cast.add_actor("rocks", rock)

    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)

    director = Game(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
