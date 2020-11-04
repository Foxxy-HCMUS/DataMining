import File as file

class ExcludeDuplicate:
    def ExcludeDuplicate(filename):

            oldList=file.RowFile.getInstance(filename).data.copy()
            newList = set(tuple(x) for x in oldList[1:])
            newList=sorted(newList)
            newList.insert(0,oldList[0])
            return newList
    pass

print(ExcludeDuplicate.ExcludeDuplicate("house-prices.csv")[0])