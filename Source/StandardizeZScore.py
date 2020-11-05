import File as file

class StandardizeZScore:
    def StandardizeZScore(fileIn, fileOut):
        """chuẩn hoá dữ liệu dạng số bằng phương pháp z-scores

        Args:
            fileIn (string): tên file chứa data đầu vào
            fileOut (string): tên file chứa data đầu ra

        Returns:
            list: chứa data sau khi được chuẩn hoá ở dạng cột
        """

        #Đọc data theo cột, mỗi cột là 1 attribute
        oldList = file.ColumnFile.getInstance(fileIn).data.copy()

        for i in range(len(oldList)):
            newList = oldList[i][1:] #Lấy data cột đó mà không có header

            #Kiểm tra xem attb có phải nummeric không
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
                #Tính trung bình
                mean = sum(newList)/len(newList)

                #Tính độ lệch chuẩn (n)
                var = 0
                for j in range(len(newList)):
                    var += (newList[j]-mean)**2
                var = var/(len(newList))
                var = var**(1/2)

                if var == 0:
                    continue
                for j in range(1, len(oldList[i])):
                    if oldList[i][j] != '':
                        oldList[i][j] = (oldList[i][j]-mean)/var

        file.MakeFile.makeColumnFile(fileOut, oldList)
        return oldList


# StandardizeZScore.StandardizeZScore('house-prices.csv')
StandardizeZScore.StandardizeZScore('test.csv', 'z.csv')
