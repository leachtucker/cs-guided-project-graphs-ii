"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

```plaintext

Input:
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr = 1, sc = 1, newColor = 2

Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
]

Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```

Notes:

- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

def get_neighbors(graph, start_row, start_col, color):
    neighbors = []

    # Find neighbors of the vert at start_row,start_col

    # Up
    if start_row-1 >= 0 and graph[start_row-1][start_col] == color:
        neighbors.append((start_row-1, start_col))

    # Down
    if start_row+1 < len(graph) and graph[start_row+1][start_col] == color:
        neighbors.append((start_row+1, start_col))

    # Left
    if start_col-1 >= 0 and graph[start_row][start_col-1] == color:
        neighbors.append((start_row, start_col-1))

    # Right
    if start_col+1 < len(graph[start_row]) and graph[start_row][start_col+1] == color:
        neighbors.append((start_row, start_col+1))

    return neighbors

print(get_neighbors(image, 1, 1, 1))

def dft_helper(grid, start_row, start_col, visited, new_color):
  stack = []
  old_color = grid[start_row][start_col]

  stack.append((start_row, start_col))
  while len(stack) > 0:
    currRow, currCol = stack.pop()

    # If we've already visited, let's move on
    if (currRow, currCol) in visited:
      continue

    # Add to our visited set
    visited.add((currRow, currCol))

    # Eval/change color
    grid[currRow][currCol] = new_color

    # Traverse the neighbors
    for neighbor in get_neighbors(grid, currRow, currCol, old_color):
      stack.append(neighbor)


def flood_fill(image, start_row, start_col, new_color):
    """
    Inputs:
    image -> List[List[int]]
    start_row -> int
    start_col -> int
    new_color -> int

    Output:
    List[List[int]]
    """
    visited = set()
    color_to_fill = image[0][0]

    dft_helper(image, 0, 0, visited, new_color)

    return image

print(flood_fill(image, 1, 1, 2))