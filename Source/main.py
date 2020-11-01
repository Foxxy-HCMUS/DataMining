import File as file
from ListMissingDataColumn import ListMissingDataColumn as lc
from CountMissingDataRow import CountMissingDataRow as cr
from EraseRow import EraseRow as er
from EraseColumn import EraseColumn as ec

if __name__ == '__main__':
    filename = 'test.csv'
    df = file.DataFile.getInstance(filename)
    print(df.data)

    # print(lc.listMissingDataColumn(filename))
    # print(cr.countMissingDataRow(filename))

    # er.eraseRow(filename, 0.1)
    # ec.eraseColumn(filename, 0.3)
