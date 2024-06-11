class Solution:
    def heightChecker(self, height: List[int]) -> int:
        index_list=[]
        sorted_list=sorted(height)
        for indx in range(len(height)):
            if height[indx]!=sorted_list[indx]:
                index_list.append(indx)
        
        return len(index_list)
            
    
    
c1=Solution()
print(c1.heightChecker([1,1,4,2,1,3]))
c2=Solution()
print(c2.heightChecker([5,1,2,3,4]))
c3=Solution()
print(c3.heightChecker([1,2,3,4,5]))
        