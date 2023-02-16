

import random
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('savedfile.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some data headers.
worksheet.write('A1', 'Column 1', bold)
worksheet.write('B1', 'Column 2', bold)
worksheet.write('C1', 'Column 3', bold)
worksheet.write('D1', 'Column 4', bold)
worksheet.write('E1', 'Column 5', bold)
worksheet.write('F1', 'Column 6', bold)
worksheet.write('G1', 'Column 7', bold)
worksheet.write('H1', 'Column 8', bold)
worksheet.write('I1', 'Column 9', bold)
worksheet.write('J1', 'Column 10', bold)

# Start from the first cell below the headers.
row = 1
col = 0

# Generate 100 random numbers and write them to the worksheet.
for i in range(100):
    worksheet.write(row, col,     random.randint(1, 100))
    worksheet.write(row, col + 1, random.randint(1, 100))
    worksheet.write(row, col + 2, random.randint(1, 100))
    worksheet.write(row, col + 3, random.randint(1, 100))
    worksheet.write(row, col + 4, random.randint(1, 100))
    worksheet.write(row, col + 5, random.randint(1, 100))
    worksheet.write(row, col + 6, random.randint(1, 100))
    worksheet.write(row, col + 7, random.randint(1, 100))
    worksheet.write(row, col + 8, random.randint(1, 100))
    worksheet.write(row, col + 9, random.randint(1, 100))
    row += 1

# Close the workbook.
workbook.close()