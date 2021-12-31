import numpy as np                                                                                  # Shayan Montazeri - 99100925

equation_1 = input()
equation_2 = input()


def find_coefficient(equation_string):
    index_x = equation_string.index("x")
    index_y = equation_string.index("y")
    x_coefficient = int(equation_string[0: index_x])
    y_coefficient = int(equation_string[(index_x + 2): index_y])
    constant = int(equation_string[(index_y + 2): ])

    return np.array([x_coefficient, y_coefficient,constant])


coefficient_array = np.array([find_coefficient(equation_1)[0:2], find_coefficient(equation_2)[0:2]])
constant_array = np.array([find_coefficient(equation_1)[2], find_coefficient(equation_2)[2]]).reshape(2, 1)
inverse_coefficient_array = np.linalg.inv(coefficient_array)

output_matrix = np.matmul(inverse_coefficient_array, constant_array)

print("x = %.6f and y = %.6f" % (output_matrix[0], output_matrix[1]))















