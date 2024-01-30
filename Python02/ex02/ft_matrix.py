import sys

try:
	matrix = []
	sum_rows = []
	sum_col = []
	Row = int(sys.argv[1])
	Col = int(sys.argv[2])
	for row in range(Row):
		m_row = []
		for col in range(Col):
			m_row.append(float(input(f"Insert the element in position ({row} {col}): ")))
		matrix.append(m_row)
	print("The inserted matrix is:")
	for row in range(Row):
		print(matrix[row])
		sum_r = 0
		sum_c = 0
		for col in range(Col):
			sum_r+=matrix[row][col]
		sum_rows.append(sum_r)
	print(f"The sum over rows is:\n{sum_rows}")
	for col in range(Col):
		sum = 0
		for row in range(Row):
			sum+=matrix[row][col]
		sum_col.append(sum)
	print(f"The sum over columns is:\n{sum_col}")
except:
	print("Error! Usage: python3 ft_matrix <n> <m>")
