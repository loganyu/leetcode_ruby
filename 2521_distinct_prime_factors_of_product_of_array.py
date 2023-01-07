'''
Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.
Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.
 

Constraints:

1 <= nums.length <= 104
2 <= nums[i] <= 1000
'''

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_factors = set()
        for num in nums:
            current_prime_factors = self.get_prime_factors(num)
            prime_factors.update(current_prime_factors)
        
        return len(prime_factors)

    def get_prime_factors(self, num: int) -> set:
        prime_factors = set()
        
        while num % 2 == 0:
            prime_factors.add(2)
            num /= 2
        
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                prime_factors.add(i)
                num /= i
        
        if num > 2:
            prime_factors.add(num)
        
        return prime_factors

