RISE = 2
RUN = 1

def descend(y_off, x_off, trees, counter):
    # x_off is the total offset. Adjust that to be within the string given.
    adj_x = x_off - (x_off//len(trees) * len(trees))
    adj_y = y_off + 1

    #print(y_off, adj_y, x_off, adj_x)
    #print((x_off//len(trees) + 1) * trees)
    if adj_y == 1:
        #print(x_off * '-' + '^')
        if trees[adj_x] == '#':
            counter += 1

    if adj_y == RISE:
        return (0, x_off + RUN, counter)

    return(adj_y, x_off, counter)

with open('./input.txt') as inputfile:
    x_offset = 0
    y_offset = 0
    counter = 0
    for line in inputfile:
        y_offset, x_offset, counter = descend(y_offset, x_offset, line.strip(), counter)
    print(counter)
