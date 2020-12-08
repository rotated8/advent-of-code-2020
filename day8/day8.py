DEBUG = True
DEBUG_STR = 'acc: {}, step: {}, op: {}, val: {}'

class Processor:
    def __init__(self, filename=None):
        self.instructions = list()
        self.accumulator = 0
        self.program_counter = 0
        self.steps = 0
        self.visited = set()

        if filename is not None:
            self.load(filename)
            self.run()

    def __str__(self):
        return str(self.accumulator)

    def load(self, filename):
        with open(filename) as inputfile:
            self.instructions = inputfile.readlines()

    def run(self):
        while self.program_counter not in self.visited:
            self.visited.add(self.program_counter)
            self.steps += 1

            instruction = self.instructions[self.program_counter].strip()
            operation, value = instruction[:3], int(instruction[4:])

            if operation == 'acc':
                self.accumulator += value
                self.program_counter += 1
            elif operation == 'jmp':
                self.program_counter += value
            else:
                self.program_counter += 1

            if DEBUG:
                print(DEBUG_STR.format(self.accumulator, self.steps, operation, value))

if __name__ == '__main__':
    DEBUG = False

    if not DEBUG:
        print('acc:', Processor('input.txt')) # 1949
    else:
        print('acc:', Processor('test.txt')) # 5
