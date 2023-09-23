/*
 * You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
*/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32) -> i32 {
              let len = nums.len();
        let total: i32 = nums.iter().sum();
        let target = total - x;
        let mut res: i32 = -1;
        let mut current_v = 0;
        let mut left = 0;
        for right in 0..len {
            current_v += nums[right];
            while current_v > target && left <= right {
                current_v -= nums[left];
                left += 1;
            }
            if current_v == target {
                res = std::cmp::max(res, (right - left + 1) as i32);
            }
        }
        if res == -1 {
            return -1;
        } else {
            return len as i32 - res;
        }
    }
}

