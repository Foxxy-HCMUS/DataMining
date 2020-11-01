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
    """
    lưu file ở dạng dòng
    singleton implementation
    lấy data bằng cách gọi hàm getInstance()
    """
    _df = None

    @staticmethod
    def getInstance(filename):
        """
        trả về dữ liệu của file ở dạng list
        """
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

class ColumnFile:
    """
    lưu file ở dạng cột
    """
    _cf = None 

    @staticmethod
    def getInstance(filename):
        """
        trả về dữ liệu của file ở dạng list, tổng hợp theo cột
        """
        if ColumnFile._cf is None:
            ColumnFile._cf = ColumnFile(filename)
        return ColumnFile._cf

    def __init__(self, filename):
        data = DataFile.getInstance(filename).data.copy()
        self.data = []
        self.filename = filename
        for i in range(4):
            self.data.append([])

        for row in data:
            i = 0
            while i < len(data[0]):
                self.data[i].append(row[i])
                i += 1