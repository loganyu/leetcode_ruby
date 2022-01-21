/*
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
*/

impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, mut n: i32) -> bool {
        let mut i = 0;
        let len = flowerbed.len();
        for i in 0..len {
            if n == 0 { break; }
            
            
            if flowerbed[i] == 1 || (i > 0 && flowerbed[i-1] == 1) || (i < len - 1 && flowerbed[i+1] == 1) {
                continue;

            }
            flowerbed[i] = 1;
            n -= 1
        }
            
        n == 0
    }
}

