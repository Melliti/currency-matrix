import sys
import matrix
import csvReader

def help():
    print("Usage:")
    print("[first case] ./matrix")
    print("\tIt will make a matrix with default values:")
    print("\t\tUSD: 1, GBP: 1.22174, CAD: 0.752, EUR: 1.10839, NZD: 0.67425\n")
    print("[second case] ./matrix <file.csv>")
    print("Matrix must be format as follow:")
    print("\t\tCurrenct, Value where first row must have a value of 1\n")

matrix = matrix.Matrix()
s = 1
i = 1
if (len(sys.argv) > 1):
    if(sys.argv[1] == "--help"):
        help()
        exit()
    if (sys.argv[1] != "--help"):
        csvReader = csvReader.csvReader()
        csvReader.extractCSVData(sys.argv[1], matrix.matrix)

while i < len(matrix.matrix):
    matrix.fillFirstLine(i)
    i += 1
while s < len(matrix.matrix):
    matrix.fillLines(s)
    s += 1
if (len(sys.argv) > 1):
    matrix.descMatrix(csvReader.countries)
else:
    matrix.descMatrix([])


# else:
    
    # print(matrix.matrix)