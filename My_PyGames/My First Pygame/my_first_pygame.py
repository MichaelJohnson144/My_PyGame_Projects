# |---------------------------------------------------------------------------------------------------------------------|
# |                                    | This Is a BASIC INTRODUCTORY GAME DESIGN! |                                    |
# |---------------------------------------------------------------------------------------------------------------------|

import random

import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, K_RETURN, QUIT)

# |---------------------------------------------------------------------------------------------------------------------|
# |                           | "INITIALIZE" the Program and "CREATE" Its "DISPLAY WINDOW!" |                           |
# |---------------------------------------------------------------------------------------------------------------------|

# Initialize PyGame:
pygame.init()

pygame.display.set_caption("My First PyGame")

# "'Define' and then 'create' a 'new 'display window'' ''with' the 'given 'perimeters:'''"
Screen = pygame.display.set_mode(size=(800, 600))

# |---------------------------------------------------------------------------------------------------------------------|
# |                           | "LOAD" and Then "SCALE" the Program's "BACKGROUND SURFACE!" |                           |
# |---------------------------------------------------------------------------------------------------------------------|

# "'Create' a 'new ''imaged' surface:''"
The_Background_Surface = pygame.image.load("Troposphere_Bg.png")

# "'Scale' the 'new ''imaged' surface'' 'to' the 'given 'perimeters:''"
The_Background_Surface = pygame.transform.scale(The_Background_Surface, size=(800, 600))


# |---------------------------------------------------------------------------------------------------------------------|
# |                       | "DEFINING" the Program's "ELEMENTS:" "COMPONENTS" and "MECHANICS!!" |                       |
# |---------------------------------------------------------------------------------------------------------------------|

# "'Define' the ''player' object' by ''extending' 'pygame.sprite.Sprite;'' The 'new 'Surface' sprite' that  will be
# ''drawn' on the 'screen'' will be 'attributed 'as' the 'player:''"
class Player(pygame.sprite.Sprite):

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self):

        # "'super(Player, self).__init__()' is 'equivalent' to '''base' class,' 'pygame.sprite.Sprite.__init__(self).''"
        # This will use the "'super()' method to call the "__init__()" constructor of "Sprite." "super()" is typically
        # used for the "'inheritance' of 'classes'" in "OOP ('Object-Oriented Programming')." They "'expands' the
        # 'functionality' of an ''inherited' method' or more through 'permissible access' to a ''parent' and or 'sub'
        # class:'"
        super(Player, self).__init__()

        # "'Create' a 'new ''imaged' surface (I.e., 'Jet.png')'' and then create a 'transparent' copy of its 'surface'
        # with the 'desired' 'pixel format' 'through' the 'convert_alpha()' command:"
        self.the_surface = pygame.image.load("Jet.png")

        # "Scale" the image:
        self.the_surface = pygame.transform.scale(self.the_surface, size=(920 / 11, 550 / 11))

        # "'Create' a 'new 'rectangular 'sprite'' 'on' the 'surface (Or 'image')' 'of' the 'display:'"
        self.rect = self.the_surface.get_rect()

    # "'Move' the 'sprite' 'based upon' the ''keys' 'that are 'pressed''' by the 'player'" on their  keyboard" and
    # "secure" their "object" on the display window:
    def update(self, pressed_keys):

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-17, 0)

        if self.rect.right < 800 and pressed_keys[K_RIGHT]:
            self.rect.move_ip(17, 0)

        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -17)

        if self.rect.bottom < 600 and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 17)


