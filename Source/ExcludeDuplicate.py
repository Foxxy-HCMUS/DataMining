import File as file

class ExcludeDuplicate:
    def ExcludeDuplicate(fileIn, fileOut):
        """Loại bỏ dòng trùng lặp trong dataset

        Args:
            fileIn (string): tên file chứa data đầu vào
            fileOut (string): tên file chứa data đầu ra

        Returns:
            list: chứa data đầu ra ở dạng list các dòng
        """
        # Đọc data theo dòng, mỗi dòng là 1 attribute
        oldList=file.RowFile.getInstance(fileIn).data.copy()

        #Dùng tính chất của set để loại bỏ trùng lặp
        newList = set(tuple(x) for x in oldList[1:])
        newList=list(list(x)for x in newList)

        #Ép kiểu về List
        newList=sorted(newList)

        #Add header vào data
        newList.insert(0,oldList[0])

        # tạo file
        file.MakeFile.makeRowFile(fileOut, newList)

        return newList

ExcludeDuplicate.ExcludeDuplicate("house-prices.csv")