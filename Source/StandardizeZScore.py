import File as file


class StandardizeZScore:

    def StandardizeZScore(filename):
        """

        Chuẩn hóa dữ liệu theo phương pháp ZScore: z=(z-mean)/s (n)
        Input: filename
        Output: List đã được chuẩn hóa

        """
        #Đọc data theo cột, mỗi cột là 1 attribute
        oldList = file.ColumnFile.getInstance(filename).data.copy()


        for i in range(len(oldList)):
            newList = oldList[i][1:] #Lấy data cột đó mà không có header

            #Kiểm tra xem attb có phải nummeric không
            isnumber = True
            j = 0
            while j in range(len(newList)):
                if (newList[j] != ''):
                    if(type(newList[j]) != int and type(newList[j]) != float):
                        isnumber = False
                        break
                else:
                    newList.pop(j)
                    j -= 1
                j += 1

            if isnumber == True:
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


        return oldList

        pass


StandardizeZScore.StandardizeZScore('test.csv')
