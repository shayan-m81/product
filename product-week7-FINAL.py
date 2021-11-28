# to inputs disk_numbers and steps_count
first_input = input().split()     
disk_number = int(first_input[0])
shape_list = []

# these 4 fors are to fill rows of my shape based on disk_numbers
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


# this def will draw my shape 
def print_shape():
    for f in range(len(shape_list) * 4):
        if (f % 4) != 3:    # to consider first 3 indices of each row
            print(shape_list[f // 4][f % 4].center(20, " "), end="")    # to move on each row's indices
            print(" ", end="")
        else:
            print("")


# this def will find the number of row that i should make change in, for each columns
def top(column):
    for g in range(disk_number + 3):
        if shape_list[g][column][0] == "=":
            return g
        elif g == disk_number + 2:
            return disk_number + 2

        
steps = int(first_input[-1])
print_shape()

# to change the position of disks for each move based the inputs
for x in range(steps):
    command = list(input())
    column1 = int(command[0])
    column2 = int(command[-1])
    shape_list[top(column1)][column1], shape_list[top(column2) - 1][column2] = \
        shape_list[top(column2) - 1][column2], shape_list[top(column1)][column1]
    print_shape()
