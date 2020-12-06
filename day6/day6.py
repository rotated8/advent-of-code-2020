class Group:
    # Without the full set, the intersection will always return an empty set.
    # This was easier than popping a set from the list, because it's nondestructive.
    FULL_SET = set('abcdefghijklmnopqrstuvwxyz')

    def __init__(self):
        self.questions = list()

    def update(self, data):
        self.questions.append(set(data))

    def count_any(self):
        return len(set().union(*self.questions))

    def count_all(self):
        #import pdb; pdb.set_trace()
        return len(Group.FULL_SET.intersection(*self.questions))

if __name__ == '__main__':
    curr_group = Group()
    any_q = 0
    all_q = 0

    with open('./input.txt') as inputfile:
        for line in inputfile:
            line = line.strip()

            if line == '':
                any_q += curr_group.count_any()
                all_q += curr_group.count_all()
                #print(curr_group.count_all())
                curr_group = Group()
            else:
                # Only call update on non-blank lines, or they add an empty set.
                curr_group.update(line)

        any_q += curr_group.count_any()
        all_q += curr_group.count_all()
        #print(curr_group.count_all())

        print('Total Questions:', any_q, all_q)
