import re

DEBUG = True

class BagManager:
    NAME_REGEX = re.compile('(?P<num>[0-9]+)\s+(?P<name>[a-z]+\s+[a-z]+)')

    def __init__(self, rule_file):
        # The keys are names of bags that can be held.
        # The values are sets of the bags that can hold them.
        self.bag_containers = dict()

        # tbd
        self.bag_contents = dict()

        with open(rule_file) as rules:
            for line in rules:
                self.add_rule(line.strip())

        if DEBUG:
            print(self)

    def __str__(self):
        output = ['BagManager']
        for key in self.bags:
            output.append(f'    {key}:')
            for name, num in self.bags[key].items():
                output.append(f'        {name}: {num}')

        return "\n".join(output)

    def add_rule(self, rule):
        container, _, contents = rule.partition(' bags contain ')

        parsed_contents = dict()
        for bag in contents.split(', '):
            if not bag.startswith('no other bags'):
                match = BagManager.NAME_REGEX.match(bag)
                parsed_contents[match.group('name')] = match.group('num')

        # Update `self.bag_containers`
        for bag_name in parsed_contents:
            existing_containers = self.bag_containers.get(bag_name, set())
            existing_containers.add(container.strip())
            self.bag_containers[bag_name] = existing_containers
            #import pdb; pdb.set_trace()

        # Update `self.bag_contents`
        #TODO.

    def find_bags_for(self, bag_name):
        bags_to_check = {bag_name}
        acceptable_bags = set()

        while len(bags_to_check) > 0:
            # Get a bag to check.
            name = bags_to_check.pop()
            # Get bags that can contain that bag that aren't in `acceptable_bags`.
            bags_to_add = self.bag_containers.get(name, set()) - acceptable_bags
            # Add any bags to `bags_to_check`
            bags_to_check.update(bags_to_add)

            # Now that we have checked it, add this bag to `acceptable_bags`.
            acceptable_bags.add(name)

        # We started with the given bag, but we assume bags can't hold themselves.
        acceptable_bags.remove(bag_name)

        return acceptable_bags

    def count_bags_in(self, bang_name):
        #TODO.
        pass

if __name__ == '__main__':
    DEBUG = False

    bagman = BagManager('./input.txt')
    print(len(bagman.find_bags_for('shiny gold')))
    # 370
