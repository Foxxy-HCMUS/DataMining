import File as file 

class EraseRow:
    @staticmethod
    def eraseRow(fileIn, rate, fileOut):
        """xoá dòng bị thiếu dữ liệu. sau khi xoá xong thì xuất ra file mới nếu cần

        Args:
            fileIn (string): tên file cần xoá dòng 
            rate (float): tỷ lệ dữ liệu thiếu tối thiểu để xoá
            fileOut (string): tên file kết quả
        """
        data = file.RowFile.getInstance(fileIn).data.copy()
        i = 0
        while i < len(data):
            count = 0
            for j in range(len(data[i])):
                if data[i][j] == '':
                    count += 1

            if count/len(data[i]) >= rate:
                del data[i]
                i -= 1

            i += 1

        file.MakeFile.makeRowFile(fileOut, data)
