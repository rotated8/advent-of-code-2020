class BoardingPass:
    FMT_STR = 'Boarding Pass: Row: {}, Col: {}, ID: {}, Desc: {}'

    @staticmethod
    def from_desc(desc):
        row_desc = list(desc[:7])
        col_desc = list(desc[-3:])

        for _ in range(len(row_desc)):
            c = row_desc.pop(0)
            b = '1' if c == 'B' else '0'
            row_desc.append(b)

        for _ in range(len(col_desc)):
            c = col_desc.pop(0)
            b = '1' if c == 'R' else '0'
            col_desc.append(b)

        row = int(''.join(row_desc), 2)
        col = int(''.join(col_desc), 2)

        return (row, col)

    def __init__(self, description):
        self.row, self.col = self.from_desc(description)

    @property
    def id(self):
        return self.row * 8 + self.col

    @property
    def desc(self):
        row_desc = list(format(self.row, '07b'))
        col_desc = list(format(self.col, '03b'))

        for _ in range(len(row_desc)):
            b = bool(int(row_desc.pop(0)))
            c = 'B' if b else 'F'
            row_desc.append(c)

        for _ in range(len(col_desc)):
            b = bool(int(col_desc.pop(0)))
            c = 'R' if b else 'L'
            col_desc.append(c)

        return ''.join(row_desc + col_desc)

    def __str__(self):
        return BoardingPass.FMT_STR.format(self.row, self.col, self.id, self.desc)

if __name__ == '__main__':
    smallest = 1000
    biggest = 0

    # run once to determine smallest = 27, biggest = 963
    # top end of range is not inclusive, so add one.
    ids = list(range(27, 964))

    with open('./input.txt') as inputfile:
        for line in inputfile:
            line = line.strip()

            b = BoardingPass(line)

            if b.id > biggest:
                biggest = b.id
            if b.id < smallest:
                smallest = b.id

            ids.remove(b.id)

    print(smallest, biggest)
    print(ids)
