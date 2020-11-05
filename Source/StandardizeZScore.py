import File as file

class StandardizeZScore:
    def StandardizeZScore(filename):
        oldList = file.ColumnFile.getInstance(filename).data.copy()
        a = []
        b = []
        for i in range(len(oldList)):
            newList = oldList[i][1:]
            isNumber = True
            j = 0
            while j in range(len(newList)):
                if (newList[j] != ''):
                    if(type(newList[j]) != int and type(newList[j]) != float):
                        isNumber = False
                        break
                else:
                    newList.pop(j)
                    j -= 1
                j += 1

            if isNumber == True:
                if len(newList) == 0:
                    continue
                mean = sum(newList)/len(newList)
                var = 0
                for j in range(len(newList)):
                    var += (newList[j]-mean)**2
                var = var/(len(newList)-1)
                var = var**(1/2)
                if var == 0:
                    continue
                for j in range(1, len(oldList[i])):
                    if oldList[i][j] != '':
                        oldList[i][j] = (oldList[i][j]-mean)/var

        file.MakeFile.makeColumnFile('./z.csv', oldList)


# StandardizeZScore.StandardizeZScore('house-prices.csv')
StandardizeZScore.StandardizeZScore('test.csv')
