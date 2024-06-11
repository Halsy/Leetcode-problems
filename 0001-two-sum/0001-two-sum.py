class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                # Complement found, return the indices
                return [num_dict[complement], index]
            else:
                # Store the current number and its index
                num_dict[num] = index
        # Return empty list if no pair is found
        return []


c1=Solution()
print(c1.twoSum([1,2,3,4,5,6,7,8,9],15))