
#from game.artifact import Artifact
class Game:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

        gems = cast.get_first_actor("gems")
        for gem in gems.get_lists():
            max_x = self._video_service.get_width()
            max_y = self._video_service.get_height()
            gem.move_down(max_x, max_y)

        rocks = cast.get_first_actor("rocks")
        for rock in rocks.get_lists():
            max_x = self._video_service.get_width()
            max_y = self._video_service.get_height()
            rock.move_down(max_x, max_y)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        
        score = banner.get_score()
        banner.set_score(score)
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

        for gem in gems:
            if player.get_position().equals(gem.get_position()):
                score += 100
                banner.set_score(score)

        for rock in rocks:
            if player.get_position().equals(rock.get_position()):
                score -= 100
                banner.set_score(score)  

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()