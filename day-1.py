with open("input-day-1.txt") as f:
    lines = f.readlines()

lines.append("\n")
counter = 0
sum_cals = []
for i in lines:
    if i == "\n":
        sum_cals.append(counter)
        counter = 0
    else:
        cal = int(i.strip("\n"))
        counter += cal
        # print(counter)

sorted_cals = sorted(sum_cals, reverse=True)
print(sorted_cals[0:3])
max_three = sum(sorted_cals[0:3])
print(max_three)
