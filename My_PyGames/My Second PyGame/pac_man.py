from pygame.locals import (KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_RETURN, K_BACKSPACE, K_ESCAPE, QUIT, K_p)
from pac_mans_main_menu_state_machine import *
from the_players_class import *


# def display_the_paused_text_display(self):

#     the_paused_text_display_font = pygame.font.Font('Labraid 8PX.ttf', 36)

#     the_paused_text_display_surface = the_paused_text_display_font.render("Paused", True, "Yellow")

#     the_paused_text_display_surface_rect = \
#         the_paused_text_display_surface.get_rect(center=(self.the_screens_width // 2, self.the_screens_height // 2))

#     self.the_screens_perimeter_surface.blit(the_paused_text_display_surface, the_paused_text_display_surface_rect)


class ItsElements:

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self):

        # |*********************************************************************************************************************|
        # |                           | "INITIALIZE" the Program and "CREATE" Its "DISPLAY WINDOW!" |                           |
        # |*********************************************************************************************************************|

        # Initialize PyGame:
        pygame.init()

        # "'Define' the 'new 'display windows's 'title:''"
        pygame.display.set_caption("Pac-Man")

        # "'Define' the 'new ''screen's' 'perimeters (448x512 pixels):'''"
        self.the_screens_width, self.the_screens_height = 448, 576

        # "'Pre-define' the 'screen perimeter's 'offset'' for planned and future references:"
        self.the_screen_perimeters_offset = 60

        # "'Pre-defined' the 'grid's 'perimeters (19x21 pixels)' for planned and future references:
        self.the_grids_rows, self.the_grids_columns = 19, 21

        # "'Pre-define' the ''grid's' ''cell' 'perimeters:'''"
        self.the_cells_width, self.the_cells_height = \
            (self.the_screens_width - self.the_screen_perimeters_offset) / self.the_grids_rows, \
            (self.the_screens_height - self.the_screen_perimeters_offset) / self.the_grids_columns

        # "'Create' a 'new ''imaged' surface' on the ''screen's' 'window'' ''using' its 'pre-defined' 'perimeters:'''"
        self.the_screens_perimeter_surface = pygame.Surface((self.the_screens_width, self.the_screens_height))

        # "'Create' the 'new ''screen's' 'window'' ''using' its 'pre-defined' 'perimeters:'''"
        self.the_screens_perimeter_window = pygame.display.set_mode(size=(self.the_screens_width, self.the_screens_height))

        # "'Load' the image:"
        self.the_maze_image_surface = pygame.image.load("Maze_Background.png")

        # "'Scale' the image:"
        self.the_maze_image_surface = \
            pygame.transform.scale(self.the_maze_image_surface,
                                   size=(self.the_screens_width - self.the_screen_perimeters_offset,
                                         self.the_screens_height - self.the_screen_perimeters_offset))

        # "'Pre-define' the 'maze background's' 'walls coordinates:''"
        self.the_mazes_walls = []

        # "'Open' 'The_Mazes_Walls.txt' and then 'create' a 'walls list' with its ''inherent' 'pre-defined' 'walls coordinates''
        # ''through' 'enumeration (The 'enumerate()' method ''adds' a 'counter' 'to an 'iterable'' and ''returns' it ''in a form'
        # of an ''enumerating' object,''' which can then be 'used 'directly' for 'loops' or '''converted into' a 'list of
        # 'tuples''' ''using' the 'list()' method''''):'"
        with open("The_Mazes_Walls_Coordinates.txt", 'r') as the_maze_images_surface:
            for the_maze_image_surfaces_y_index, the_maze_image_surfaces_walls_coordinates in enumerate(the_maze_images_surface):
                for the_maze_image_surfaces_x_index, the_characters_type in enumerate(the_maze_image_surfaces_walls_coordinates):
                    if the_characters_type == "1":
                        self.the_mazes_walls.append(The_Vector(the_maze_image_surfaces_x_index, the_maze_image_surfaces_y_index))

        # |*********************************************************************************************************************|
        # |                                      | These Are the Program's "VARIABLES!!" |                                      |
        # |*********************************************************************************************************************|

        # "'Pre-define' the 'conditions' of the program's 'state menu' and 'running' 'controls' so that the player can later
        # '''navigate' 'throughout'' the program's 'main menu:'"
        self.THE_UP_KEY, self.THE_DOWN_KEY, self.THE_LEFT_KEY, self.THE_RIGHT_KEY, self.THE_START_KEY, self.THE_BACK_KEY, \
            self.THE_PAUSE_KEY = False, False, False, False, False, False, False

        # |*********************************************************************************************************************|
        # |                                 "'Pre-define' the program's ''state' conditions!'"                                  |
        # |*********************************************************************************************************************|

        self.the_programs_running_status, self.the_programs_playing_status = True, False

        self.the_main_menu = TheMainMenu(self)

        self.the_options_menu = TheOptionsMenu(self)

        self.the_credits_menu = TheCreditsMenu(self)

        self.the_current_menu = self.the_main_menu

        self.the_players_circular_rect_object = ThePlayer(self, The_Vector(9, 15))

    # |*************************************************************************************************************************|
    # |                             | "DEFINE" the Program's "FONTS," "STYLES," and "BACKGROUND!" |                             |
    # |*************************************************************************************************************************|

    def display_the_start_menu_text(self, x_2, y_2, the_outer_rects_perimeter, x_1, y_1, the_inner_rects_perimeter):

        # "'Create' a 'new ''outer' rectangle:''"
        the_outer_rect = pygame.Rect(the_outer_rects_perimeter, (x_1, y_1))

        # "'Create' a 'new ''inner' rectangle:''"
        the_inner_rect = pygame.Rect(the_inner_rects_perimeter, (x_2, y_2))

        # "Define" the new "text's 'font:'"
        the_pac_man_text_display_font = pygame.font.Font("CrackMan.ttf", 63)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        the_pac_man_text_display_surface = the_pac_man_text_display_font.render("Pac-Man", True, "Black")

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        the_pac_man_text_display_surface_rect = \
            the_pac_man_text_display_surface.get_rect(center=(the_outer_rect.center and the_inner_rect.center))

        # "'Draw' the 'red,' ''outer' 'curved' rectangular surface' ''around' the 'new 'surfaced text:'''"
        pygame.draw.rect(self.the_screens_perimeter_surface, "Red", the_outer_rect, 5, 12)

        # "'Draw' the 'orange,' ''inner' 'curved' rectangular surface' ''within' the ''outer' 'curved' rectangular surface' and
        # ''around' the 'new 'surfaced text:'''"
        pygame.draw.rect(self.the_screens_perimeter_surface, (216, 108, 0), the_inner_rect, 0, 4)

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        self.the_screens_perimeter_surface.blit(the_pac_man_text_display_surface, the_pac_man_text_display_surface_rect)

    def display_the_options_menu_text(self, x_2, y_2, the_outer_rects_perimeter, x_1, y_1, the_inner_rects_perimeter):

        # "'Create' a 'new ''outer' rectangle:''"
        the_outer_rect = pygame.Rect(the_outer_rects_perimeter, (x_1, y_1))

        # "'Create' a 'new ''inner' rectangle:''"
        the_inner_rect = pygame.Rect(the_inner_rects_perimeter, (x_2, y_2))

        # "Define" the new "text's 'font:'"
        the_options_menu_text_display_font = pygame.font.Font("CrackMan.ttf", 63)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        the_options_menu_text_display_surface = the_options_menu_text_display_font.render("Options", True, "Black")

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        the_options_menu_text_display_surface_rect = \
            the_options_menu_text_display_surface.get_rect(center=(the_outer_rect.center and the_inner_rect.center))

        # "'Draw' the 'red,' ''outer' 'curved' rectangular surface' ''around' the 'new 'surfaced text:'''"
        pygame.draw.rect(self.the_screens_perimeter_surface, "Red", the_outer_rect, 5, 12)

        # "'Draw' the 'orange,' ''inner' 'curved' rectangular surface' ''within' the ''outer' 'curved' rectangular surface' and
        # ''around' the 'new 'surfaced text:'''"
        pygame.draw.rect(self.the_screens_perimeter_surface, (216, 108, 0), the_inner_rect, 0, 4)

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        self.the_screens_perimeter_surface.blit(the_options_menu_text_display_surface, the_options_menu_text_display_surface_rect)

    def display_the_credits_menu_text(self, x_2, y_2, the_outer_rects_perimeter, x_1, y_1, the_inner_rects_perimeter):

        # "'Create' a 'new ''outer' rectangle:''"
        the_outer_rect = pygame.Rect(the_outer_rects_perimeter, (x_1, y_1))

        # "'Create' a 'new ''inner' rectangle:''"
        the_inner_rect = pygame.Rect(the_inner_rects_perimeter, (x_2, y_2))

        # "Define" the new "text's 'font:'"
        the_credits_menu_text_display_font = pygame.font.Font("CrackMan.ttf", 63)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        the_credits_menu_text_display_surface = the_credits_menu_text_display_font.render("Credits", True, "Black")

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        the_credits_menu_text_display_surface_rect = \
            the_credits_menu_text_display_surface.get_rect(center=(the_outer_rect.center and the_inner_rect.center))

        # "'Draw' the 'red,' ''outer' 'curved' rectangular surface' ''around' the 'new 'surfaced text:'''"
        pygame.draw.rect(self.the_screens_perimeter_surface, "Red", the_outer_rect, 5, 12)

        # "'Draw' the 'orange,' ''inner' 'curved' rectangular surface' ''within' the ''outer' 'curved' rectangular surface' and
        # ''around' the 'new 'surfaced text:'''"
        pygame.draw.rect(self.the_screens_perimeter_surface, (216, 108, 0), the_inner_rect, 0, 4)

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        self.the_screens_perimeter_surface.blit(the_credits_menu_text_display_surface, the_credits_menu_text_display_surface_rect)

    def display_the_menus_texts(self, the_text, the_size, x, y):

        # "'Pre-define' the program's ''texts' 'font:''"
        the_text_button_display_font = pygame.font.Font("ArcadeClassic.ttf", the_size)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        the_text_button_display_surface = the_text_button_display_font.render(the_text, True, "White")

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        the_text_button_display_surface_rect = the_text_button_display_surface.get_rect(center=(x, y))

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        self.the_screens_perimeter_surface.blit(the_text_button_display_surface, the_text_button_display_surface_rect)

    def display_the_menus_custom_text(self, the_text, the_size, x, y):

        # "Define" the new "text's 'font:'"
        the_custom_text_display_font = pygame.font.Font("Namco Regular.ttf", the_size)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        the_custom_text_display_surface = the_custom_text_display_font.render(the_text, True, "Red")

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        the_custom_text_display_surface_rect = the_custom_text_display_surface.get_rect(center=(x, y))

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        self.the_screens_perimeter_surface.blit(the_custom_text_display_surface, the_custom_text_display_surface_rect)

    def display_the_custom_images(self):

        # the_pac_man_main_menu_logo_image_surface = pygame.image.load("Pac_Man_Main_Menu_Logo.png")

        # the_pac_man_main_menu_logo_image_surface = \
        #    pygame.transform.scale(the_pac_man_main_menu_logo_image_surface, size=(408 // 1, 232 // 1))

        # self.the_screens_perimeter.blit(the_pac_man_main_menu_logo_image_surface, (40, 100))

        # |*********************************************************************************************************************|

        # "'Load' the image:"
        the_ghost_squad_image_surface = pygame.image.load("The_Ghost_Squad.png")

        # "'Scale' the image:"
        the_ghost_squad_image_surface = pygame.transform.scale(the_ghost_squad_image_surface, size=(820 // 4.5, 240 // 4.5))

        # "'Load' the ''image' 'to'' and ''display' it 'on'' the 'screen's ''main menu' surface'' ''at' the 'pre-defined'
        # 'position:''
        self.the_screens_perimeter_surface.blit(the_ghost_squad_image_surface, (265 / 2, 695 / 2))

        # |*********************************************************************************************************************|

        # "'Load' the image:"
        pac_man_left_image_surface = pygame.image.load("Pac_Man_Left.png")

        # "'Scale' the image:"
        pac_man_left_image_surface = pygame.transform.scale(pac_man_left_image_surface, size=(551 // 7, 391 // 7))

        # "'Load' the ''image' 'to'' and ''display' it 'on'' the 'screen's ''main menu' surface'' ''at' the 'pre-defined'
        # 'position:''
        self.the_screens_perimeter_surface.blit(pac_man_left_image_surface, (45, 390))

        # |*********************************************************************************************************************|

        # "'Load' the image:"
        pac_man_left_right_surface = pygame.image.load("Pac_Man_Right.png")

        # "'Scale' the image:"
        pac_man_left_right_surface = pygame.transform.scale(pac_man_left_right_surface, size=(551 // 7, 391 // 7))

        # "'Load' the ''image' 'to'' and ''display' it 'on'' the 'screen's ''main menu' surface'' ''at' the 'pre-defined'
        # 'position:''
        self.the_screens_perimeter_surface.blit(pac_man_left_right_surface, (320, 390))

    def display_the_custom_credits_text(self, the_text, the_size, x, y):

        # "'Pre-define' the program's ''texts' 'font:''"
        the_custom_credits_text_display_font = pygame.font.Font("Labraid 8PX.ttf", the_size)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        the_custom_credits_text_display_surface = the_custom_credits_text_display_font.render(the_text, True, (216, 108, 0))

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        the_custom_credits_text_display_surface_rect = the_custom_credits_text_display_surface.get_rect(center=(x, y))

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        self.the_screens_perimeter_surface.blit(the_custom_credits_text_display_surface, the_custom_credits_text_display_surface_rect)

    def display_the_maze_background(self):

        # "'Load' the ''image' 'to'' and ''display' it 'on'' the 'screen's ''at' the 'pre-defined' 'position:''
        self.the_screens_perimeter_surface.blit(self.the_maze_image_surface, (30, 30))

    def draw_the_screens_grid(self):

        # "'Draw' the ''vertical' 'grid lines:''"
        for x in range(self.the_screens_width // 2):
            pygame.draw.line(self.the_maze_image_surface, "Gray",
                             (x * self.the_cells_width, 0), (x * self.the_cells_width, self.the_screens_height))

        # "'Draw' the ''horizontal' 'grid lines:''"
        for y in range(self.the_screens_height // 2):
            pygame.draw.line(self.the_maze_image_surface, "Gray",
                             (0, y * self.the_cells_height), (self.the_screens_width, y * self.the_cells_height))

    def draw_the_maze_backgrounds_walls_using_the_manual_pre_defined_grid_coordinates(self):

        # "''Manually' draw' the ''maze background's 'walls'' using the ''pre-defined' 'coordinates'' using the 'screen's
        # 'grid:''"
        for the_walls in self.the_mazes_walls:
            pygame.draw.rect(self.the_maze_image_surface, "Purple",
                             (the_walls.x * self.the_cells_width, the_walls.y * self.the_cells_height,
                              self.the_cells_width + 1, self.the_cells_height + 1))

    def display_the_current_score_text(self):

        the_current_score_text_display_font = pygame.font.Font('Labraid 8PX.ttf', 18)

        the_current_score_text_display_surface = the_current_score_text_display_font.render("Score: N/A", True, "Yellow")

        the_current_score_text_display_surface_rect = \
            the_current_score_text_display_surface.get_rect(center=(self.the_screens_width - 355, self.the_screens_height // (73 / 2)))

        self.the_screens_perimeter_surface.blit(the_current_score_text_display_surface, the_current_score_text_display_surface_rect)

    def display_the_high_score_text(self):

        the_high_score_text_display_font = pygame.font.Font('Labraid 8PX.ttf', 18)

        the_high_score_text_display_surface = the_high_score_text_display_font.render("High Score: N/A", True, "Yellow")

        the_high_score_text_display_surface_rect = \
            the_high_score_text_display_surface.get_rect(center=(self.the_screens_width - 120, self.the_screens_height // (73 / 2)))

        self.the_screens_perimeter_surface.blit(the_high_score_text_display_surface, the_high_score_text_display_surface_rect)

    # |*************************************************************************************************************************|
    # |                     | "'LOOK' AT" and "CHECK" the Program's "EVENTS" For the 'Player's 'INPUTS!'" |                     |
    # |*************************************************************************************************************************|

    # This method will "''look' at' and 'Check' ''every' event' ''in' the program's 'queue'' for the 'player's 'inputs:''"
    def check_the_events(self):

        # "''look' at' and 'Check' ''every' event' ''in' the program's 'queue'' for the 'player's 'inputs:''"
        for the_event in pygame.event.get():

            # "'Check' to 'see' 'when the ''post-defined' keyboard buttons (I.e., 'K_RETURN,' 'K_BACKSPACE,' and etc) are
            # ''pressed' and 'released'' 'as 'events''' in the queue:"
            if the_event.type == KEYDOWN:

                # |*************************************************************************************************************|

                #   |*********************************************************************************************************|
                #   |        This "'key event' will 'allow the user to ''enter' the ''various 'state menus'' ''within'        |
                #   |                                      the program's 'main menu'''''"                                     |
                #   |*********************************************************************************************************|

                #  Did the "'player' 'hit' the ''enter' key' on their 'keyboard?'" "If so," then "'set' 'THE_START_KEY' to
                #  'True:'"
                if the_event.key == K_RETURN:
                    self.THE_START_KEY = True

                # |*************************************************************************************************************|

                #  Did the "'player' 'hit' the ''up' key' on their 'keyboard?'" "If so," then "'set' 'THE_UP_KEY' to
                #  'True' and then ''move' the '''circular' surface's' 'position'' 'in the ''upwards' direction:'''"
                if the_event.key == K_UP:
                    self.THE_UP_KEY = True
                    if self.the_programs_playing_status is True:
                        self.the_players_circular_rect_object.move_the_players_circular_rect_objects_position(The_Vector(0, -1))

                #  Did the "'player' 'hit' the ''down' key' on their 'keyboard?'" "If so," then "'set' 'THE_DOWN_KEY' to
                #  'True' and then ''move' the '''circular' surface's' 'position'' 'in the ''downwards' direction:'''"
                if the_event.key == K_DOWN:
                    self.THE_DOWN_KEY = True
                    if self.the_programs_playing_status is True:
                        self.the_players_circular_rect_object.move_the_players_circular_rect_objects_position(The_Vector(0, 1))

                #  Did the "'player' 'hit' the ''left' key' on their 'keyboard?'" "If so," then "'set' 'THE_LEFT_KEY' to
                #  'True' and then ''move' the '''circular' surface's' 'position'' 'in the ''leftwards' direction:'''"
                if the_event.key == K_LEFT:
                    self.THE_LEFT_KEY = True
                    if self.the_programs_playing_status is True:
                        self.the_players_circular_rect_object.move_the_players_circular_rect_objects_position(The_Vector(-1, 0))

                #  Did the "'player' 'hit' the ''right' key' on their 'keyboard?'" "If so," then "'set' 'THE_RIGHT_KEY' to
                #  'True' and then ''move' the '''circular' surface's' 'position'' 'in the ''rightwards' direction:'''"
                if the_event.key == K_RIGHT:
                    self.THE_RIGHT_KEY = True
                    if self.the_programs_playing_status is True:
                        self.the_players_circular_rect_object.move_the_players_circular_rect_objects_position(The_Vector(1, 0))

                # |*************************************************************************************************************|

                #   |*********************************************************************************************************|
                #   |         This "'key event' will 'allow the user to ''pause' the program 'while it's running'''"          |
                #   |*********************************************************************************************************|

                #  Did the "'player' 'hit' the ''P' key' on their 'keyboard?'" "If so," then "'set' 'THE_PAUSE_KEY' to 'True,'
                #  and then 'pause' 'playing' the program by '''freezing' the 'player's ''circular' surface'''' ''at' its 'last
                #  known location''' while it 'continues' 'running:'"
                if the_event.key == K_p:
                    self.THE_PAUSE_KEY = True
                    self.the_players_circular_rect_object.move_the_players_circular_rect_objects_position(The_Vector(0, 0))

                # |*************************************************************************************************************|

                #   |*********************************************************************************************************|
                #   |          This "'key event' will 'allow the user to '''return' to' the program's 'main menu'''"          |
                #   |*********************************************************************************************************|

                #  Did the "'player' 'hit' the ''backspace' key' on their 'keyboard?'" "If so," then "'set' 'THE_BACK_KEY' to
                #  'True,' and then "'stop' 'playing' the program and 'reset' the 'player's 'position'' 'to their 'starting's:''"
                if the_event.key == K_BACKSPACE:
                    self.THE_BACK_KEY = True
                    self.the_programs_playing_status = False
                    self.the_players_circular_rect_object = ThePlayer(self, The_Vector(9, 15))

                # |*************************************************************************************************************|

                # Did the "player" "hit" the "'Escape (ESC)' key on their keyboard?" "If so," then "'terminate' the 'program' by
                # ''setting' 'both' of its 'running' and 'playing' status to 'False:''"
                if the_event.key == K_ESCAPE:
                    self.the_programs_running_status, self.the_programs_playing_status = False, False
                    self.the_current_menu.run_the_display = False

            # Did the "player" "click" the "Window 'exit' button on their keyboard?" "If so," then "'terminate' the 'program' by
            # ''setting' 'both' of its 'running' and 'playing' status to 'False:''"
            elif the_event.type == QUIT:
                self.the_programs_running_status, self.the_programs_playing_status = False, False
                self.the_current_menu.run_the_display = False

    # This method will "'reset' the ''player's 'inputs'' 'in the 'events:''"
    def reset_the_pressed_keys(self):
        self.THE_UP_KEY, self.THE_DOWN_KEY, self.THE_LEFT_KEY, self.THE_RIGHT_KEY, self.THE_START_KEY, self.THE_BACK_KEY, \
            self.THE_PAUSE_KEY = False, False, False, False, False, False, False

    # |*************************************************************************************************************************|
    # |                                  | This Is Our Program's "MAIN 'CONDITIONAL' LOOP!'" |                                  |
    # |*************************************************************************************************************************|

    def the_programs_main_loop(self):

        while self.the_programs_playing_status:
            # "'Check' the ''player's 'inputs'' 'in the 'events:''"
            self.check_the_events()

            # "''Create' a 'new surface'' ''over' the 'screen's perimeter'' and ''fill' it 'Black:''"
            self.the_screens_perimeter_surface.fill("Black")

            # "'Display' the 'game's 'background:''"
            self.display_the_maze_background()

            # "'Display' the 'screen's 'grid:''"
            self.draw_the_screens_grid()

            # "'Display' the ''manually' drawn' ''maze background' image:'"
            self.draw_the_maze_backgrounds_walls_using_the_manual_pre_defined_grid_coordinates()

            # "'Display' the 'player's ''current' score:''"
            self.display_the_current_score_text()

            # "'Display' the 'player's ''high' score:''"
            self.display_the_high_score_text()

            # 'Draw' the 'new 'pre-defined' 'surfaces' of the program '''onto' a 'new canvas'' ''over' its 'initial's:'''
            self.the_screens_perimeter_window.blit(self.the_screens_perimeter_surface, (0, 0))

            # |*********************************************************************************************************************|

            # "'Display' the 'player's ''circular' surface:''
            self.the_players_circular_rect_object.draw_the_players_circular_rect_object()

            self.the_players_circular_rect_object.update()

            # |*********************************************************************************************************************|

            # "'Calling' 'flip()' will 'update the 'screen's 'display'' 'with the 'newly drawn surface''' or else 'nothing will
            # change:'"
            pygame.display.flip()

            self.reset_the_pressed_keys()
