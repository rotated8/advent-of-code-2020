DEBUG = True
RISE = 1
RUN = 3

def descend(y_off, x_off, counter, terrain):
    # Bounds check y_off and x_off.
    adj_y = y_off % RISE
    adj_x = x_off % len(terrain)

    if DEBUG:
        print(y_off, adj_y, x_off, adj_x)

    # Check for a tree, if necessary
    if adj_y == 0:
        if DEBUG:
            print((x_off//len(terrain) + 1) * terrain)
            print(x_off * '-' + '^')

        if terrain[adj_x] == '#':
            counter += 1

        # Increment y_off, add RUN to x_off after checks. Allows us to check (0,0).
        return (y_off + 1, x_off + RUN, counter)

    # Do not add RUN to x_off, we haven't finished RISE-ing yet.
    return(y_off + 1, x_off, counter)

if __name__ == '__main__':
    DEBUG = False

    with open('./input.txt') as inputfile:
        x_offset = 0
        y_offset = 0
        counter = 0
        for line in inputfile:
            # I was not stripping the line originally, and the return threw off the length.
            # y_off, x_off always go up. This accomodates lines of unequal length.
            y_offset, x_offset, counter = descend(y_offset, x_offset, counter, line.strip())
        print(counter)
