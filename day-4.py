with open("input-day-4.txt", "r") as f:
    lines = f.readlines()


counter = 0
for i in lines:
    pair = i.strip("\n")
    val = pair[::2]
    print(val)
    a = int(pair.split(",")[0].split("-")[0])
    b = int(pair.split(",")[0].split("-")[1])
    c = int(pair.split(",")[1].split("-")[0])
    d = int(pair.split(",")[1].split("-")[1])
    print(pair)
    if a >= c and d >= b:
        # print(a, b, c, d)
        counter += 1
    elif c >= a and b >= d:
        # print(a, b, c, d)
        counter += 1
# print(counter)


# part 2

counter = 0
for i in lines:
    pair = i.strip("\n")
    a = int(pair.split(",")[0].split("-")[0])
    b = int(pair.split(",")[0].split("-")[1])
    c = int(pair.split(",")[1].split("-")[0])
    d = int(pair.split(",")[1].split("-")[1])
    if a <= d and b >= c:
        counter += 1
print(counter)
