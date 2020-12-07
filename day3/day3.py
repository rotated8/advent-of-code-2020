DEBUG = True

class Path:
    def __init__(self, map_file, rise=1, run=1):
        self.rise = rise
        self.run = run
        self.trees = 0
        self.checks = 0
        self.x_offset = 0
        self.y_offset = 0

        with open(map_file) as terrain_map:
            for line in terrain_map:
                # Still important to strip the line.
                self.descend(line.strip())

    def __str__(self):
        fmt_str = 'right: {}, down: {}, trees: {}'
        return fmt_str.format(self.run, self.rise, self.trees)

    def descend(self, terrain):
        # Adjust x_offset and y_offset for the length of the line, and the length of rise.
        adj_x = self.x_offset % len(terrain)
        adj_y = self.y_offset % self.rise

        if DEBUG:
            print(self.y_offset, adj_y, self.x_offset, adj_x)

        # Check for a tree, if necessary
        if adj_y == 0:
            if DEBUG:
                print((self.x_offset//len(terrain) + 1) * terrain)
                print(self.x_offset * '-' + '^')

            self.checks += 1
            if terrain[adj_x] == '#':
                self.trees += 1

            # Finished rising, so add run to x_offset.
            self.x_offset += self.run

        # Finished with this line of terrain; increment y_offset.
        self.y_offset += 1

if __name__ == '__main__':
    DEBUG = False

    if not DEBUG:
        p1_3 = Path('./input.txt', 1, 3)
        p1_1 = Path('./input.txt', 1, 1)
        p1_5 = Path('./input.txt', 1, 5)
        p1_7 = Path('./input.txt', 1, 7)
        p2_1 = Path('./input.txt', 2, 1)

        print(p1_3, p1_1, p1_5, p1_7, p2_1, sep="\n")
    else:
        p1_3 = Path('./test.txt', 1, 3)
        print(p1_3)

        #p1_1 = Path('./test.txt', 1, 1)
        #p1_5 = Path('./test.txt', 1, 5)
        #p1_7 = Path('./test.txt', 1, 7)
        #p2_1 = Path('./test.txt', 2, 1)
        #print(p1_3, p1_1, p1_5, p1_7, p2_1, sep="\n")

