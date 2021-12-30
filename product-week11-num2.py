import numpy as np                                                              # Shayan Montazeri - 99100925

demension_input = input().split()
rows = int(demension_input[0])
columns = int(demension_input[-1])

graph_input = ""
for x in range(rows):
    graph_input += input()
    
graph_input = list((graph_input))
graph_input = np.array(graph_input).reshape(rows, columns)

area = 0
for column in range(columns):
    for row in range(rows):
        if (graph_input[row][column] == "/") or (graph_input[row][column] == "\\"):
            area += (((rows - 1) - row) + (0.5))
            
        if graph_input[row][column] == "_":
            area += ((rows - 1) - row)
            
print(area)