# "'Define' the ''enemy' object' by ''extending' 'pygame.sprite.Sprite;'' The 'new 'Surface' sprite' that will be
# ''drawn' on the 'screen'' will be 'attributed 'as' the 'enemy:''"
class Enemy(pygame.sprite.Sprite):

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self):
        # "'super(Player, self).__init__()' is 'equivalent' to '''base' class,' 'pygame.sprite.Sprite.__init__(self).''"
        # This will use the "'super()' method to call the "__init__()" constructor of "Sprite." "super()" is typically
        # used for the "'inheritance' of 'classes'" in "OOP ('Object-Oriented Programming')." They "'expands' the
        # 'functionality' of an ''inherited' method' or more through 'permissible access' to a ''parent' and or 'sub'
        # class:'"
        super(Enemy, self).__init__()

        # "'Create' a 'new ''imaged' surface (I.e., 'Missile.png')'' and then create a 'transparent' copy of its
        # 'surface' with the 'desired' 'pixel format' 'through' the 'convert_alpha()' command:"
        self.the_surface = pygame.image.load("Missile.png")

        # "Scale" the image:
        self.the_surface = pygame.transform.scale(self.the_surface, size=(310 / 8, 230 / 8))

        # "'Create' 'new 'Missile.pngs' at ''random' locations 'along' the 'right edge' of the 'screen' and
        # ''centered' 'off'' of it:'''"
        self.rect = self.the_surface.get_rect(center=(random.randint(800, 900), random.randint(0, 600)))

        # "Define a 'random number' 'between '5' and '20.''" This will "specify 'how fast' the 'enemy' 'moves towards'
        # the 'player:'"
        self.speed = random.uniform(5, 20)

    # "Remove" the sprite when it "passes the 'left edge' of the screen."
    def update(self):
        # Check and make sure that the "right side" of the rectangle has "gone past" the "left side" of the screen at the
        # "pre-defined 'speed:'"
        self.rect.move_ip(-self.speed, 0)

        # If the "right side" of the rectangle has "gone past" the "left side" of the screen at the "pre-defined 'speed,'
        # then "'prevent it' from being 'processed' any further by 'killing it:'"
        if self.rect.right < 0:
            self.kill()


# "'Create' the 'new and 'following' 'explosion 'animated'' and display it when the 'program's 'sprites' 'collides:'"
class Explosion(pygame.sprite.Sprite):

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self, center):

        # "'super(Player, self).__init__()' is 'equivalent' to '''base' class,' 'pygame.sprite.Sprite.__init__(self).''"
        # This will use the "'super()' method to call the "__init__()" constructor of "Sprite." "super()" is typically
        # used for the "'inheritance' of 'classes'" in "OOP ('Object-Oriented Programming')." They "'expands' the
        # 'functionality' of an ''inherited' method' or more through 'permissible access' to a ''parent' and or 'sub'
        # class:'"
        super(Explosion, self).__init__()

        self.the_explosion_animation = []
        for i in range(0, 9):
            the_explosion_image = pygame.image.load(f"Explosions/Explosion_V1_#{i}.png")
            the_explosion_image = pygame.transform.scale(the_explosion_image, size=(1252 / 10, 1252 / 10))
            self.the_explosion_animation.append(the_explosion_image)

        # This "'index' will be used to 'access' the ''particular' 'explosion 'animated' images'' ''within' the list.'"
        # And, by setting the index's initial value to "0," the program will "'always' create the ''first' 'explosion
        # animated image'' 'every time' a new explosion instance is created:"
        self.index = 0

        # This line of code will "'produce' the 'explosion 'animated' images' ''on' the 'screen'' ''in 'order''
        # ''through' the 'index:'''"
        self.image = self.the_explosion_animation[self.index]

        # This will "'create' a 'new 'rectangle'' for the 'explosion 'animation:'"
        self.rect = self.image.get_rect()

        self.rect.center = center

        # This "'counter' 'will 'increase' ''every' 'iteration:'''"
        self.the_counter = 0

    def update(self):

        # This line of code will "'set' the 'rate of 'change'' at which the 'explosion 'animation'' will 'update:'"
        the_explosion_speed = 5 / 4

        # This line of code will "'update' the 'explosion 'animation'' 'by ''incrementing' the 'counter' by '1' at
        # ''each' iteration:'''"
        self.the_counter += 1

        # "'Go through' the ''explosion 'animation'' images' list' and '''access' its 'images'' in 'order:''"
        if self.the_counter >= the_explosion_speed and self.index < len(self.the_explosion_animation) - 1:
            # This line of code will "'reset' the 'counter:'"
            self.the_counter = 0

            # This line of code will "'access' the ' '''post' initial' 'explosion image'' '''from' and 'within' its
            # 'list'' ''by' and 'after' ''incrementing' the 'index:''''"
            self.index += 1
            self.image = self.the_explosion_animation[self.index]

        # This line of code will "'reset' the ''explosion animation's' 'index'' ''after' 'it' has been 'completed:''"
        if self.index >= len(self.the_explosion_animation) - 1 and self.the_counter >= the_explosion_speed:
            self.kill()


