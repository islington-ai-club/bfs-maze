class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(p1, p2):
        return Point(p1.x + p2.x, p1.y + p2.y)

    def to_str(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

    def print_points(points):
        final_str = ""

        for point in points:
            final_str += point.to_str() + '\n'

        print(final_str)
