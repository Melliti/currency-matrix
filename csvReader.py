import csv

class csvReader:
    counter = 0
    countries = []

    def __lengthErrorMessage(self):
        print("CSV must be formatted as follow:")
        print("\n\t[currency, value] where first value = 1")
        print("\t[currency, value]")
        print("\t[currency, value]")
        print("\t[currency, value]")

    def __initialValueErrorMessage(self):
        print("CSV must be formatted as follow:")
        print("\n\t[currency, value] where first value = 1")

    def __addValueInMatrix(self, matrix, value):
        matrix[self.counter][0] = round(float(value[1].strip()), 4)
        if (matrix[0][0] != 1):
            print(matrix[0][0])
            self.__initialValueErrorMessage()
            exit()
        self.countries.append(value[0])
        self.counter += 1

    def extractCSVData(self, filename, matrix):
        with open(filename, 'r') as csvFile:
            datas = csv.reader(csvFile, delimiter=",")
            for row in datas:
                if (len(row) != 2):
                    self.__errorMessage()
                    exit()
                else:
                    self.__addValueInMatrix(matrix, row)
        return (self.countries)

        pass