# "'Create' the 'new and 'following' 'surfaced 'text'' 'with' the 'pre-defined' 'style'' and 'center' it on the
# 'screen:'"
class TheStartButtonTextDisplay(pygame.sprite.Sprite):

    # This--def __init__(self, color, width, height)--is a "Constructor;" "Constructors" are used to "''initialize
    # ('Assign 'values--like collections of statements (i.e 'instructions')'')' to the 'data member' of a 'class'' when
    # an ''object' of the 'class'' is 'created.'"
    def __init__(self):

        # "'super(Player, self).__init__()' is 'equivalent' to '''base' class,' 'pygame.sprite.Sprite.__init__(self).''"
        # This will use the "'super()' method to call the "__init__()" constructor of "Sprite." "super()" is typically
        # used for the "'inheritance' of 'classes'" in "OOP ('Object-Oriented Programming')." They "'expands' the
        # 'functionality' of an ''inherited' method' or more through 'permissible access' to a ''parent' and or 'sub'
        # class:'"
        super(TheStartButtonTextDisplay, self).__init__()

        # "Define" the new "text's 'font:'"
        self.the_start_button_font = pygame.font.Font("8-BIT WONDER.ttf", 36)

        # "'Create' the 'new and 'following' 'rectangular surfaced 'text:''"
        self.the_start_button_surface = self.the_start_button_font.render('Start', True, "Black")

        # "'Return' and 'position' the 'new and 'following' 'rectangular surfaced 'text'' on the 'center' of the screen:"
        self.the_start_button_surface_rect = self.the_start_button_surface.get_rect(center=(400, 300))

        # "'Establish' a '''singular' limit' condition' for the 'amount of times' a 'player' can 'click' the ''start'
        # button display:'"
        self.the_mouse_click_limiter = False

    def is_being_displayed(self):

        # "'Display' the 'new and 'following' 'surfaced 'text:''"
        Screen.blit(self.the_start_button_surface, self.the_start_button_surface_rect)

    def is_being_clicked(self):

        # This will be used a " ''boolean' measure' 'to 'determine 'when' the 'player' 'left-clicks' the ''start' button
        # text display' on the screen:''"
        the_players_action = False

        # "'Get' the ''player's' 'mouse 'position:'''"
        the_mouse_position = pygame.mouse.get_pos()

        # "'Check' to 'see' 'when the 'player' ''moves' their mouse 'over' 'and or' then 'clicks' the ''start' button
        # display:''" "'Check' to 'see' 'when the 'mouse cursor' 'collides' 'with' the the ''start' button display:''"
        if self.the_start_button_surface_rect.collidepoint(the_mouse_position):

            # "'Check' to 'see' 'when the ''start' button display' has been 'left-clicked' by the 'player'
            # 'only 'once:'''"
            if pygame.mouse.get_pressed()[0] == 1 and self.the_mouse_click_limiter is False:
                the_players_action = True
                self.the_mouse_click_limiter = True

        # "'Check' to 'see' 'when the ''start' button display'' has been 'released' ''after' 'being 'left-clicked' 'only
        # once:''' by the 'player:'"
        if pygame.mouse.get_pressed()[0] == 0:
            # "'if' the 'player' 'releases' their 'mouse's ''left' button,'' 'then '''reset' 'the_mouse_click_limiter''
            # 'back' to 'False:'''"
            self.the_mouse_click_limiter = False

        # "'Update' the ''player's' 'action'' ''when' they ''click' the ''start' button display:'''"
        return the_players_action


# |---------------------------------------------------------------------------------------------------------------------|
# |                 | These Two Lines of Codes "'CREATES' 'CUSTOM 'UNIQUE' EVENTS'" "IN" The Program! |                 |
# |---------------------------------------------------------------------------------------------------------------------|

# "'Create' a 'new 'custom 'unique' event (By adding '1' to the 'USER EVENT')''' for 'adding' 'new 'enemies,'' that will
# later then get 'included' into 'the_group_of_sprites' on 'line: '370:''"
Add_New_Enemies = pygame.USEREVENT + 1

# "''Insert' 'this event' ''into' the 'event queue'' at 'regular intervals' ''throughout' the game' by 'firing' ''new'
# 'enemies'' 'every '250 milli-seconds,' or 'four times per second'' 'towards the ''left side' of the 'screen:'''"
pygame.time.set_timer(Add_New_Enemies, 250)

# |---------------------------------------------------------------------------------------------------------------------|
# |   | These Lines of Codes Will 'GROUPS'" The "PROGRAM'S 'ELEMENTS'" "AFTER" It "'INSTANTIATES' A 'NEW 'PLAYER!'" |   |
# |---------------------------------------------------------------------------------------------------------------------|

# "'Instantiate' a 'new 'player.''"

Player = Player()

