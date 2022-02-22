import pygame
from pygame.math import Vector2 as The_Vector


class ThePlayer(pygame.sprite.Sprite):

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self, pac_man, the_grids_position):
        # "'super(Player, self).__init__()' is 'equivalent' to '''base' class,' 'pygame.sprite.Sprite.__init__(self).''"
        # This will use the "'super()' method to call the "__init__()" constructor of "Sprite." "super()" is typically
        # used for the "'inheritance' of 'classes'" in "OOP ('Object-Oriented Programming')." They "'expands' the
        # 'functionality' of an ''inherited' method' or more through 'permissible access' to a ''parent' and or 'sub'
        # class:'"
        super(ThePlayer, self).__init__()

        self.pac_man = pac_man

        # This line of code will be responsible for "'defining' the ''player's circular rect object's' ''grid'
        # position:''"
        self.the_grids_position = the_grids_position

        # This line of code will "allow the 'player's circular rect object' to 'move 'fluidly' instead of in 'intervals''
        # ''on' the 'grid'' by 'moving ''one' pixel at a time:''"
        self.the_pixels_position = \
            The_Vector((self.the_grids_position.x * self.pac_man.the_cells_width) +
                       (self.pac_man.the_screen_perimeters_offset / 2 + self.pac_man.the_cells_width / 1.85),
                       (self.the_grids_position.y * self.pac_man.the_cells_height) +
                       (self.pac_man.the_screen_perimeters_offset / 2.05 + self.pac_man.the_cells_height / 1.85))

        self.the_players_circular_rect_object = None

        # self.the_players_circular_rect_objects_tracker = None

        self.the_players_circular_rect_objects_position = The_Vector(0, 0)

    def draw_the_players_circular_rect_object(self):
        self.the_players_circular_rect_object = \
            pygame.draw.rect(self.pac_man.the_screens_perimeter_window, "Yellow",
                             (self.the_pixels_position.x - self.pac_man.the_cells_width +
                              self.pac_man.the_screen_perimeters_offset / 4.8,
                              self.the_pixels_position.y - self.pac_man.the_cells_height +
                              self.pac_man.the_screen_perimeters_offset / 3.5,
                              self.pac_man.the_cells_width / 1.35, self.pac_man.the_cells_height / 1.6), 0, 10, 10)
        #                                                       OR:
        # self.the_players_circular_rect_object = \
        #     pygame.draw.rect(self.pac_man.the_screens_perimeter_window, "Yellow",
        #                      (self.the_grids_position.x * self.pac_man.the_cells_width +
        #                       self.pac_man.the_screen_perimeters_offset / 1.85,
        #                       self.the_grids_position.y * self.pac_man.the_cells_height +
        #                       self.pac_man.the_screen_perimeters_offset / 1.7,
        #                       self.pac_man.the_cells_width / 1.35, self.pac_man.the_cells_height / 1.6), 0, 10, 10)

        # |**************************************************************************************************************|
        # |       | These blocks can be used to "'create' a 'rect' that will continuously 'track' the ''circular |       |
        # |                                       | rect surface's' 'position:'' |                                       |
        # |**************************************************************************************************************|

        # self.the_players_circular_rect_objects_tracker = \
        #     pygame.draw.rect(self.pac_man.the_screens_perimeter_window, "Red",
        #                      (self.the_pixels_position.x - self.pac_man.the_cells_width +
        #                       self.pac_man.the_screen_perimeters_offset / 4.8,
        #                       self.the_pixels_position.y - self.pac_man.the_cells_height +
        #                       self.pac_man.the_screen_perimeters_offset / 3.5,
        #                       self.pac_man.the_cells_width / 1.35, self.pac_man.the_cells_height / 1.6), 0, 10, 10)
        #                                                      OR:
        # self.the_players_circular_rect_objects_tracker = \
        #     pygame.draw.rect(self.pac_man.the_screens_perimeter_window, "Red",
        #                      (self.the_grids_position.x * self.pac_man.the_cells_width +
        #                       self.pac_man.the_screen_perimeters_offset / 1.85,
        #                       self.the_grids_position.y * self.pac_man.the_cells_height +
        #                       self.pac_man.the_screen_perimeters_offset / 1.7,
        #                       self.pac_man.the_cells_width / 1.35, self.pac_man.the_cells_height / 1.6), 0, 10, 10)

    def move_the_players_circular_rect_objects_position(self, the_players_circular_rect_objects_position):
        self.the_players_circular_rect_objects_position = the_players_circular_rect_objects_position

    def update(self):
        # "'Move' the 'circular surface' 'relative to' the 'pixel's 'x's' and 'y's' positions' ''on' the 'screen:''"
        self.the_pixels_position += self.the_players_circular_rect_objects_position

        # "'Set' the 'grid's 'position'' 'relative to' the 'pixel's 'x's' and 'y's,' respectively:"
        # self.the_grids_position.x, self.the_grids_position.y = \
        #     (self.the_pixels_position.x - 60 + self.pac_man.the_cells_width // 2) // self.pac_man.the_cells_width + 1, \
        #     (self.the_pixels_position.y - 60 + self.pac_man.the_cells_height // 2) // self.pac_man.the_cells_height + 1

        # |**************************************************************************************************************|
        # |    | In the event that the user "'desires' to 'track' the ''circular rect surface's' 'position,'' they  |    |
        # |                                       | 'must' 'enable' this block:" |                                       |
        # |**************************************************************************************************************|

        # "'Set' the 'grid's 'position'' 'relative to' the 'pixel's 'x' and 'y,' respectively:"
        # self.the_grids_position.x, self.the_grids_position.y = \
        #     (self.the_pixels_position.x - 60 + self.pac_man.the_cells_width // 2) // self.pac_man.the_cells_width + 1, \
        #     (self.the_pixels_position.y - 60 + self.pac_man.the_cells_height // 2) // self.pac_man.the_cells_height + 1
