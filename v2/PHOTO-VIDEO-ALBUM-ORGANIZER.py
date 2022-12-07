import sys
import os
try:
    sys.path.insert(1, "D:/Users/Vlad/Projects/Applications/FOXY-FUNCTIONS")
    from FoxyFunctions import ff
    
    class main:
        def __init__(self):
            # create a foxy object
            self.ff = ff("APP TEMPLATE", "1.0")

            # load settings
            self.settings = self.ff.get_settings()

            # display main menu
            self.display_menu()
        
        def display_menu(self):
            # display header
            self.ff.display_header()

            # display main menu
            main_menu = (("START", self.start), ("EDIT SCRIPT", self.edit), ("SETTINGS", self.set_settings), ("HELP", self.help), ("EXIT", self.exit))
            self.ff.display_menu("MAIN MENU", main_menu)
        
        def start(self):
            # ENTER YOUR CODE HERE

            # go back to main menu
            self.display_menu()
        
        def edit(self):
            # edit script file
            os.popen("script.txt")
            
            # go back to main menu
            self.display_menu()

        def set_settings(self):
            # set new settings
            self.ff.set_settings(self.settings)

            # go back to main menu
            self.display_menu()
        
        def help(self):
            # display readme file
            self.ff.help()

            # go back to main menu
            self.display_menu()
        
        def exit(self):
            # exit the program
            self.ff.exit()

    main()
except Exception as e:
    print(e)
    input("")