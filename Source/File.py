class MakeFile:
    @staticmethod
    def makeFile(filename, data):
        file = open(filename, 'w')
        for row in data:
            file.write(row[0])
            for i in range(1, len(row)):
                file.write(',' + str(row[i]))
            file.write('\n')
        file.close()

class DataFile:
    _df = None

    @staticmethod
    def getInstance(filename):
        if DataFile._df is None:
            DataFile._df = DataFile(filename)
        return DataFile._df

    def __init__(self, filename):
        self.filename = filename
        self.data = []

        file = open(filename, 'r')

        while True:
            row = file.readline().strip().split(',')
            if len(row) == 1:
                break

            row1 = []
            for item in row:
                try:
                    row1.append(float(item))
                except:
                    row1.append(item)

            self.data.append(row1)
        file.close()