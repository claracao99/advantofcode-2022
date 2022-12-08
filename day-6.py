with open("input-day-6.txt") as f:
    lines = f.readlines()


# part 2

hold_ls = []
counter = 0
start_point = 14

for i in lines[0]:
    if len(hold_ls) == start_point:
        break
    else:
        if i in hold_ls:
            index = hold_ls.index(i)
            del hold_ls[: index + 1]
        hold_ls.append(i)
        counter += 1
print(counter)
