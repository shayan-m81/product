input_string = input()                                                      # Shayan Montazeri - 99100925
characters_list = list()
numbers_list = list()
special_characters_list = list()
output_list = list()
output_string = ""

for char in input_string:
    if char.isdigit():
        numbers_list.append(char)
    elif not char.isalnum():
        special_characters_list.append(char)
    else:
        characters_list.append(char)


characters_list = sorted(characters_list, key=lambda v: (v.casefold(), v))

numbers_list = sorted(numbers_list)

special_characters_list = sorted(special_characters_list)
space_count = special_characters_list.count(" ")
del special_characters_list[: space_count]

output_list = special_characters_list + numbers_list + characters_list

for char in output_list:
    output_string += char

print(output_string)

