try:
    import os
    print("Installing Libraries...")
    os.system("pip install windows-curses")
except:
    pass

from curses import wrapper
from Mapping import MapGame
import curses
import time

class Player:
    def __init__(self):
        self.pos_x = 0 
        self.pos_y = 29 #MIN: 0 MAX: 29
        self.s_player = ("D")
        self.jump = False
        self.platform = False
        self.last_jump_time = 0
        
    def move_up(self):
        current_time = time.time()
        if current_time - self.last_jump_time > 2:
            self.last_jump_time = current_time
            self.pos_y -= 4
            curses.beep()
    
    def move_right(self):
        self.pos_x += 2

    def move_left(self):
        self.pos_x -= 2

    def apply_gravity(self):
        if self.pos_y < 29:
            self.pos_y += 1

class Fruit:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, stdscr):
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        MAGENTA = curses.color_pair(4)
        stdscr.addstr(self.pos_y, self.pos_x, "*", MAGENTA | curses.A_UNDERLINE)
        
class Game:
    def __init__(self):
        self.help_message = ""
        self.help_content = ""
        self.help_logo = "Press 'H' to open <Help menu>"
        self.logo = '''
                                ██████╗  ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
                                ██╔══██╗██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                                ██║  ██║██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
                                ██║  ██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                                ██████╔╝╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                                ╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                         
        '''
        self.help_bool = 0
        self.help_pos = [0,0]
        self.qnt_fruit = 0
        self.text_pos = [0,0]
        self.text_pos2 = [0,0]
        self.end = 0
        self.message = ""
        self.message2 = ""
        self.gravity = 1
        self.player1 = Player()
        
        self.fruits = [
            Fruit(12, 23),
            Fruit(18, 25),
            Fruit(20, 17),
            Fruit(38, 17),
            Fruit(68, 15),
            Fruit(86, 16),
            Fruit(102, 14)
        ]
        
    def main(self, stdscr):
        self.map = MapGame().platforms
        stdscr.nodelay(True)
        while True:
            stdscr.clear()

            for platforms in self.map:
                platforms.draw(stdscr)

            for fruits in self.fruits:
                fruits.draw(stdscr)
                
            curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            MARGENTA = curses.color_pair(2)
            YELLOW = curses.color_pair(3)
            stdscr.addstr(self.player1.pos_y, self.player1.pos_x, self.player1.s_player, YELLOW)

            try:
                key = stdscr.getkey()
            except:
                key = None

            self.verify_player(self.map)

            self.restart()
            stdscr.addstr(0, 60, f"{self.logo}", YELLOW)
            stdscr.addstr(2, 2, f"Fruits: {self.qnt_fruit}", MARGENTA)
            stdscr.addstr(8, 46, f"{self.help_logo}", YELLOW)

            if self.end == 1:
                stdscr.addstr(self.text_pos[0], self.text_pos[1], f"{self.message}", YELLOW)
                stdscr.addstr(self.text_pos2[0], self.text_pos2[1], f"{self.message2}", YELLOW)
                
            stdscr.addstr(self.help_pos[0], self.help_pos[1], f"{self.help_content}", YELLOW)
                

            if key == "KEY_LEFT":
                self.player1.move_left()
                self.player1.s_player = "G"
            elif key == "KEY_RIGHT":
                self.player1.move_right()
                self.player1.s_player = "D"
            elif key == "KEY_END":
                break
            elif key == "KEY_UP":        
                self.player1.move_up()
            elif key == "r" or key == "R":
                self.fruits.clear()
                self.gravity = 1
                self.fruits = [
                    Fruit(12, 23),
                    Fruit(18, 25),
                    Fruit(20, 17),
                    Fruit(38, 17),
                    Fruit(68, 15),
                    Fruit(86, 16),
                    Fruit(102, 14)
                ]
                self.player1.pos_x = 0
                self.player1.pos_y = 29
                self.end = 0
                self.qnt_fruit = 0
                self.message = ""
                self.message2 = ""
                self.text_pos[0] = 0
                self.text_pos[1] = 0
                self.text_pos2[0] = 0
                self.text_pos2[1] = 0
                self.restart_game = 0
                self.logo = '''
                                ██████╗  ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
                                ██╔══██╗██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                                ██║  ██║██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
                                ██║  ██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                                ██████╔╝╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                                ╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                         
        '''
                self.help_logo = "Press 'H' to open <Help menu>"
                self.help_bool = 0
                self.help_content = ""

            elif key == "KEY_DOWN":
                self.player1.pos_x = 108
                self.player1.pos_y = 12

            elif key == "h" or key == "H":
                if not self.help_bool:
                    self.help_content = "Just tap the Arrow   \nUpArrow: Jump\n  LeftArrow: Move to Left\n  RightArrow: Move to Right\n  'H': Help menu\n  'R': Restart Game\n  'END': Quit Game\n  Press 'H' to hide Help Menu"
                    self.help_bool = True
                    self.help_pos[0] = 7
                    self.help_pos[1] = 2
                else:
                    self.help_bool = False
                    self.help_content = ""      
                    self.help_pos[0] = 0
                    self.help_pos[1] = 0
               
            self.player1.apply_gravity()
            self.verify_fruit()
            
            stdscr.refresh()
            time.sleep(.1)

    def verify_player(self, platform):
        for i in platform:
            if self.player1.pos_y == i.pos_y and self.player1.pos_x == i.pos_x:
                self.player1.platform = True
                self.player1.pos_y = i.pos_y - 1
            else:
                self.player1.platform = False

    def verify_fruit(self):
        for i in self.fruits:
            if (self.player1.pos_x == i.pos_x and self.player1.pos_y == i.pos_y):
                self.qnt_fruit += 1
                i.pos_x = 4
                i.pos_y = 2

    def restart(self):
        self.end = 1
        r = [
            (108, 12),
            (109, 12),
            (110, 12),
            (111, 12),
            (112, 12)
        ]
        for i in r:
            if (self.player1.pos_x == i[0] and self.player1.pos_y == i[1]):
                self.help_content = ""
                self.help_message = ""
                self.logo = ''
                self.help_logo = ''
                self.player1.pos_x = 0
                self.player1.pos_y = 29
                self.text_pos[0] = 10
                self.text_pos[1] = 50
                self.text_pos2[0] = 20
                self.text_pos2[1] = 50
                self.message = '''
                                    ██████╗ ██████╗  █████╗ ████████╗███████╗██╗██╗██╗        
                                   ██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝╚══███╔╝██║██║██║        
                                   ██║  ███╗██████╔╝███████║   ██║     ███╔╝ ██║██║██║        
                                   ██║   ██║██╔══██╗██╔══██║   ██║    ███╔╝  ╚═╝╚═╝╚═╝        
                                   ╚██████╔╝██║  ██║██║  ██║   ██║   ███████╗██╗██╗██╗        
                                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝╚═╝╚═╝                                                                 
                '''
                self.message2 = "PRESS 'R' TO RESTART" 
                  

if __name__ == "__main__":
    try:
        game = Game()
        curses.wrapper(game.main)
    except:
        import os
        os.system("pip install windows-curses")

