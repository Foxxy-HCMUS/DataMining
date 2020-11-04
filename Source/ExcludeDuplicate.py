import File as file

class ExcludeDuplicate:
    def ExcludeDuplicate(filename):
        oldList=file.RowFile.getInstance(filename).data.copy()
        # print(oldList[1])
        newList = set(tuple(x) for x in oldList[1:])
        newList=sorted(newList)
        newList.insert(0,oldList[0])
        return newList

# list = ExcludeDuplicate.ExcludeDuplicate("test.csv")
# for row in list:
#     print(row)