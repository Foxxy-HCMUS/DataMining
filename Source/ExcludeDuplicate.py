import File as file

class ExcludeDuplicate:
    def ExcludeDuplicate(filename):

            oldList=file.RowFile.getInstance(filename).data.copy()
            newList = set(tuple(x) for x in oldList)
            list(newList)
            return newList


    pass






ExcludeDuplicate.ExcludeDuplicate("house-prices.csv")