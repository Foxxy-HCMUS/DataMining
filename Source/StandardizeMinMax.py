import File as file


class StandardizeMinMax:
    """

    Chuẩn hóa dữ liệu theo phương pháp Min-Max: CalculateMinMax(min_i, max_i, value)
    Input: filename
    Output: List đã được chuẩn hóa

    """

    def CalculateMinMax(min_i, max_i, value):

        return (value-min_i)/(max_i-min_i)*(1-0)+0
        pass

    def StandardizeMinMax(filename):
        # Đọc data theo cột, mỗi cột là 1 attribute
        oldList = file.ColumnFile.getInstance(filename).data.copy()

        for i in range(len(oldList)):

            # Lấy data cột đó mà không có header
            newList = oldList[i][1:]

            # Kiểm tra xem attb có phải nummeric không
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
                a = min(newList)
                b = max(newList)
                for j in range(1, len(oldList[i])):
                    if oldList[i][j] != '':
                        oldList[i][j] = StandardizeMinMax.CalculateMinMax(a, b, oldList[i][j])

            pass

        return oldList
        pass


StandardizeMinMax.StandardizeMinMax('test.csv')
