=begin
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
=end

# @param {Integer[][]} buildings
# @return {Integer[][]}
def get_skyline(buildings)
    n = buildings.length
    if n == 0
        return []
    end
    if n == 1
        x_start, x_end, y = buildings[0]
        return [[x_start, y], [x_end, 0]]
    end
    left_skyline = get_skyline(buildings[0...(n/2)])
    right_skyline = get_skyline(buildings[(n/2)..-1])
    
    return merge_skylines(left_skyline, right_skyline)
end

def merge_skylines(left, right)
    n_l = left.length
    n_r = right.length
    p_l = p_r = 0
    curr_y = left_y = right_y = 0
    output = []
    
    while p_l < n_l && p_r < n_r
        point_l, point_r = left[p_l], right[p_r]
        if point_l[0] < point_r[0]
            x, left_y = point_l
            p_l += 1
        else
            x, right_y = point_r
            p_r += 1
        end
        max_y = [left_y, right_y].max
        if curr_y != max_y
            update_output(output, x, max_y)
            curr_y = max_y
        end
    end
    
    append_skyline(output, left, p_l, n_l, curr_y)
    append_skyline(output, right, p_r, n_r, curr_y)
    
    return output
end

def update_output(output, x, y)
    if output.empty? || output[-1][0] != x
        output.push([x,y])
    else
        output[-1][1] = y
    end
end

def append_skyline(output, skyline, p, n, curr_y)
   while p < n
       x, y = skyline[p]
       p += 1
       if curr_y != y
           update_output(output, x, y)
           curr_y = y
       end
   end
end