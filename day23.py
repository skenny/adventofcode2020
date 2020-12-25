import logging

logging.basicConfig(level=logging.INFO)

class circular_linked_list:

    def __init__(self, values):
        self.current = node(values[0])
        prev = self.current
        for value in values[1:]:
            new_node = node(value)
            self.insert_node(new_node, prev)
            prev = new_node

    def __repr__(self):
        this_current = self.current
        values = []
        while True:
            this_current_val = str(this_current.value)
            if this_current == self.current:
                values.append("({})".format(this_current_val))
            else:
                values.append(this_current_val)
            if (this_current.next is self.current):
                break
            this_current = this_current.next
        return " ".join(values)

    def next(self):
        self.current = self.current.next

    def insert_node(self, node, after):
        node.prev = after
        node.next = after.next
        node.next.prev = node
        after.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if self.current == node:
            self.current = node.next
        return node

    def find(self, value):
        this_current = self.current
        while True:
            #logging.debug("v={}, c={}".format(value,this_current))
            if this_current.value == value:
                return this_current
            if this_current.next == self.current:
                return None
            this_current = this_current.next

class node:

    def __init__(self, value):
        self.value = value
        self.prev = self
        self.next = self

    def __repr__(self):
        return str(self.value)

def test_circular_linked_list():
    ll = circular_linked_list([1,2,3,4,5,6,7,8,9])
    print("99?", ll.find(99))
    
    print(ll)
    for i in range(10):
        ll.next()
        print(ll)

    ll.insert_node(node(25), ll.find(4))
    print(ll)

    print(ll.remove_node(ll.current))
    print(ll)

    print(ll.remove_node(ll.find(7)))
    print(ll)

def play(cups_str, num_turns):
    cup_nums = [int(s) for s in cups_str]
    min_cup = min(cup_nums)
    max_cup = max(cup_nums)

    logging.debug("cups: {} (min={}, max={})".format(cup_nums, min_cup, max_cup))

    cups = circular_linked_list(cup_nums)

    for turn in range(num_turns):
        logging.debug("-- move {} --".format(turn + 1))
        logging.debug("cups:  {}".format(cups))

        current_cup = cups.current
        
        next_3 = []
        for i in range(3):
            next_3.append(cups.remove_node(current_cup.next))
        
        logging.debug("pick up: {}".format(", ".join([str(n) for n in next_3])))

        target_cup_value = current_cup.value - 1
        while True:
            if target_cup_value < min_cup:
                target_cup_value = max_cup
            target_cup = cups.find(target_cup_value)
            if target_cup:
                break
            target_cup_value -= 1

        logging.debug("destination: {}\n".format(target_cup_value))

        for i in range(3):
            cups.insert_node(next_3[i], target_cup)
            target_cup = next_3[i]
        
        cups.next()
    
    print("-- final --")
    print("cups:  {}".format(cups))

#test_circular_linked_list()
#play("389125467", 10)
#play("389125467", 100)
play("598162734", 100)