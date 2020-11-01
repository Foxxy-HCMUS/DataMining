import File as file 

class EraseRow:
    @staticmethod
    def eraseRow(filename, rate):
        """
        xoá các dòng bị thiếu dữ liệu với tỉ lệ cho trước
        xuất kết quả sau khi xoá ra file đích
        """
        data = file.DataFile.getInstance(filename).data.copy()
        i = 0
        while i < len(data):
            count = 0
            for j in range(len(data[i])):
                print(data[i][j], i, j)
                if data[i][j] == '':
                    count += 1

            if count/len(data[i]) >= rate:
                del data[i]
                i -= 1

            i += 1

        file.MakeFile.makeFile('afterRowErasing.csv', data)