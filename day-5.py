class Pile:
    def __init__(self, num_stacks) -> None:
        self.pile = list()
        self.num_stacks = num_stacks
        for i in range(num_stacks):
            self.pile.append([])

    def add_item_to_stack(self, stack_index, item):
        self.pile[stack_index].append(item)

    def move_items(self, move_num, from_num, to_num):
        for i in range(move_num):
            to_add = self.pile[from_num].pop()
            self.add_item_to_stack(stack_index=to_num, item=to_add)

    def move_items_part_two(self, move_num, from_num, to_num):
        to_add = self.pile[from_num][-move_num:]
        del self.pile[from_num][-move_num:]
        self.pile[to_num].extend(to_add)

    def get_top_item(self, stack_index):
        return self.pile[stack_index][-1]

    def show(self):
        print(self.pile)

    def show_top_numbers(self):
        for i in range(self.num_stacks):
            print(self.get_top_item(i))


with open("input-day-5.txt", "r") as f:
    lines = f.readlines()
piles_lines = lines[0:10]
move_lines = lines[10:]
# parsing each line and adding item to the stack as instructed
elf_pile = Pile(9)
for i in range(7, -1, -1):
    row = piles_lines[i]
    for x in range(0, 36, 4):
        if row[x] == "[":
            to_add = row[x + 1]
            stack_index = int(x / 4)
            elf_pile.add_item_to_stack(stack_index, to_add)


for i in move_lines:
    i = i.strip("\n")
    i = i.split(" ")
    move_num = int(i[1])
    from_num = int(i[3]) - 1
    to_num = int(i[5]) - 1
    elf_pile.move_items_part_two(move_num, from_num, to_num)

elf_pile.show()
elf_pile.show_top_numbers()
# print(move_lines)
