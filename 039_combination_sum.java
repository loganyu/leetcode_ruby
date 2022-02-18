/*
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
*/

class Solution {
    List<List<Integer>> combos = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        find_combos(0, target, candidates, new LinkedList<>());
        return combos;
    }
    
    void find_combos(int i, int target, int[] candidates, LinkedList<Integer> path) {
        if (target == 0) {
            combos.add((List<Integer>) path.clone());
            return;
        }
        if (i == candidates.length || target < candidates[i]) return;
        path.addLast(candidates[i]);
        find_combos(i, target - candidates[i], candidates, path);
        path.removeLast();
        
        find_combos(i + 1, target, candidates, path);
    }
}

