/*
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> seen = new HashMap<>();
        for (int j = 0, i = 0; j < n; j++) {
            if (seen.containsKey(s.charAt(j))) {
                i = Math.max(i, seen.get(s.charAt(j)));
            }
            ans = Math.max(ans, j - i + 1);
            seen.put(s.charAt(j), j + 1);
        }
        
        return ans;
    }
}

