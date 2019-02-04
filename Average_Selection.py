class AverageSelection(object):
    def __init__ (self, arr):
        self.arr=arr
        
    def partition(self,first,last):
        pivot=self.arr[int(last/2)]
        pivot_small=[]
        pivot_big=[]
        selection_arr=[]
        
        for i in self.arr:
            if(pivot>i):
                pivot_small.append(i)
            elif(pivot<i):
                pivot_big.append(i)

        for j in pivot_small:
            selection_arr.append(j)

        pivot_index=len(selection_arr)
        selection_arr.append(pivot)

        for k in pivot_big:
            selection_arr.append(k)

        self.arr[first:last]=selection_arr

        return pivot_index
    
    def select (self,first,last,search_num): #i=i번째로 작음
        if(first>last):
            print("Wrong call") #Wrong Call
            return -1

        pivot_index=self.partition(first,last)
        locate=pivot_index-first+1

        if(search_num<locate):
            return select(self,first,pivot_index-1,search_num)
        elif(search_num==locate):
            return self.arr[pivot_index]
        else:
            return select(self,pivot_index+1,last,search_num-locate)
        


test_list=list([31,8,48,73,11,3,20,29,65,15])
average_selection=AverageSelection(test_list)
print(average_selection.select(0,9,3))
        
        
