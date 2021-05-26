import File as file

class FillMissingData:
    """điền dữ liệu thiếu vào file csv
    """
    def __init__(self, filename):
        self.data = file.ColumnFile.getInstance(filename).data.copy()

    def getMean(self, attribute):
        sum = 0
        count = 0
        for item in attribute:
            if not isinstance(item, str):
                count += 1
                sum += item
        return sum / count

    def getMedian(self, attribute):
        temp = []
        for item in attribute:
            if not isinstance(item, str):
                temp.append(item)

        temp.sort()
        if len(temp) % 2 == 1:
            return temp[len(temp)//2]
        return (temp[len(temp)//2] + temp[len(temp)//2+1])/2

    def getMode(self, attribute):
        countData = {}
        for i in range(1, len(attribute)):
            if attribute[i] != '':
                countData[attribute[i]] = countData.get(attribute[i], 0) + 1

        max = -1
        mode = None
        for item in countData:
            if countData[item] > max:
                max = countData[item]
                mode = item

        return mode

    def fillColumnData(self, attribute, kind):
        """điền data còn thiếu cho cột bằng cách sử dụng mean, median hoặc mode
        Nếu là thuộc tính số thì chỉ có thể là median hoặc mean. thuộc tính định danh thì là mode

        Args:
            attribute (list): 1 cột dữ liệu trong tập dữ liệu
            kind (string): 'mean' hoặc 'median'
        """
        value = None
        if kind == 'mean':
            try:
                value = self.getMean(attribute)
            except:
                value = self.getMode(attribute)
        elif kind == 'median':
            try:
                value = self.getMedian(attribute)
            except:
                value = self.getMode(attribute)
        else:
            print('wrong format')
            return

        # for item in attribute:
        for i in range(1, len(attribute)):
            if attribute[i] == '': 
                attribute[i] = value

    def fillDataFile(self, kind, fileOut):
        """điền dữ liệu còn thiếu cho full file

        Args:
            kind (string): 'mean' hoặc 'median'
        """
        for column in self.data:
            if '' in column:
                self.fillColumnData(column, kind)

        file.MakeFile.makeColumnFile(fileOut, self.data)
