from stl import mesh
import math
import numpy
import numpy as np

import sys

# Take a look at https://pypi.org/project/numpy-stl/

def cube_generation_by_extending_objects():
  # Create 3 faces of a cube
  data = numpy.zeros(6, dtype=mesh.Mesh.dtype)

  # Top of the cube
  data['vectors'][0] = numpy.array([[0, 1, 1],
                                    [1, 0, 1],
                                    [0, 0, 1]])
  data['vectors'][1] = numpy.array([[1, 0, 1],
                                    [0, 1, 1],
                                    [1, 1, 1]])
  # Right face
  data['vectors'][2] = numpy.array([[1, 0, 0],
                                    [1, 0, 1],
                                    [1, 1, 0]])
  data['vectors'][3] = numpy.array([[1, 1, 1],
                                    [1, 0, 1],
                                    [1, 1, 0]])
  # Left face
  data['vectors'][4] = numpy.array([[0, 0, 0],
                                    [1, 0, 0],
                                    [1, 0, 1]])
  data['vectors'][5] = numpy.array([[0, 0, 0],
                                    [0, 0, 1],
                                    [1, 0, 1]])

  # Since the cube faces are from 0 to 1 we can move it to the middle by
  # substracting .5
  data['vectors'] -= .5

  cube_back = mesh.Mesh(data.copy())
  cube_front = mesh.Mesh(data.copy())

  # Rotate 90 degrees over the X axis followed by the Y axis followed by the
  # X axis
  cube_back.rotate([0.5, 0.0, 0.0], math.radians(90))
  cube_back.rotate([0.0, 0.5, 0.0], math.radians(90))
  cube_back.rotate([0.5, 0.0, 0.0], math.radians(90))

  cube = mesh.Mesh(numpy.concatenate([
      cube_back.data.copy(),
      cube_front.data.copy(),
  ]))

  # Write the mesh to file "cube.stl"
  cube.save('cube.stl')

def cube_generation(sizex=1, sizey=1, sizez=1):

  sizex = 0.5 * sizex
  sizey = 0.5 * sizey
  sizez = 0.5 * sizez

  # Define the 8 vertices of the cube
  vertices = np.array([\
      [-sizex, -sizey, -sizez],
      [+sizex, -sizey, -sizez],
      [+sizex, +sizey, -sizez],
      [-sizex, +sizey, -sizez],
      [-sizex, -sizey, +sizez],
      [+sizex, -sizey, +sizez],
      [+sizex, +sizey, +sizez],
      [-sizex, +sizey, +sizez]])
  # Define the 12 triangles composing the cube
  faces = np.array([\
      [0,3,1],
      [1,3,2],
      [0,4,7],
      [0,7,3],
      [4,5,6],
      [4,6,7],
      [5,1,2],
      [5,2,6],
      [2,3,6],
      [3,7,6],
      [0,1,5],
      [0,5,4]])

  # Create the mesh
  cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
  for i, f in enumerate(faces):
      for j in range(3):
          cube.vectors[i][j] = vertices[f[j],:]

  # Write the mesh to file "cube.stl"
  cube.save('cube.stl')

sizex = sizey = sizez = 1

if len(sys.argv) > 1:
  sizex = float(sys.argv[1])
if len(sys.argv) > 2:
  sizey = float(sys.argv[2])
if len(sys.argv) > 3:
  sizez = float(sys.argv[3])

cube_generation(sizex, sizey, sizez)