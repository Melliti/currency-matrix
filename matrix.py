class Matrix:
    # Sample matrix used id user did not submit a csv
    matrix = (
        [1, 0, 0, 0, 0],
        [1.22174, 1, 0, 0, 0],
        [0.752, 0, 1, 0, 0],
        [1.10839, 0, 0, 1, 0],
        [0.67425, 0, 0, 0, 1]
    )

    # First method called. Using first pair currency values, fill the
    # first row of currencies
    def fillFirstRow(self, idx):
        value = 1 / self.matrix[idx][0]
        self.matrix[0][idx] = float(format(value, '.5f'))
        idx += 1
        self.fillFirstRow(idx)


    # second method called. Using the first column and the first row,
    # fill every row from left to the right
    def fillRows(self, idx):
        i = 1
        while i < len(self.matrix[idx]):
            if (self.matrix[idx][i] != 1):
                value =  self.matrix[0][i] * self.matrix[idx][0]
                self.matrix[idx][i] = float(format(value, '.5f'))
            i += 1
        idx += 1
        self.fillRows(idx)
    
    # Print matrix values
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