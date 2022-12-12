with open("input-day-7.txt") as f:
    lines = f.readlines()

# print(lines)


class FileSytem:
    def __init__(self) -> None:
        self.dir_size = {}
        self.current_dir = ""

    def move_to_a_level(self, dir_name):
        if dir_name == "/":
            self.current_dir = dir_name
        elif dir_name == "..":
            self.move_out_one_level()
        else:
            self.current_dir += f"{dir_name}/"

        if self.dir_size.get(self.current_dir) == None:
            self.dir_size.update({self.current_dir: 0})
        print(f"Moving to level {self.current_dir}")

    @staticmethod
    def return_prev_level(path):
        return "".join([i + "/" for i in (path.split("/")[:-2])])

    def move_out_one_level(self):
        self.current_dir = "".join([i + "/" for i in (self.current_dir.split("/")[:-2])])
        # print(f"Moving out to {self.current_dir}")

    def add_size(self, size):
        print(f"add to {self.current_dir}, size {size}")
        self.dir_size[self.current_dir] += size
        cur_path = self.current_dir
        while cur_path != "/":
            prev_path = self.return_prev_level(cur_path)
            print(f"add to prev_path {prev_path}, size {size}")
            self.dir_size[prev_path] += size
            cur_path = prev_path


my_file_system = FileSytem()
for i in lines:
    i = i.strip("\n")
    if i.startswith("$ cd"):
        print(i)
        level = i.split(" ")[2]
        my_file_system.move_to_a_level(level)
    elif i[0].isdigit():
        print(i)
        file_size = int(i.split(" ")[0])
        my_file_system.add_size(file_size)

print(my_file_system.dir_size)

sorted_ls = [i for i in sorted(my_file_system.dir_size.values(), reverse=True) if i <= 100000]
print(sum(sorted_ls))

# part 2
total_space = 70000000
used_space = my_file_system.dir_size.get("/")
larger_than = used_space - total_space + 30000000
delete_ls = [i for i in sorted(my_file_system.dir_size.values()) if i >= larger_than]
print(delete_ls)
