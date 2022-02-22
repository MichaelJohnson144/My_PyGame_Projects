import pygame


class StateMachine:

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self, pac_man):
        self.pac_man = pac_man

        self.the_screens_mid_width, self.the_screens_mid_height = \
            self.pac_man.the_screens_width // 2, self.pac_man.the_screens_height // 2

        self.run_the_display = True

        self.the_cursor_rect = pygame.Rect(0, 0, 20, 20)

    # This method will "'draw' a 'cursor' 'next to' the 'text button displays' '''after' 'calling'' the program's 'pac_man.py'
    # file:'"
    def draw_the_cursor(self):
        self.pac_man.display_the_menus_texts("!", 15, self.the_cursor_rect.x, self.the_cursor_rect.y)

    def blit_the_surface_to_the_screen(self):
        self.pac_man.the_screens_perimeter_window.blit(self.pac_man.the_screens_perimeter_surface, (0, 0))

        # "'Calling' 'flip()' will 'update the 'screen's 'display'' 'with the 'newly drawn surface''' or else 'nothing will
        # change:'"
        pygame.display.flip()

        # "'Reset' the 'keyboard 'flags'' 'at the 'beginning' of 'every frame'' '''after' 'calling'' the program's 'pac_man.py'
        #  file:'"
        self.pac_man.reset_the_pressed_keys()


