import numpy as np                                                                              # Shayan Montazeri - 99100925

dimension_input = input().split()
rows = int(dimension_input[0])
columns = int(dimension_input[-1])

graph_input = ""
for x in range(rows):
    graph_input += input()
    graph_input = graph_input.strip()

graph_input = list(graph_input)
graph_input = np.array(graph_input).reshape(rows, columns)

area = 0.0
for i in range(rows):
    for j in range(columns):
        if (graph_input[i][j] == "/") or (graph_input[i][j] == "\\"):
            area += (((rows - 1) - i) + (0.5))
        elif graph_input[i][j] == "_":
            area += (((rows - 1) - i) + 0.0)

print(area)