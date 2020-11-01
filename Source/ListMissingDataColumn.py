import File as file

class ListMissingDataColumn:
    @staticmethod
    def listMissingDataColumn(filename):
        listColumn = set()
        data = file.DataFile.getInstance(filename).data
        header = data[0]

        for row in data:
            for i in range(len(row)):
                if row[i] == '':
                    listColumn.add(header[i])
        return listColumn