# "'Inherit' the 'elements of the ''base' class' 'StateMachine:'"
class TheMainMenu(StateMachine):

    # "'Use' the 'previous 'init' function' that was utilized in the 'StateMachine's ''base' class''' and then 'pass' the
    # program's 'pac_man.py' file reference 'as its 'argument:''"
    def __init__(self, pac_man):

        # "'Pass' the program's 'pac_man.py' file reference 'as the '''base' class's' 'argument:'''"
        StateMachine.__init__(self, pac_man)

        # "'Set' the 'new 'cursor's'' ''default' 'starting position'' 'at the 'Start Game' text display:'
        self.the_state = "Start Game"

        # |*********************************************************************************************************************|
        # |                      This block will "'separate' our texts ''20 cm' 'away' from each other:'"                       |
        # |*********************************************************************************************************************|

        self.the_width_of_the_start_game_text_button_display, self.the_height_of_the_start_game_text_button_display = \
            self.the_screens_mid_width, self.the_screens_mid_height - 40

        self.the_width_of_the_options_text_button_display, self.the_height_of_the_options_text_button_display = \
            self.the_screens_mid_width, self.the_screens_mid_height

        self.the_width_of_the_credits_text_button_display, self.the_height_of_the_credits_text_button_display = \
            self.the_screens_mid_width, self.the_screens_mid_height + 40

        self.the_cursor_rect.midtop = \
            (self.the_width_of_the_start_game_text_button_display - 100, self.the_height_of_the_start_game_text_button_display)

    # This method will "'display' all of the '''Start' menu's' text buttons displays:'"
    def the_display_menu(self):

        self.run_the_display = True

        while self.run_the_display:
            # "'Check' 'all' of the 'events' ''in the program's 'events queue:''"
            self.pac_man.check_the_events()

            # "'Check' for ''whenever' the player ''enters' 'an 'input' 'in the 'program's 'events:''''''"
            self.check_the_players_inputs()

            # "'Fill' the 'screen' 'black:'"
            self.pac_man.the_screens_perimeter_surface.fill("Black")

            # "'Create' and then 'display' the ''Pac-Man' text' 'at the ''defined' position' ''on' the 'screen:'''"
            self.pac_man.display_the_start_menu_text(335, 84, (49, 455 // 3.77), 351, 100, (57, 449 // 3.49))

            # "'Create' and then 'display' the 'new 'Start Game' text button' ''on' the 'screen:''"
            self.pac_man.display_the_menus_texts("Start Game", 36,
                                                 self.the_width_of_the_start_game_text_button_display,
                                                 self.the_height_of_the_start_game_text_button_display)

            # "'Create' and then 'display' the 'new 'Options' text button' ''on' the 'screen:''"
            self.pac_man.display_the_menus_texts("Options", 36,
                                                 self.the_width_of_the_options_text_button_display,
                                                 self.the_height_of_the_options_text_button_display)

            # "'Create' and then 'display' the 'new 'Credits' text button' ''on' the 'screen:''"
            self.pac_man.display_the_menus_texts("Credits", 36,
                                                 self.the_width_of_the_credits_text_button_display,
                                                 self.the_height_of_the_credits_text_button_display)

            # "'Create' and then 'display' the 'new 'cursor'' ''on' the 'screen:''"
            self.draw_the_cursor()

            # "'Create' and then 'display' the 'new, ''custom' text'' ''on' the ''Start menu' 'screen:''"
            self.pac_man.display_the_menus_custom_text("pacco", 27, self.the_screens_mid_width,
                                                       self.the_screens_mid_height + 140)

            # "'Create' and then 'display' the 'new, ''custom' images' ''on' the 'screen:''"
            self.pac_man.display_the_custom_images()

            # "''Update' the 'screen' 'with the 'new 'surfaces:'''"
            self.blit_the_surface_to_the_screen()

    # This method will "'allow' the 'cursor' to 'move to the next 'desired 'selectable state'' ''within' the 'Main-Menu:'''"
    def move_the_cursor(self):

        if self.pac_man.THE_DOWN_KEY:

            # "'Set' the cursor '''80 cm' ''away' on the 'right' from'' the 'Options' text button display:'"
            if self.the_state == "Start Game":
                self.the_cursor_rect.midtop = (self.the_width_of_the_options_text_button_display - 80,
                                               self.the_height_of_the_options_text_button_display)
                self.the_state = "Options"

            # "'Set' the cursor '''80 cm' ''away' on the 'right' from'' the 'Credits' text button display:'"
            elif self.the_state == "Options":
                self.the_cursor_rect.midtop = (self.the_width_of_the_credits_text_button_display - 80,
                                               self.the_height_of_the_credits_text_button_display)
                self.the_state = "Credits"

            # "'Set' the cursor '''101 cm' ''away' on the 'right' from'' the 'Start Game' text button display:'"
            elif self.the_state == "Credits":
                self.the_cursor_rect.midtop = (self.the_width_of_the_start_game_text_button_display - 101,
                                               self.the_height_of_the_start_game_text_button_display)
                self.the_state = "Start Game"

        elif self.pac_man.THE_UP_KEY:

            # "'Set' the cursor '''80 cm' ''away' on the 'right' from'' the 'Credits' text button display:'"
            if self.the_state == "Start Game":
                self.the_cursor_rect.midtop = (self.the_width_of_the_credits_text_button_display - 80,
                                               self.the_height_of_the_credits_text_button_display)
                self.the_state = "Credits"

            # "'Set' the cursor '''80 cm' ''away' on the 'right' from'' the 'Options' text button display:'"
            elif self.the_state == "Credits":
                self.the_cursor_rect.midtop = (self.the_width_of_the_options_text_button_display - 80,
                                               self.the_height_of_the_options_text_button_display)
                self.the_state = "Options"

            # "'Set' the cursor '''101 cm' ''away' on the 'right' from'' the 'Start Game' text button display:'"
            elif self.the_state == "Options":
                self.the_cursor_rect.midtop = (self.the_width_of_the_start_game_text_button_display - 101,
                                               self.the_height_of_the_start_game_text_button_display)
                self.the_state = "Start Game"

    # This method will "'check' for the ''player's 'inputs:'' ''within' the 'Main-Menu:'''"
    def check_the_players_inputs(self):

        self.move_the_cursor()

        if self.pac_man.THE_START_KEY:

            # Did the player "'hit' the ''Start Game' text button display?' 'If so,' then ''allow' the player to ''play' the
            # game:'''"
            if self.the_state == "Start Game":
                self.pac_man.the_programs_playing_status = True

            # Did the player "'hit' the ''Options' text button display?' 'If so,' then ''take' the player to the ''options'
            # menu:''"
            elif self.the_state == "Options":
                self.pac_man.the_current_menu = self.pac_man.the_options_menu

            # Did the player "'hit' the ''Credits' text button display?' 'If so,' then ''take' the player to the ''Credits'
            # menu:''"
            elif self.the_state == "Credits":
                self.pac_man.the_current_menu = self.pac_man.the_credits_menu

            self.run_the_display = False


# "'Inherit' the 'elements of the ''base' class' 'StateMachine:'"
class TheOptionsMenu(StateMachine):

    # "'Use' the 'previous 'init' function' that was utilized in the 'StateMachine's ''base' class''' and then 'pass' the
    # program's 'pac_man.py' file reference 'as its 'argument:''"
    def __init__(self, pac_man):

        # "'Pass' the program's 'pac_man.py' file reference 'as the '''base' class's' 'argument:'''"
        StateMachine.__init__(self, pac_man)

        self.the_state = "Volume"

        # |*********************************************************************************************************************|
        # |                      This block will "'separate' our texts ''20 cm' 'away' from each other:'"                       |
        # |*********************************************************************************************************************|

        self.the_width_of_the_volumes_text_button_display, self.the_height_of_the_volumes_text_button_display = \
            self.the_screens_mid_width, self.the_screens_mid_height - 40

        self.the_width_of_the_controls_text_button_display, self.the_height_of_the_controls_text_button_display = \
            self.the_screens_mid_width, self.the_screens_mid_height

        self.the_width_of_the_graphics_text_button_display, self.the_height_of_the_graphics_text_button_display = \
            self.the_screens_mid_width, self.the_screens_mid_height + 40

        self.the_cursor_rect.midtop = \
            (self.the_width_of_the_volumes_text_button_display - 70, self.the_height_of_the_volumes_text_button_display)

    # This method will "'display' all of the '''Options' menu's' text buttons displays:'"
    def the_display_menu(self):

        self.run_the_display = True

        while self.run_the_display:
            # "'Check' 'all' of the 'events' ''in the program's 'events queue:''"
            self.pac_man.check_the_events()

            # "'Check' for ''whenever' the player ''enters' 'an 'input' 'in the 'program's 'events:''''''"
            self.check_the_players_inputs()

            # "'Fill' the 'screen' 'black:'"
            self.pac_man.the_screens_perimeter_surface.fill("Black")

            # "'Create' and then 'display' the ''Options' text' 'at the ''defined' position' ''on' the 'screen:'''"
            self.pac_man.display_the_options_menu_text(335, 84, (49, 455 // 3.77), 351, 100, (57, 449 // 3.49))

            # "'Create' and then 'display' the 'new 'Volume' text button' ''on' the 'screen:''"
            self.pac_man.display_the_menus_texts("Volume", 36,
                                                 self.the_width_of_the_volumes_text_button_display,
                                                 self.the_height_of_the_volumes_text_button_display)

            # "'Create' and then 'display' the 'new 'Controls' text button' ''on' the 'screen:''"
            self.pac_man.display_the_menus_texts("Controls", 36,
                                                 self.the_width_of_the_controls_text_button_display,
                                                 self.the_height_of_the_controls_text_button_display)

            # "'Create' and then 'display' the 'new 'Graphics' text button' ''on' the 'screen:''"
            self.pac_man.display_the_menus_texts("Graphics", 36,
                                                 self.the_width_of_the_graphics_text_button_display,
                                                 self.the_height_of_the_graphics_text_button_display)

            self.draw_the_cursor()

            # "'Create' and then 'display' the 'new, ''custom' text'' ''on' the ''Option' menu' 'screen:''"
            self.pac_man.display_the_menus_custom_text("pacco", 27, self.the_screens_mid_width,
                                                       self.the_screens_mid_height + 140)

            # "'Create' and then 'display' the 'new, ''custom' images' ''on' the 'screen:''"
            self.pac_man.display_the_custom_images()

            # "''Update' the 'screen' 'with the 'new 'surfaces:'''"
            self.blit_the_surface_to_the_screen()

    # This method will "'allow' the 'cursor' to 'move to the next 'desired 'selectable state'' ''within' the ''Options' menu:'''"
    def move_the_cursor(self):

        if self.pac_man.THE_DOWN_KEY:

            # "'Set' the cursor '''90 cm' ''away' on the 'right' from'' the 'Controls' text button display:'"
            if self.the_state == "Volume":
                self.the_cursor_rect.midtop = (self.the_width_of_the_controls_text_button_display - 90,
                                               self.the_height_of_the_controls_text_button_display)
                self.the_state = "Controls"

            # "'Set' the cursor '''90 cm' ''away' on the 'right' from'' the 'Graphics' text button display:'"
            elif self.the_state == "Controls":
                self.the_cursor_rect.midtop = (self.the_width_of_the_graphics_text_button_display - 90,
                                               self.the_height_of_the_graphics_text_button_display)
                self.the_state = "Graphics"

            # "'Set' the cursor '''70 cm' ''away' on the 'right' from'' the 'Volume' text button display:'"
            elif self.the_state == "Graphics":
                self.the_cursor_rect.midtop = (self.the_width_of_the_volumes_text_button_display - 70,
                                               self.the_height_of_the_volumes_text_button_display)
                self.the_state = "Volume"

        elif self.pac_man.THE_UP_KEY:

            # "'Set' the cursor '''90 cm' ''away' on the 'right' from'' the 'Graphics' text button display:'"
            if self.the_state == "Volume":
                self.the_cursor_rect.midtop = (self.the_width_of_the_graphics_text_button_display - 90,
                                               self.the_height_of_the_graphics_text_button_display)
                self.the_state = "Graphics"

            # "'Set' the cursor '''90 cm' ''away' on the 'right' from'' the 'Controls' text button display:'"
            elif self.the_state == "Graphics":
                self.the_cursor_rect.midtop = (self.the_width_of_the_controls_text_button_display - 90,
                                               self.the_height_of_the_controls_text_button_display)
                self.the_state = "Controls"

            # "'Set' the cursor '''70 cm' ''away' on the 'right' from'' the 'Volume' text button display:'"
            elif self.the_state == "Controls":
                self.the_cursor_rect.midtop = (self.the_width_of_the_volumes_text_button_display - 70,
                                               self.the_height_of_the_volumes_text_button_display)
                self.the_state = "Volume"

    # This method will "'check' for the ''player's 'inputs:'' ''within' the ''Options' menu:'''"
    def check_the_players_inputs(self):

        self.move_the_cursor()

        # Did the player "'hit' the ''backspace' key' ''on' their 'keyboard' ''while' they were 'in' the ''Options' menu?''' 'If
        # so,' then ''take' them 'back' ''to' the program's 'main menu:'''"
        if self.pac_man.THE_BACK_KEY:
            self.pac_man.the_current_menu = self.pac_man.the_main_menu
            self.run_the_display = False


# "'Inherit' the 'elements of the ''base' class' 'StateMachine:'"
class TheCreditsMenu(StateMachine):

    # "'Use' the 'previous 'init' function' that was utilized in the 'StateMachine's ''base' class''' and then 'pass' the
    # program's 'pac_man.py' file reference 'as its 'argument:''"
    def __init__(self, pac_man):

        # "'Pass' the program's 'pac_man.py' file reference 'as the '''base' class's' 'argument:'''"
        StateMachine.__init__(self, pac_man)

        # |*********************************************************************************************************************|
        # |          This block will "'separate' our texts ''at' the ''pre-defined' 'cm's''' 'away' from each other:'"          |
        # |*********************************************************************************************************************|

        self.the_width_of_the_made_by_text_display, self.the_height_of_the_made_by_text_display = \
            self.the_screens_mid_width, self.the_screens_mid_height - 40

        self.the_width_of_my_name_text_display, self.the_height_of_my_name_text_display = \
            self.the_screens_mid_width, self.the_screens_mid_height + 5

        self.the_width_of_the_and_inspired_by_text_display, self.the_height_of_the_and_inspired_by_text_display = \
            self.the_screens_mid_width, self.the_screens_mid_height + 50

        self.the_width_of_the_cdcodes_text_display, self.the_height_of_the_cdcodes_text_display = \
            self.the_screens_mid_width, self.the_screens_mid_height + 100

    # This method will "'display' all of the '''Credits' menu's' text buttons displays:'"
    def the_display_menu(self):

        self.run_the_display = True

        while self.run_the_display:

            # "'Check' 'all' of the 'events' ''in the program's 'events queue:''"
            self.pac_man.check_the_events()

            if self.pac_man.THE_BACK_KEY:
                self.pac_man.the_current_menu = self.pac_man.the_main_menu
                self.run_the_display = False

            # "'Fill' the 'screen' 'black:'"
            self.pac_man.the_screens_perimeter_surface.fill("Black")

            # "'Create' and then 'display' the ''Credits' text' 'at the ''defined' position' ''on' the 'screen:'''"
            self.pac_man.display_the_credits_menu_text(335, 84, (49, 455 // 3.77), 351, 100, (57, 449 // 3.49))

            self.pac_man.display_the_menus_texts("Made by", 36,
                                                 self.the_width_of_the_made_by_text_display,
                                                 self.the_height_of_the_made_by_text_display)

            self.pac_man.display_the_custom_credits_text("Michael D Johnson", 27, self.the_width_of_my_name_text_display,
                                                         self.the_height_of_my_name_text_display)
            self.pac_man.display_the_menus_texts("And inspired by", 36,
                                                 self.the_width_of_the_and_inspired_by_text_display,
                                                 self.the_height_of_the_and_inspired_by_text_display)
            self.pac_man.display_the_custom_credits_text("CDcodes", 36, self.the_width_of_the_cdcodes_text_display,
                                                         self.the_height_of_the_cdcodes_text_display)

            # "''Update' the 'screen' 'with the 'new 'surfaces:'''"
            self.blit_the_surface_to_the_screen()