#                  |--------------------------------------------------------------------------------|
#                  |  | "''Create' 'groups'' to ''hold' ''every' sprite' ''in' the 'program!:''" |  |
#                  |--------------------------------------------------------------------------------|

# "'The_Enemies' 'will be 'grouped' and 'used for 'collision detection' and 'position updates.'''"
The_Enemies = pygame.sprite.Group()

the_explosion_group = pygame.sprite.Group()

# - "''All' of the 'sprites'' 'will be 'grouped' and 'used for 'rendering.'''"
the_group_of_sprites = pygame.sprite.Group()

# - "'Add' the 'player' to the ''group' of 'sprites:''"
the_group_of_sprites.add(Player)

# |---------------------------------------------------------------------------------------------------------------------|
# |            | These Three Lines of Codes "'CREATES' 'INSTANCES!'" For the Program's "'TEXTS' DISPLAYS!" |            |
# |---------------------------------------------------------------------------------------------------------------------|

# "'Create' a 'new 'instance'' for the ''start' button' using the ''TheStartButtonDisplay' class:'"
the_start_button = TheStartButtonTextDisplay()

# |---------------------------------------------------------------------------------------------------------------------|
# |                                           | The Program's "VARIABLES!!" |                                           |
# |---------------------------------------------------------------------------------------------------------------------|

# "'Run' this program 'until' the 'player' 'decides to 'quit:''"
the_programs_running_status = True

# # "This very important line of code will 'act' as a ''boolean' data type' for ''specific' conditions' for ''certain'
# executions' ''of' and 'throughout'' the program:'"
the_programs_playing_status = False

# "'Set' the 'background 'surface position'' 'to the 'pre-defined 'value:'''"
The_Background_Surface_Position = 0

# |---------------------------------------------------------------------------------------------------------------------|
# |                                | This Is Our Program's "MAIN 'CONDITIONAL' LOOP!'" |                                |
# |---------------------------------------------------------------------------------------------------------------------|

