import string

letter2num = dict(zip(string.ascii_lowercase, range(1, 27)))
letter2num.update(dict(zip(string.ascii_uppercase, range(27, 53))))

with open("input-day-3.txt", "r") as f:
    lines = f.readlines()

counter = 0
for rucksack in lines:
    items = rucksack.strip("\n")
    cut_off = int(len(items) / 2)
    first_half = items[:cut_off]
    second_half = items[cut_off:]
    overlaps = set([i for i in first_half if i in second_half])
    for i in overlaps:
        counter += letter2num.get(i)
# print(counter)

## part 2

counter_group = 0
counter_bagdes = 0
for rucksack in lines:
    counter_group += 1
    items = rucksack.strip("\n")
    if counter_group == 1:
        first_items = items
    elif counter_group == 2:
        overlaps = set([i for i in items if i in first_items])
    elif counter_group == 3:
        overlaps = set([i for i in items if i in overlaps])
        counter_group = 0
        counter_bagdes += letter2num.get(list(overlaps)[0])
print(counter_bagdes)
