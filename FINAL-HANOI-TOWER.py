# to inputs disk_numbers and steps_count
first_input = input().split()
disk_number = int(first_input[0])
rows_count = disk_number + 3
columns_count = 3
shape_list = []

# these 4 for loops are to fill rows of my shape based on disk_numbers
for row in range(rows_count):
    shape_list.append(["", "", ""])

for row in range(rows_count - 1):
    for column_number in range(columns_count):
        shape_list[row][column_number] = "||"

for column_number in range(columns_count):
    shape_list[rows_count - 1][column_number] = "-" * 20

for disk in range(disk_number):
    shape_list[2 + disk][0] = "==" * (i + 1)

shape_list.append(["Tower #0", "Tower #1", "Tower #2"])


# this def will draw my shape
def print_shape():
    for row in shape_list:
        for character in row:
            print(character.center(20, " "), end=" ")
        print("")


# this def will find the number of row that i should make change in, for each columns
def top(column):
    for row in range(rows_count):
        if shape_list[row][column][0] == "=":
            return row
        elif row == rows_count - 1:
            return row


steps = int(first_input[-1])
print_shape()

# to change the position of disks for each move based the inputs
for step in range(steps):
    command = list(input())
    column1 = int(command[0])
    column2 = int(command[-1])
    shape_list[top(column1)][column1], shape_list[top(column2) - 1][column2] = \
        shape_list[top(column2) - 1][column2], shape_list[top(column1)][column1]
    print_shape()
