from collections import deque

DEBUG = True

def main(filename, size):
    queue = deque()

    with open(filename) as inputfile:
        for line in inputfile:
            num = int(line.strip())

            if size > 0:
                queue.append(num)
                size -= 1
            else:
                valid = False

                for item in queue:
                    diff = num - item

                    if diff in queue:
                        queue.popleft()
                        queue.append(num)
                        valid = True
                        break

                if not valid:
                    return num

if __name__ == '__main__':
    DEBUG = False

    if not DEBUG:
        print('num:', main('./input.txt', 25)) # 1721308972
    else:
        print('num:', main('./test.txt', 5)) # 127
