DEBUG = True
DEBUG_STR = 'acc: {}, step: {}, op: {}, val: {}'

class Processor:
    CHANGE_OP = { 'nop': 'jmp', 'jmp': 'nop' }

    def __init__(self, filename=None):
        self.instructions = list()
        self.accumulator = 0
        self.program_counter = 0
        self.steps = 0
        self.visited = set()

        if filename is not None:
            self.load(filename)

    def load(self, filename):
        with open(filename) as inputfile:
            for line in inputfile:
                self.instructions.append(line.strip())

    def repair(self):
        for idx in range(len(self.instructions)):
            # Get current instruction, operation.
            old_inst = self.instructions[idx]
            old_op = old_inst[:3]

            # Change the operation, if allowed.
            if old_op in Processor.CHANGE_OP:
                # Construct and insert new instruction
                new_inst = Processor.CHANGE_OP[old_op] + old_inst[3:]
                self.instructions[idx] = new_inst

                if DEBUG:
                    print(f'idx: {idx}, new inst: {new_inst}')

                self.run()

                if self.terminated():
                    # If the run completed successfully, return the result, like run() does.
                    return self.accumulator
                else:
                    # If not, reset the instruction, and the processor.
                    self.instructions[idx] = old_inst
                    self.reset()

        # If we get here, the program was either fine, or cannot be fixed.
        return None

    def run(self):
        while self.program_counter not in self.visited:
            # Loop control
            self.visited.add(self.program_counter)
            self.steps += 1

            # Parse instruction
            instruction = self.instructions[self.program_counter]
            operation, value = instruction[:3], int(instruction[4:])

            # Perform operation
            if operation == 'acc':
                self.accumulator += value
                self.program_counter += 1
            elif operation == 'jmp':
                self.program_counter += value
            else:
                self.program_counter += 1

            # Rather than get an index out of bounds, exit.
            if self.program_counter >= len(self.instructions):
                break

            if DEBUG:
                print(DEBUG_STR.format(self.accumulator, self.steps, operation, value))

        # Return the accumulator, to make the script output what we want.
        return self.accumulator

    def terminated(self):
        return True if self.program_counter == len(self.instructions) else False

    def reset(self):
        self.accumulator = 0
        self.program_counter = 0
        self.steps = 0
        self.visited = set()

if __name__ == '__main__':
    DEBUG = False

    if not DEBUG:
        print('acc:', Processor('input.txt').run()) # 1949
        print('acc:', Processor('input.txt').repair()) # 2092
    else:
        print('acc:', Processor('test.txt').run()) # 5
        print('acc:', Processor('test.txt').repair()) # 8
