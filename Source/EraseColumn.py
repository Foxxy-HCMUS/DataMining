import File as file 

class EraseColumn:
    @staticmethod
    def eraseColumn(fileIn, rate, fileOut):
        """xoá cột bị thiếu dữ liệu. sau khi xoá xong thì xuất ra file csv mới nếu cần

        Args:
            fileIn (string): tên file cần xoá cột bị thiếu data
            rate (float): tỷ lệ thiếu data tối thiểu để xoá
            fileOut (string): tên file kết quả
        """
        data = file.ColumnFile.getInstance(fileIn).data.copy()
        i = 0
        while i < len(data):
            count = 0
            for j in range(len(data[i])):
                if data[i][j] == '': 
                    count += 1

            if count / len(data[i]) >= rate:
                del data[i]
                i -=1

            i += 1

        file.MakeFile.makeColumnFile(fileOut, data)


if __name__ == "__main__":
    EraseColumn.eraseColumn('./test.csv', 0.1, 'column.csv') 