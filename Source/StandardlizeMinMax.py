import File as file



class StandardlizeMinMax:
    def CalculateMinMax(min_i,max_i,value):

        return (value-min_i)/(max_i-min_i)*(1-0)+0
        pass

    def StandardlizeMinMax(filename):
        oldList=file.ColumnFile.getInstance(filename).data.copy()
        a=[]
        b=[]
        for i in range(len(oldList)):
            newList=oldList[i][1:]
            isnumber=True
            j=0
            while j in range(len(newList)):
               if (newList[j]!=''):
                   if(type(newList[j])!=int and type(newList[j])!=float):
                       isnumber=False
                       break
               else :
                   newList.pop(j)
                   j-=1
               j+=1

            if isnumber==True:
                a=min(newList)
                b=max(newList)
                for j in range(1,len(oldList[i])):
                        if oldList[i][j]!='':
                            oldList[i][j]=StandardlizeMinMax.CalculateMinMax(a,b,oldList[i][j])


            pass


        pass

StandardlizeMinMax.StandardlizeMinMax('test.csv')
