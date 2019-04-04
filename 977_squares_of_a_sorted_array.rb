=begin
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

=end

# @param {Integer[]} a
# @return {Integer[]}
def sorted_squares(a)
    n = a.length
    j = 0
    while j < n && a[j] < 0
        j += 1
    end
    i = j - 1
    
    ans = []
    while 0 <= i && j < n
        if a[i]**2 < a[j]**2
            ans.push(a[i]**2)
            i -= 1
        else
            ans.push(a[j]**2)
            j += 1
        end
    end
    while i >= 0
        ans.push(a[i]**2)
        i -= 1
    end
    while j < n
        ans.push(a[j]**2)
        j += 1
    end
    
    ans
end
