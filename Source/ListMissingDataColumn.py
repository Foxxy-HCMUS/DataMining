import File as file

class ListMissingDataColumn:
    @staticmethod
    def listMissingDataColumn(filename):
        """liệt kê các cột bị thiếu dữ liệu

        Args:
            filename (string): tên file 

        Returns:
            set: danh sách các cột bị thiêú dữ liệu
        """
        listColumn = set()
        data = file.RowFile.getInstance(filename).data
        header = data[0]

        for row in data:
            for i in range(len(row)):
                if row[i] == '':
                    listColumn.add(header[i])
        return listColumn
