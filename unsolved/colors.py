class Colors():
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (36, 110, 139)

    colors = {
        "white": white,
        "yellow": yellow,
        "black": black,
        "red": red,
        "green": green,
        "blue": blue
    }

    def add_alpha(color, alpha):
        return (color[0], color[1], color[2], alpha)
