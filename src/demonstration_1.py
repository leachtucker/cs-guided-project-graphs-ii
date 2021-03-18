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
    # Your code here
    visited = set()

    for row in range(len(image)):
        for col in range(len(image[row])):
            vert = (row, col)
            old_color = image[row][col]

            # If we've already visited this vert, let's skip it
            if vert in visited:
                continue

            # Add the current vert to the visited dict
            visited.add(vert)

            # Find the neighbors of the vert
            neighbors = get_neighbors(image, row, col, old_color)

            # Color the current vert were on
            if len(neighbors) > 0:
                image[row][col] = new_color

            # For each neighbor in
            while len(neighbors) > 0:
                v2 = neighbors.pop(0)

                # If we've already visited this vert, let's skip it
                if v2 in visited:
                    continue

                visited.add(v2)
                image[v2[0]][v2[1]] = new_color

                for j in get_neighbors(image, v2[0], v2[1], old_color):
                    neighbors.append(j)



    return image

print(flood_fill(image, 1, 1, 2))