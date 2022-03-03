
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
    
    # create the gems and rocks
    for _ in range(constants.DEFAULT_ARTIFACTS):
        gem_or_rock = random.randint(1, 2)
        if gem_or_rock == 1:
            artifact = Gem()
        elif gem_or_rock == 2:
            artifact = Rock()
        else:
            print("There was an error in finding whether this is a rock or a gem in __main__.py")
        
        artifact.create_random_values()

        if gem_or_rock == 1:
            cast.add_actor("gems", artifact)
        elif gem_or_rock == 2:
            cast.add_actor("rocks", artifact)

    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Game(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
