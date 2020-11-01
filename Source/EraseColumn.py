import File as file 

class EraseColumn:
    @staticmethod
    def eraseColumn(filename, rate):
        """
        xoá các cột bị thiếu dữ liệu với tỷ lệ cho trước
        xuất kết qủa sau khí xoá ra file đích
        """
        data = file.DataFile.getInstance(filename).data.copy()
        i = 0
        while i < len(data[0]):
        # for i in range(len(data[0])):
            count = 0
            for j in range(len(data)):
                if data[j][i] == '':
                    count += 1

            if count/(len(data)-1) >= rate:
                for k in range(len(data)):
                    del data[k][i]
                i -= 1

            i += 1

        file.MakeFile.makeFile('afterColumnErasing.csv', data)