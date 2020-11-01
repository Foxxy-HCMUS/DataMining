import File as file

class CountMissingDataRow:
    @staticmethod
    def countMissingDataRow(filename):
        count = 0
        data = file.DataFile.getInstance(filename).data
        header = data[0]

        for row in data:
            if '' in row:
                count += 1
        return count