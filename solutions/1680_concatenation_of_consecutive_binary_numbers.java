/*
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
 

Constraints:

1 <= n <= 105
*/

class Solution {
    public int concatenatedBinary(int n) {
        final int MOD = 1000000007;
        int length = 0;
        long result = 0;
        for (int i = 1; i <= n; i++) {
            if ((i & (i-1)) == 0) {
                length++;
            }
            result = ((result << length) | i) % MOD;
        }
        
        return (int) result;
    }
}

