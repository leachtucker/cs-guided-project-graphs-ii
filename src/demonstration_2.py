"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def get_neighbors(graph, start_row, start_col):
  neighbors = []

  # Find neighbors of the vert at start_row,start_col

  # Up
  if start_row-1 >= 0 and graph[start_row-1][start_col] == "1":
      neighbors.append((start_row-1, start_col))

  # Down
  if start_row+1 < len(graph) and graph[start_row+1][start_col] == "1":
      neighbors.append((start_row+1, start_col))

  # Left
  if start_col-1 >= 0 and graph[start_row][start_col-1] == "1":
      neighbors.append((start_row, start_col-1))

  # Right
  if start_col+1 < len(graph[start_row]) and graph[start_row][start_col+1] == "1":
      neighbors.append((start_row, start_col+1))

  return neighbors

def dft_helper(grid, start_row, start_col, visited):
  stack = []

  stack.append((start_row, start_col))
  while len(stack) > 0:
    currRow, currCol = stack.pop()

    # If we've already visited, let's move on
    if (currRow, currCol) in visited:
      continue

    # Add to our visited set
    visited.add((currRow, currCol))

    # Traverse the neighbors
    for neighbor in get_neighbors(grid, currRow, currCol):
      stack.append(neighbor)


def numIslands(grid):
  # Your code here
  visited = set()
  islandCounter = 0

  for row in range(len(grid)):
    for col in range(len(grid[row])):
      currVertVal = grid[row][col]

      if currVertVal == '1' and (row, col) not in visited:
        dft_helper(grid, row, col, visited)
        islandCounter += 1

  return islandCounter

print(numIslands(grid))
print(numIslands(grid2))
