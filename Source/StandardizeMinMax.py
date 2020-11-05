import File as file

class StandardizeMinMax:
    def CalculateMinMax(min_i, max_i, value):
        return (value-min_i)/(max_i-min_i)*(1-0)+0

    def StandardizeMinMax(filename):
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
                a = min(newList)
                b = max(newList)
                for j in range(1, len(oldList[i])):
                    if oldList[i][j] != '':
                        oldList[i][j] = StandardizeMinMax.CalculateMinMax(
                            a, b, oldList[i][j])

        file.MakeFile.makeColumnFile('./min-max.csv', oldList)


StandardizeMinMax.StandardizeMinMax('test.csv')
