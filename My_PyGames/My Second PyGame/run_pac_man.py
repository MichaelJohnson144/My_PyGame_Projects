from pac_man import ItsElements

pac_man_is_running = ItsElements()

while pac_man_is_running.the_programs_running_status:
    # "'Display' the program's 'main menu:'"
    pac_man_is_running.the_current_menu.the_display_menu()

    pac_man_is_running.the_programs_main_loop()
