from collections import deque

DEBUG = True

def find_invalid(filename, size):
    queue = deque()

    with open(filename) as inputfile:
        for line in inputfile:
            num = int(line.strip())

            if size > 0:
                # Decrement size to load the cache
                queue.append(num)
                size -= 1
            else:
                # Check num against the cache. Assume it fails.
                valid = False

                for item in queue:
                    # We're using item as one of the two numbers in the cache.
                    # The other one will be diff.
                    diff = num - item

                    if diff in queue:
                        # Found two items in the cache, so pop one, and add our new number.
                        queue.popleft()
                        queue.append(num)

                        # It's valid, so don't return, but be also don't need to loop anymore.
                        valid = True
                        break

                if not valid:
                    # This is the number we're looking for!
                    return num

def find_weakness(filename, target):
    stream = list()

    with open(filename) as inputfile:
        for line in inputfile:
            stream.append(int(line.strip()))

    # In Python, `list.pop(0)` is slow, so we operate on the tail, and to preserve order, `reverse()`
    # We could probably assume that the stream does not contain two solutions, but...
    # If it does, this will return the "first" one.
    stream.reverse()

    while len(stream) > 0:
        idx = 0
        acc = stream.pop()
        max_num, min_num = acc, acc

        while acc < target:
            # Lovely negative indexes, to move backwards through the list.
            idx -= 1
            stream_num = stream[idx]
            acc += stream_num
            max_num = stream_num if stream_num > max_num else max_num
            min_num = stream_num if stream_num < min_num else min_num

        if acc == target:
            return max_num + min_num


if __name__ == '__main__':
    DEBUG = False

    invalid = None
    weakness = None

    if not DEBUG:
        invalid = find_invalid('./input.txt', 25) # 1721308972
        weakness = find_weakness('./input.txt', invalid) # 209694133
    else:
        invalid = find_invalid('./test.txt', 5) # 127
        weakness = find_weakness('./test.txt', invalid) # 62

    print(f'invalid: {invalid}')
    print(f'weakness: {weakness}')
