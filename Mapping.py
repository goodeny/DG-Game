import curses

class Platform:
    def __init__(self, pos_x, pos_y, width, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.color = color

    def draw(self, stdscr):
        if self.color == 0:
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            GREEN = curses.color_pair(1)
            stdscr.addstr(self.pos_y, self.pos_x, "_" * self.width, GREEN)
        else:
            curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
            CYAN = curses.color_pair(5)
            stdscr.addstr(self.pos_y, self.pos_x, "_" * self.width, CYAN)
        
class MapGame:
    def __init__(self):
        self.platforms =  [
                Platform(22, 26, 1, 0),
                Platform(23, 26, 1, 0),
                Platform(24, 26, 1, 0),
                Platform(25, 26, 1, 0),
                Platform(26, 26, 1, 0),
                Platform(27, 26, 1, 0),
                 
                Platform(16, 25, 1, 0),
                Platform(17, 25, 1, 0),
                Platform(18, 25, 1, 0),
                Platform(19, 25, 1, 0),

                Platform(10, 23, 1, 0),
                Platform(11, 23, 1, 0),
                Platform(12, 23, 1, 0),
                Platform(13, 23, 1, 0),
                Platform(14, 23, 1, 0),

                Platform(18, 17, 1, 0),
                Platform(19, 17, 1, 0),
                Platform(20, 17, 1, 0),
                Platform(21, 17, 1, 0),
                Platform(22, 17, 1, 0),

                Platform(18, 21, 1, 0),
                Platform(19, 21, 1, 0),
                Platform(20, 21, 1, 0),
                Platform(21, 21, 1, 0),
                Platform(22, 21, 1, 0),

                Platform(35, 17, 1, 0),
                Platform(36, 17, 1, 0),
                Platform(37, 17, 1, 0),
                Platform(38, 17, 1, 0),
                Platform(39, 17, 1, 0),
                Platform(40, 17, 1, 0),

                Platform(27, 17, 1, 0),
                Platform(28, 17, 1, 0),
                Platform(29, 17, 1, 0),
                Platform(30, 17, 1, 0),

                Platform(37, 17, 1, 0),
                Platform(38, 17, 1, 0),
                Platform(39, 17, 1, 0),
                Platform(40, 17, 1, 0),
                Platform(41, 17, 1, 0),

                Platform(42, 15, 1, 0),
                Platform(43, 15, 1, 0),
                Platform(44, 15, 1, 0),
                Platform(45, 15, 1, 0),
                Platform(46, 15, 1, 0),
                Platform(47, 15, 1, 0),
                Platform(48, 15, 1, 0),
                Platform(49, 15, 1, 0),
                
                Platform(55, 15, 1, 0),
                Platform(56, 15, 1, 0),
                Platform(57, 15, 1, 0),
                Platform(58, 15, 1, 0),
                Platform(59, 15, 1, 0),

                Platform(65, 15, 1, 0),
                Platform(66, 15, 1, 0),
                Platform(67, 15, 1, 0),
                Platform(68, 15, 1, 0),
                Platform(69, 15, 1, 0),

                Platform(75, 18, 1, 0),
                Platform(76, 18, 1, 0),
                Platform(77, 18, 1, 0),
                Platform(78, 18, 1, 0),
                Platform(79, 18, 1, 0),

                Platform(82, 16, 1, 0),
                Platform(83, 16, 1, 0),
                Platform(84, 16, 1, 0),
                Platform(85, 16, 1, 0),
                Platform(86, 16, 1, 0),
                Platform(87, 16, 1, 0),
   
                Platform(91, 15, 1, 0),
                Platform(92, 15, 1, 0),
                Platform(93, 15, 1, 0),
                Platform(94, 15, 1, 0),
                Platform(95, 15, 1, 0),

                Platform(100, 14, 1, 0),
                Platform(101, 14, 1, 0),
                Platform(102, 14, 1, 0),
                Platform(103, 14, 1, 0),
                Platform(104, 14, 1, 0),

                Platform(108, 13, 1, 1),
                Platform(109, 13, 1, 1),
                Platform(110, 13, 1, 1),
                Platform(111, 13, 1, 1),
                Platform(112, 13, 1, 1),
            ]
