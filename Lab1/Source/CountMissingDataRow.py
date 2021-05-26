import File as file

class CountMissingDataRow:
    @staticmethod
    def countMissingDataRow(filename):
        """đếm số dòng bị thiếu dữ liệu

        Args:
            filename (string): tên file cần đếm

        Returns:
            int: số dòng bị thiếu dữ liệu
        """
        count = 0
        data = file.RowFile.getInstance(filename).data
        header = data[0]

        for row in data:
            if '' in row:
                count += 1
        return count
