import numpy as np
import pyvista as pv
# Create two quad elements, as follows:
#
# Coordinates:                
# y ^                   
#   |
# 4 *----*----*         
#   |    |    |         
#   |    |    |                    
# 2 *----*----*         
#   |    |    |         
#   |    |    |         
#   *----*----*--->     
#   0    1    2   x     
#

# This will have a total of 6 vertices (points), with the coordinates as follows:
# y ^                   
#   |
#  (6)--(7)--(8)         
#   |    |    |         
#   |    |    |                     
#  (3)--(4)--(5)         
#   |    |    |         
#   |    |    |         
#  (0)--(1)--(2)-->     
#                 x     
#
points = np.array([[-2, 0, 0],
                   [0, 0, 0],
                   [2, 0, 0],
                   [-2, 2, 0],
                   [0, 2, 0],
                   [2, 2, 0],
                   [-2, 4, 0],
                   [0, 4, 0],
                   [2, 4, 0]], dtype=np.float64 )

npoints = points.shape[0]

# Each quad element is formed by 4 nodes, with the following order
# (see Figure 2 under 
# https://docs.vtk.org/en/latest/design_documents/VTKFileFormats.html#legacy-file-examples )
#
# Quad element:                  
#  (3)--(2)
#   |    |
#   |    |
#  (0)--(1)
# 
# The connectivity of a cell is determined by supplying the indices of the points
# that form the correspoinding quad (in the order described above). 
#
# For example, the first quad is formed by the points 0, 1, 4 and 3. 
# y ^                   
#   |                   
#  (3)--(4)--(5)         
#   |    |    |         
#   |    |    |         
#  (0)--(1)--(2)-->     
#                 x 
#
# The  second quad is formed by the nodes 1, 2, 4 and 5. 
# 
# The cells array is a 1d-array that contains the connectivity of the cells:
# First, the number of indices that corresponds to this type is supplied, and then
# the cell's connectivity:
# [nInd, id_0, id_1, ...,id_(nInd-1) ]
#
cells = np.array([4, 0, 1, 4, 3, # First  quad
                  4, 1, 2, 5, 4,  # Second quad.
                  4, 3, 4, 7, 6,  # Third quad.
                  4, 4, 5, 8, 7  # Fourth quad.
                  ])
# Number of cells
ncells = 4

# All cells are type quad, thus we only define for each
# cell, its correspondign type:
cell_type = pv.CellType.QUAD * np.ones(ncells,dtype=np.int8)

# The grid is created using all the cells
grid = pv.UnstructuredGrid(cells, cell_type, points)

# Define a scalar field 'dcenter' measuring the distance from the center point (0,2,0)
center_point = np.array([0, 2, 0])
dcenter = np.linalg.norm(points - center_point, axis=1)
grid['dcenter'] = dcenter

# Define a vector field 'velocity'
velocity = np.zeros_like(points)
velocity[:, 0] = points[:, 1]   # v_x = y
velocity[:, 1] = -points[:, 0]  # v_y = -x
velocity[:, 2] = 0              # v_z = 0
grid['velocity'] = velocity

# Optionally, plot the grid with scalar field
# grid.plot(scalars='dcenter', show_edges=True, show_grid=True)
grid.save("main_program.vtk")