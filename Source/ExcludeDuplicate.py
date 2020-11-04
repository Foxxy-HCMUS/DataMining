import File as file

class ExcludeDuplicate:
    def ExcludeDuplicate(filename):
        """

            Loại bỏ trùng lặp
            Input: filename
            Output:List đã loại bỏ trùng lặp

        """
        # Đọc data theo dòng, mỗi dòng là 1 attribute
        oldList=file.RowFile.getInstance(filename).data.copy()

        #Dùng tính chất của set để loại bỏ trùng lặp
        newList = set(tuple(x) for x in oldList[1:])

        #Ép kiểu về List
        newList=sorted(newList)

        #Add header vào data
        newList.insert(0,oldList[0])

        return newList

