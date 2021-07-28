'''
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

 

Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]
 

Note:

1 <= n <= 1000

'''

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        sol = [1]
        while len(sol) < n:
            sol = [i * 2 - 1 for i in sol] + [i * 2 for i in sol]
        
        return [i for i in sol if i <= n]
        
