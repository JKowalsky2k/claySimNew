
class Color():
    def __init__(self) -> None:
        self.black               = (  0,   0,   0)
        self.white               = (255, 255, 255)
        self.red                 = (255,   0,   0)
        self.blue                = (  0,   0, 255)
        self.green               = (  0, 255,   0)
        self.yellow              = (255, 255,   0)
        self.orange              = (255, 128,   0)
        self.brown               = (139,  69,  19)
        self.blue_button_fg      = ( 51, 153, 255)
        self.blue_button_bg      = (102, 178, 255)
        self.yellow_button_fg    = (204, 204,   0)
        self.yellow_button_bg    = (240, 230, 140)
        self.green_button_fg     = ( 50, 205,  50)
        self.green_button_bg     = ( 34, 139,  34)
        self.purple_button_fg    = (138,  43, 226)
        self.purple_button_bg    = (147, 112, 219)
        self.red_button_fg       = (255,   0,   0)
        self.red_button_bg       = (220,  92,  60)
        self.disable             = (169, 169, 169)

    def get_button_color_theme(self, theme):
        if theme == "green":
            return self.green_button_fg, self.green_button_bg
        elif theme == "yellow":
            return self.yellow_button_fg, self.yellow_button_bg
        elif theme == "purple":
            return self.purple_button_fg, self.purple_button_bg
        elif theme == "red":
            return self.red_button_fg, self.red_button_bg
        else:
            return self.blue_button_fg, self.blue_button_bg