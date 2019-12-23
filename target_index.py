class TargetIndex:
    def inputData(self):
        self.num_list=list(map(int,input("Input:").split()))
        self.target=int(input("Target:"))
    def searchIndex(self):
        result=False
        for i in range(len(self.num_list)):
                temp=self.target-self.num_list[i]
                if temp in self.num_list:
                    result=True
                    result_index=[i,self.num_list.index(temp)]
                    break

        if result:
            print("Output"+str(result_index))
        else:
            print("No search.")

def main():
    targetIndex=TargetIndex()
    targetIndex.inputData()
    targetIndex.searchIndex()


if __name__=="__main__":
     main()
    