# This is the "main 'conditional' loop:"
while the_programs_running_status:

    # |-----------------------------------------------------------------------------------------------------------------|
    # |                | These Seven "IMPORTANT" Lines of Codes "ANIMATES" the Program's "BACKGROUND!" |                |
    # |-----------------------------------------------------------------------------------------------------------------|

    # "'Fill' the ''initial' 'Surface'' of the 'screen' 'white:'"
    Screen.fill("White")

    # "'Draw' the 'background 'surface (Or 'image,' i.e., 'Troposphere_Bg.png')'' ''on' the 'screen' 'at' the 'given
    # position:''"
    Screen.blit(The_Background_Surface, (The_Background_Surface_Position, 0))

    # "'Draw' 'another 'background 'surface (Or 'image,' i.e., 'Troposphere_Bg.png')'' ''on' the 'screen' 'at' the
    # 'given position:''"
    Screen.blit(The_Background_Surface, (The_Background_Surface_Position + 800, 0))

    # "'After' the 'background 'surface (Or 'image,' i.e., 'Troposphere_Bg.png')'' 'moves 'beyond' the 'width' of the
    # 'screen,'' ''reset' its 'position'' and 'continue 'looping' it' at the 'program's ''pre-defined' 'speed:'''"
    if The_Background_Surface_Position <= -800:
        Screen.blit(The_Background_Surface, (The_Background_Surface_Position + 800, 0))
        The_Background_Surface_Position = 0
    The_Background_Surface_Position -= 20

    # |-----------------------------------------------------------------------------------------------------------------|
    # |                                   | "DISPLAY" the Program's "'MENU' TEXT!!" |                                   |
    # |-----------------------------------------------------------------------------------------------------------------|

    if the_programs_playing_status is False:
        the_start_button.is_being_displayed()

    # |-----------------------------------------------------------------------------------------------------------------|
    # |                                                                                                                 |
    # |-----------------------------------------------------------------------------------------------------------------|

    # "''look' at' ''every' event' ''in' the 'queue:''"
    for the_event in pygame.event.get():

        # "'Only' ''run' the program 'after' the 'player' has 'clicked' the ''start' button display (OR--see the
        # codes below between 'line: '306-310''):''"
        if the_start_button.is_being_clicked():
            the_programs_playing_status = True

        # "'Check' to 'see' 'when the ''post-defined' keyboard buttons (I.e., 'K_ESCAPE,' and 'K_RETURN') are
        # ''pressed' and 'released'' 'as 'events''' in the queue:"
        if the_event.type == KEYDOWN:

            # "'Only' ''run' the program 'after' the 'player' has 'pressed' the ''return (Or 'enter')' key' on their
            # keyboard (OR--see the codes above between 'line: '297-302''):'"

            if the_event.key == K_RETURN:
                the_programs_playing_status = True

            # Did the "player" "hit" the "'Escape (ESC)' key?" "If so," then "'terminate' the 'program' by ''setting'
            # 'Running' to 'False:''"
            if the_event.key == K_ESCAPE:
                the_programs_running_status = False

        # Did the "player" "click" the "Window 'exit' button?" "If so," then "'terminate' the 'program' by ''setting'
        # 'Running' to 'False:''"
        elif the_event.type == QUIT:
            the_programs_running_status = False

        # "'Add' 'new 'enemies'' ''every' frame' '''throughout' the program' 'until the 'player' 'exits' it:''"
        elif the_event.type == Add_New_Enemies:

            if the_programs_playing_status is True:

                # "'Create' the 'new 'enemy'' and ''add' it' to 'sprite groups:'"
                The_New_Enemy = Enemy()

                # - "'Add' 'The_New_Enemy' to the ''group' of 'The_Enemies:''"
                The_Enemies.add(The_New_Enemy)

                # - "'Add' 'The_New_Enemy' to 'the_group_of_sprites:'"
                the_group_of_sprites.add(The_New_Enemy)
            else:
                the_programs_playing_status = the_programs_playing_status

    # |-----------------------------------------------------------------------------------------------------------------|
    # |                          | These Three Lines of Codes Are for the "PLAYER'S INPUTS!" |                          |
    # |-----------------------------------------------------------------------------------------------------------------|

    # "'Return' ''all' of the 'keys'' that were ''pressed' 'by' the 'player'' and 'then ''stored' 'in 'queue''' 'by'
    # the 'program:''"
    Pressed_Keys = pygame.key.get_pressed()

    # "'Update' the '''player's' 'player 'sprite 'position''' ''every frame' ''based upon' the ''keys' 'that were
    # 'pressed' ''by' the 'player''''''' on their keyboard:"
    Player.update(Pressed_Keys)

    # "'Update' the ''enemies' sprites' 'positions:'"
    The_Enemies.update()

    # |-----------------------------------------------------------------------------------------------------------------|
    # |      | These Four Lines of Codes "'DETECTS' ANY 'COLLISION' 'BETWEEN' THE 'PLAYER' AND 'ENEMY' CLASSES!" |      |
    # |-----------------------------------------------------------------------------------------------------------------|

    # "''Draw' 'all'' of the 'sprites' to the 'screen:'"
    for all_of_the_sprites in the_group_of_sprites:
        Screen.blit(all_of_the_sprites.the_surface, all_of_the_sprites.rect)

    # "'Check' to 'see' ''whether' or 'not'' the ''player' sprite' 'has ''collided' ''with' 'any'' of the ''enemy'
    # sprites:'''"
    if pygame.sprite.spritecollideany(Player, The_Enemies):

        # "'Create' an ''explosion' 'animation'' 'whenever' the ''player' sprite' 'collides' ''with' 'any'' of the
        # ''enemy' sprites:''
        the_explosion_animation = Explosion(Player.rect.center)
        the_explosion_group.add(the_explosion_animation)
        the_explosion_group.draw(Screen)
        the_explosion_group.update()
        the_programs_playing_status = False

    # |-----------------------------------------------------------------------------------------------------------------|
    # |                                 | "DISPLAY" the Program's "COLLISION SPRITE!" |                                 |
    # |-----------------------------------------------------------------------------------------------------------------|

    the_explosion_group.draw(Screen)
    the_explosion_group.update()

    # |-----------------------------------------------------------------------------------------------------------------|
    # |                                                                                                                 |
    # |-----------------------------------------------------------------------------------------------------------------|

    # Calling "flip()" after "blit(image (left, top))" will update the "display" with the newly drawn "Surface" or
    # else nothing will change. "'blit()' 'draws the 'image' 'to the 'screen' at the ''given'  position.''" It accepts
    # either a "Surface" or a "string" as its "image parameter." If image is a "str" then the named image will be
    # "loaded from the 'images'/directory."
    pygame.display.flip()

    # "'Give' the 'player' the ''option' to 'adjust'' the 'frame rate' of the program:"
    The_Frame_Rate = pygame.time.Clock()

    # "'Ensure' that the program ''maintains' a 'frame rate' of 'x' 'frames per second:''"
    The_Frame_Rate.tick(30)

pygame.quit()
