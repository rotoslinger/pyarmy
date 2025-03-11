# Inverse Matrix Calculation for World to Tile Conversion

## Theory

Given a **2×2 transformation matrix** \( A \):

\[
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\]

The inverse of this matrix, \( A^{-1} \), is computed by swapping the diagonal elements and negating the off-diagonal elements:

\[
A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
\]

where the determinant \( \det(A) \) is given by:

\[
\det(A) = a \cdot d - b \cdot c
\]

Thus, the inverse elements are:

\[
\text{inv\_a} = d, \quad \text{inv\_b} = -b, \quad \text{inv\_c} = -c, \quad \text{inv\_d} = a
\]

---

## Application in Tile Mapping

In a tile-based system, the tile dimensions are calculated as:

\[
\text{tile\_width} = (x \cdot 0.5 \cdot \text{width}) + (y \cdot -0.5 \cdot \text{width})
\]

\[
\text{tile\_height} = (x \cdot 0.25 \cdot \text{height}) + (y \cdot 0.25 \cdot \text{height})
\]

From this, we identify matrix components:

\[
A = \begin{bmatrix} 0.5 \cdot \text{width} & 0.25 \cdot \text{height} \\ -0.5 \cdot \text{width} & 0.25 \cdot \text{height} \end{bmatrix}
\]

The determinant is:

\[
\det(A) = (0.5 \cdot \text{width} \cdot 0.25 \cdot \text{height}) - (-0.5 \cdot \text{width} \cdot 0.25 \cdot \text{height})
\]

The reciprocal of the determinant is:

\[
\text{inv\_det} = \frac{1}{\det(A)}
\]

Using this, the inverse matrix elements are computed as:

\[
\text{inv\_a} = 0.25 \cdot \text{height} \cdot \text{inv\_det}
\]

\[
\text{inv\_b} = 0.5 \cdot \text{width} \cdot \text{inv\_det}
\]

\[
\text{inv\_c} = -0.25 \cdot \text{height} \cdot \text{inv\_det}
\]

\[
\text{inv\_d} = -0.5 \cdot \text{width} \cdot \text{inv\_det}
\]

---

## Python Implementation

```python
'''
###############################################################
Inverse matrix calculation for world to tile conversion

Theory:

If you have Matrix A:
     _     _
A  =| a,  b |
    | c,  d |
     ‾     ‾
Invert the diagonals and negate from bottom left to upper right:
     _     _
A⁻¹=| d, -b |
    | -c, a |
     ‾     ‾
Calculate the determinant:
a * d - b * c

newly inverted a,b,c,d:
inv_a = d
inv_b = -b
inv_c = -c
inv_d = a

Practice: 
in your tilemap, you are creating your tile dimensions this way:

tile_width  = (x * 0.5 * width) + (y * -0.5 * width)
tile_height = (x * 0.25 * height) + (y * 0.25 * height)

lets break this down into the

getting the parts of the determinant while factoring in the tile-map scaling
a ---  0.5  * width 
b ---  0.25 * height
c --- -0.5  * width
d ---  0.25 * height

final parts of the determinant
determinant = a * d - b * c

get the reciprocal of the determinant
inverse determinant = 1 / det

###############################################################
'''

# Define width and height of the tiles
tile_width = 64  # Example value
tile_height = 32  # Example value

# Calculate determinant
inv_det = 1 / ((0.5 * tile_width * 0.25 * tile_height) - (-0.5 * tile_width * 0.25 * tile_height))

# Compute the inverse matrix elements
inv_a = 0.25 * tile_height * inv_det
inv_b = 0.5 * tile_width * inv_det
inv_c = -0.25 * tile_height * inv_det
inv_d = -0.5 * tile_width * inv_det

# Example shadow position in screen space
shadow_pos = (120, 80)  # Example coordinates

# Convert screen-space movement to tile-space
cam_pos_x_tile = int((inv_a * shadow_pos[0] + inv_b * shadow_pos[1]) / 16)
cam_pos_y_tile = int((inv_c * shadow_pos[0] + inv_d * shadow_pos[1]) / 16)

print(f"Tile Position: ({cam_pos_x_tile}, {cam_pos_y_tile})")
