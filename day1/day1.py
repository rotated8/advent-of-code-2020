ans = 'l1: {}, l2: {}, l3: {}, product: {}'
sum_ans = 'l1: {}, l2: {}, l3: {}, sum: {}'
with open('./input1.txt') as inputfile:
    lines = [ int(line) for line in inputfile ]
    lines.sort()
    print(len(lines))

    cutoff = 2020 - lines[0] -lines[1]
    lines = [line for line in lines if line <= cutoff]
    print(len(lines))
    print(lines)

    while len(lines) > 2:
        l1 = lines.pop(0)

        for l2 in lines:
            for l3 in lines[1::]:
                sumlines = l1+l2+l3
                #print(sum_ans.format(l1, l2, l3, sumlines))
                if  sumlines == 2020:
                    print(ans.format(l1, l2, l3, l1*l2*l3))
