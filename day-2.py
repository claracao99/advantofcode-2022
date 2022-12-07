class RockPaperScissors:
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        if self.symbol in ["A", "X"]:
            self.gesture = "Rock"
            self.point = 1
        elif self.symbol in ["B", "Y"]:
            self.gesture = "Paper"
            self.point = 2
        elif self.symbol in ["C", "Z"]:
            self.gesture = "Scissors"
            self.point = 3


rules = [{"Rock": 0, "Paper": 6}, {"Paper": 0, "Scissors": 6}, {"Scissors": 0, "Rock": 6}]

# print(RockPaperScissors("A").gesture)


def get_win_point_part_1(opponent, me):
    opponent = RockPaperScissors(opponent)
    me = RockPaperScissors(me)

    if opponent.gesture == me.gesture:
        win_point = 3
    else:
        for comb in rules:
            gestures = comb.keys()
            if opponent.gesture in gestures and me.gesture in gestures:
                win_point = comb.get(me.gesture)
    # print(win_point)
    return win_point + me.point


def get_win_point(opponent, me):
    opponent = RockPaperScissors(opponent)
    me = RockPaperScissors(me)

    if opponent.gesture == me.gesture:
        win_point = 3
    else:
        for comb in rules:
            gestures = comb.keys()
            if opponent.gesture in gestures and me.gesture in gestures:
                win_point = comb.get(me.gesture)
    # print(win_point)
    return win_point


def get_win_point_part_2(opponent, results):
    gestures = ["A", "B", "C"]

    if results == "X":  # LOSE
        win_point = 0
    elif results == "Y":  # DRAW
        win_point = 3
    elif results == "Z":  # WIN
        win_point = 6

    for x in gestures:
        point = get_win_point(opponent, x)
        if point == win_point:
            me = RockPaperScissors(x)

    return win_point + me.point


with open("input-day-2.txt", "r") as f:
    lines = f.readlines()

# counter = 0
# for i in lines:
#     i = i.strip("\n")
#     opponent = i.split(" ")[0]
#     me = i.split(" ")[1]
#     counter += get_win_point(opponent, me)

# print(counter)

counter = 0
for i in lines:
    i = i.strip("\n")
    opponent = i.split(" ")[0]
    result = i.split(" ")[1]
    counter += get_win_point_part_2(opponent, result)

print(counter)
