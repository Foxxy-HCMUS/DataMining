class MakeFile:
    @staticmethod
    def makeRowFile(filename, data):
        """tạo file từ dữ liệu được lưu theo từng dòng.
        Chỉ cần ghi từng dòng lên file

        Args:
            filename (string): tên file output
            data (list): dữ liệu của file
        """
        file = open(filename, 'w')
        for row in data:
            file.write(str(row[0]))
            for i in range(1, len(row)):
                file.write(',' + str(row[i]))
            file.write('\n')
        file.close()

    @staticmethod
    def makeColumnFile(filename, data):
        """tạo file từ dữ liệu được lưu theo từng cột

        Args:
            filename (string): tên file output
            data (list): dữ liệu của file
        """
        rowData = []
        for i in range(len(data[0])):
            rowData.append([])

        for i in range(len(data)):
            for j in range(len(data[0])):
                rowData[j].append(data[i][j])

        MakeFile.makeRowFile(filename, rowData)

class RowFile:
    """
    lưu file ở dạng dòng
    singleton implementation
    lấy data bằng cách gọi hàm getInstance()
    """
    _df = None

    @staticmethod
    def getInstance(filename):
        """trả về 1 instance của RowFile (chứa dữ liệu của file ở dạng row)

        Args:
            filename (string): tên file

        Returns:
            RowFile: đối tượng chứa dữ liệu của file theo dòng
        """
        if RowFile._df is None:
            RowFile._df = RowFile(filename)
        return RowFile._df

    def __init__(self, filename):
        self.filename = filename
        self.data = []

        file = open(filename, 'r')

        while True:
            row = file.readline().strip().split(',')
            if len(row) == 1:
                break

            row1 = []
            for item in row:
                try:
                    row1.append(float(item))
                except:
                    row1.append(item)

            self.data.append(row1)
        file.close()

class ColumnFile:
    """
    lưu file ở dạng cột
    singleton implementation
    lấy data bằng cách gọi hàm getInstance()
    """
    _cf = None 

    @staticmethod
    def getInstance(filename):
        """trả về 1 instance của ColumnFile (chứa dữ liệu của file ở dạng column)

        Args:
            filename (string): tên file

        Returns:
            ColumnFile: đối tượng chứa dữ liệu của file theo cột
        """
        if ColumnFile._cf is None:
            ColumnFile._cf = ColumnFile(filename)
        return ColumnFile._cf

    def __init__(self, filename):
        data = RowFile.getInstance(filename).data.copy()
        self.data = []
        self.filename = filename
        for i in range(len(data[0])):
            self.data.append([])

        for row in data:
            i = 0
            while i < len(data[0]):
                self.data[i].append(row[i])
                i += 1

def process_distance(arr):
    if len(arr)==0: 
        return [0,0]
    
    count=0
    for i in range(len(arr)):
        if(arr[i][1]=='TRUE'):
            count+=1
        
    return [count/len(arr)*100,len(arr),arr[0][0],arr[-1][0]]
    #return [count/len(arr)*100,len(arr)]


def getChurn(filename, attribute, bin):
    list =[]

    columnFile = ColumnFile.getInstance(filename).data.copy()

    realColumn = None
    for column in columnFile:
        if column[0] == attribute:
            realColumn = column
            break

    del realColumn[0]
    #print(realColumn)
    pair=[]
    for i in range(len(realColumn)):
        pair.append([realColumn[i],columnFile[-1][i+1]])
    pair.sort()
    print(len(pair))


    result=[]
    range_value=pair[-1][0]-pair[0][0]
    distance = range_value/bin
    curr_point=0
    curr_sum=pair[0][0]
    for i in range(len(pair)):
        if pair[i][0]>=curr_sum+distance:
            if (i==len(pair)-1):
                result.append(process_distance(pair[curr_point:]))
            else:
                result.append(process_distance(pair[curr_point:i]))
            curr_point=i
            curr_sum=curr_sum+distance

    for i in result:
        print(i)

def nominal_class(filename,attribute):
    columnFile = ColumnFile.getInstance(filename).data.copy()

    realColumn = None
    for column in columnFile:
        if column[0] == attribute:
            realColumn = column
            break

    del realColumn[0]
    #print(realColumn)
    pair=[]
    for i in range(len(realColumn)):
        pair.append([realColumn[i],columnFile[-1][i+1]])
    pair.sort()
    result=[]
    
    for i in range(len(pair)-1):
        if(pair[i][0]!=pair[i+1][0]) :
            result.append(process_distance(pair[0:i+1]))
            point=i+1
            break
    result.append(process_distance(pair[point:]))
    result[0].pop(3)
    result[1].pop(3)
    print(result[0])
    print(result[1])


attribute = input('Enter attribute: ')
bin = int(input('Num of bin: '))
# nominal_class('../Requirement/churn.csv', attribute)
getChurn('../Requirement/churn.csv', attribute, bin)
