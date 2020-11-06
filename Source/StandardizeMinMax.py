import File as file

class StandardizeMinMax:
    """Chuẩn hoá dữ liệu theo phương pháp Min-Max
    """

    @staticmethod
    def CalculateMinMax(min_i, max_i, value):
        """tính toán giá trị mới của value đầu vào

        Args:
            min_i (int): giá trị min cũ của value
            max_i (int): giá trị max cữ của value
            value (float): giá trị cần chuẩn hoá

        Returns:
            float: giá trị sau khi chuẩn hoá theo thang [0, 1]
        """
        return (value-min_i)/(max_i-min_i)*(1-0)+0

    @staticmethod
    def StandardizeMinMax(fileIn, fileOut):
        """chuẩn hoá giá trị số trong file fileIn
        Xuất kết quả ra file fileOut

        Args:
            fileIn (string): tên file đầu vào
            fileOut (string): tên file đầu ra

        Returns:
            list: trả về data của file mới ở dạng cột 
        """

        # Đọc data theo cột, mỗi cột là 1 attribute
        oldList = file.ColumnFile.getInstance(fileIn).data.copy()

        for i in range(len(oldList)):

            # Lấy data cột đó mà không có header
            newList = oldList[i][1:]

            # Kiểm tra xem attb có phải nummeric không
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
                        oldList[i][j] = StandardizeMinMax.CalculateMinMax(a, b, oldList[i][j])

        file.MakeFile.makeColumnFile(fileOut, oldList)
        return oldList


# StandardizeMinMax.StandardizeMinMax('./house-prices.csv', './min-max.csv')
