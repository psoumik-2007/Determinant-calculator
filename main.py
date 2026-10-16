def determinant(matrix_type):

    if matrix_type == "3x3":
        row1 = []
        row2 = []
        row3 = []

        matrix = [row1, row2, row3]

        for i in range(3):
            row1.append(int(input(f"Enter row 1, element {i+1}: ")))

        for i in range(3):
            row2.append(int(input(f"Enter row 2, element {i+1}: ")))

        for i in range(3):
            row3.append(int(input(f"Enter row 3, element {i+1}: ")))

        det = (
            row1[0] * (row2[1] * row3[2] - row2[2] * row3[1])
            - row1[1] * (row2[0] * row3[2] - row2[2] * row3[0])
            + row1[2] * (row2[0] * row3[1] - row2[1] * row3[0])
        )

        print("Matrix:", matrix)
        print("Determinant:", det)

    elif matrix_type == "2x2":
        row1 = []
        row2 = []

        matrix = [row1, row2]

        for i in range(2):
            row1.append(int(input(f"Enter row 1, element {i+1}: ")))

        for i in range(2):
            row2.append(int(input(f"Enter row 2, element {i+1}: ")))

        det = row1[0] * row2[1] - row1[1] * row2[0]

        print("Matrix:", matrix)
        print("Determinant:", det)

    else:
        print("This program only supports 2x2 and 3x3 matrices.")


matrix_type = input("Tell me your matrix type: ")
determinant(matrix_type)
