
class Matrix:
    matrix = (
        [1, 0, 0, 0, 0],
        [1.22174, 1, 0, 0, 0],
        [0.752, 0, 1, 0, 0],
        [1.10839, 0, 0, 1, 0],
        [0.67425, 0, 0, 0, 1]
    )

    def __init__(self):

        pass

    def fillFirstLine(self, idx):
        value = 1 / self.matrix[idx][0]
        self.matrix[0][idx] = float(format(value, '.5f'))

    def fillLines(self, idx):
        i = 1
        while i < len(self.matrix[idx]):
            if (self.matrix[idx][i] != 1):
                value =  self.matrix[0][i] * self.matrix[idx][0]
                self.matrix[idx][i] = float(format(value, '.5f'))
            i += 1
    
    def descMatrix(self, countries):
        i = 0
        s = 0
        if len(countries) > 1:
            print("\t", end = '')
            for name in countries:
                print(str(name) + "\t", end = '')
            print()
        while i < len(self.matrix) - 1:
            s = 0
            if len(countries) > 1:
                print(countries[i] + "\t", end = '')
            while s < len(self.matrix[i]) - 1:
                print(str(self.matrix[i][s]) + "\t", end = '')
                s += 1
            print()
            i += 1