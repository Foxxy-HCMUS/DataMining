import File as file

class StandardizeZScore:
    @staticmethod
    def StandardizeZScore(fileIn, fileOut,attrb):
        """chuẩn hoá dữ liệu dạng số bằng phương pháp z-scores

        Args:
            fileIn (string): tên file chứa data đầu vào
            fileOut (string): tên file chứa data đầu ra

        Returns:
            list: chứa data sau khi được chuẩn hoá ở dạng cột
        """

        #Đọc data theo cột, mỗi cột là 1 attribute
        oldList = file.ColumnFile.getInstance(fileIn).data.copy()

        find = False
        for i in range(len(oldList)):
            if oldList[i][0]==attrb:
                find = True
                break

        if find == False:
            print("Không tồn tại thuộc tính bạn yêu cầu")
            return None

        # Lấy data cột đó mà không có header
        newList = oldList[i][1:]

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

        if len(newList)==0:
            print("Thuộc tính bạn yêu cầu không có giá trị")
            return None

        if isNumber == False:
            print("Thuộc tính bạn yêu cầu có giá trị không phải số")
            return None



        #Tính trung bình
        mean = sum(newList)/len(newList)

        #Tính độ lệch chuẩn (n)
        var = 0
        for j in range(len(newList)):
            var += (newList[j]-mean)**2

        var = var/(len(newList))
        var = var**(1/2)

        # Nếu độ lệch chuẩn bằng 0 thì tất cả các giá trị trong thuộc tình đều bằng mean
        if var == 0:
            for j in range(1, len(oldList[i])):
                if oldList[i][j] != '':
                    oldList[i][j] = mean
            print("Chuẩn hóa thành công")
            return oldList

        for j in range(1, len(oldList[i])):
            if oldList[i][j] != '':
                oldList[i][j] = (oldList[i][j]-mean)/var

        file.MakeFile.makeColumnFile(fileOut, oldList)
        print("Chuẩn hóa thành công")
        return oldList


StandardizeZScore.StandardizeZScore('./house-prices.csv', 'z.csv','Street')
