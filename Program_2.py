"""
Time Complexity: 
Space Complexity: 

Problem_1: Two Sum Problem
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

# Approach - 1: nested iteration, by taking each element at a time and finding the other element in the rest array
# TC: O(N^2), O(1)

# Approach - 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Using hashmap to map each element and its index
        Time Complexity : O(n)
        Space Complexity : O(n)
        """
        if len(nums) <= 1: return 0
        
        map_index = {}
        res = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map_index:
                res.append(i)
                res.append(map_index.get(diff))
                return res
            else:
                map_index[nums[i]] = i
                
        return -1
        

