import re

DEBUG = True

class Bag:
    def __init__(self, name, contents=None, containers=None):
        self.name = name
        # Dict of names of bags and the number of that bag this bag holds.
        self.contents = dict()
        # Set of bag names that can contain this bag
        self.containers = set()

        if contents is not None:
            self.contents.update(contents)

        if containers is not None:
            self.containers.update(containers)

    def __str__(self):
        output = [self.name]
        output.append(f'    contents: {self.contents}')
        output.append(f'    containers: {self.containers}')

        return "\n".join(output)

class BagManager:
    NAME_REGEX = re.compile('(?P<num>[0-9]+)\s+(?P<name>[a-z]+\s+[a-z]+)')

    def __init__(self, rule_file):
        # The keys are names of bags that can be held.
        # The values are sets of the bags that can hold them.
        self.bags = dict()

        with open(rule_file) as rules:
            for line in rules:
                self.add_rule(line.strip())

        if DEBUG:
            print(self)

    def __str__(self):
        output = [str(type(self))]
        for key in self.bags:
            output.append(f'  {self.bags[key]}:')

        return "\n".join(output)

    def add_rule(self, rule):
        bag_name, _, contents = rule.partition(' bags contain ')
        bag_name = bag_name.strip()

        parsed_contents = dict()
        for content in contents.split(', '):
            if not content.startswith('no other bags'):
                match = BagManager.NAME_REGEX.match(content)
                parsed_contents[match.group('name')] = match.group('num')

        # Create or update this bag with what it contains
        bag = self.bags.get(bag_name)
        if bag is None:
            bag = Bag(bag_name, parsed_contents)
            self.bags[bag_name] = bag
        else:
            bag.contents.update(parsed_contents)

        # Create or update any contained bag with its container
        for contained_bag in parsed_contents:
            bag = self.bags.get(contained_bag)
            if bag is None:
                bag = Bag(contained_bag)
                bag.containers.add(bag_name)
                self.bags[contained_bag] = bag
            else:
                bag.containers.add(bag_name)

        #import pdb; pdb.set_trace()

    def find_bags_for(self, bag_name):
        bags_to_check = {bag_name}
        acceptable_bags = set()

        while len(bags_to_check) > 0:
            # Get a bag to check.
            name = bags_to_check.pop()
            bag = self.bags.get(name)

            if bag is not None:
                # Add bags that can contain that bag that aren't in `acceptable_bags` to check.
                bags_to_check.update(bag.containers.difference(acceptable_bags))

            # Now that we have checked it, add this bag to `acceptable_bags`.
            acceptable_bags.add(name)

        # We started with the given bag, but we assume bags can't hold themselves.
        acceptable_bags.remove(bag_name)

        return acceptable_bags

    def count_bags_in(self, bag_name):
        #TODO.
        return 1

if __name__ == '__main__':
    DEBUG = False

    if not DEBUG:
        bagman = BagManager('./input.txt')
        print(len(bagman.find_bags_for('shiny gold')), 'bags can contain the bag') # 370
        print('The bag contains', bagman.count_bags_in('shiny gold'), 'bags')
    else:
        bagman = BagManager('./test.txt')
        print(len(bagman.find_bags_for('shiny gold')), 'bags can contain the bag') # 4
        print('The bag contains', bagman.count_bags_in('shiny gold'), 'bags') # 32
        bagman = BagManager('./test2.txt')
        print('The bag contains', bagman.count_bags_in('shiny gold'), 'bags') # 126
