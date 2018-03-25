"""
:type grid: List[List[int]]
:rtype: int

4x4 matrix
looking from top or bottom, the highest values in each column
looking from left or right, the highest values in each row

gridold = [ [3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0] ]    top or bottom : [9, 4, 8, 7]        left or right : [8, 7, 9, 3]

find the new grid without affecting the selected heights (top or bottom) and (left or right)

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]      then the sum of the increased change of height is : 35


"""

# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35

def maxIncreaseKeepingSkyline(grid):
    rows_max = [0] * len(grid)
    cols_max = [0] * len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rows_max[i] = max(rows_max[i], grid[i][j])
            cols_max[j] = max(cols_max[j], grid[i][j])

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res += min(rows_max[i], cols_max[j]) - grid[i][j]

    return res

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))