disk_number = int(input())
shape_list = []

for x in range(disk_number + 3):
    shape_list.append(["", "", "", ""])

for x in range(disk_number + 2):
    for y in range(3):
        shape_list[x][y] = "||"

for x in range(3):
    shape_list[disk_number + 2][x] = "-" * 20

for i in range(disk_number):
    shape_list[disk_number + 1 - i][0] = "==" * (disk_number - i)
shape_list.append(["Tower #0", "Tower #1", "Tower #2"])


def print_shape():
    for f in range(len(shape_list) * 4):
        if (f % 4) != 3:
            print(shape_list[f // 4][f % 4].center(20, " "), end="")
            print(" ", end="")
        else:
            print("")


def top(column):
    for g in range(disk_number + 3):
        if shape_list[g][column][0] == "=":
            return g
        elif g == disk_number + 2:
            return disk_number + 2


steps = int(input())
print_shape()
for x in range(steps):
    command = list(input())
    column1 = int(command[0])
    column2 = int(command[-1])
    shape_list[top(column1)][column1], shape_list[top(column2) - 1][column2] = \
        shape_list[top(column2) - 1][column2], shape_list[top(column1)][column1]
    print_shape()
    print("kosse kharet")
