class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list=[]
        for index1 in range(len(nums)):
            for index2 in range(index1+1,len(nums)):
                if nums[index1]+nums[index2]==target:
                    index_list.append(index1)
                    index_list.append(index2)
            if len(index_list)==2:
                break
        return index_list


c1=Solution()
print(c1.twoSum([1,2,3,4,5,6,7,8,9],15))