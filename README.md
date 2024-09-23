[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lPjPSoOJ)
# 3D Transformations Assignment

Welcome to the **3D Transformations** assignment! In this exercise, you will implement a Python class that performs various 3D transformations such as translations and rotations. These transformations are fundamental in fields like computer graphics, robotics, and 3D simulations.

## Task Overview

Your task is to implement a class named `Transform3D` that provides methods for applying 3D transformations on points in space. The methods will handle:

1. **Translation**: Moving points along the x, y, and z axes.
2. **Rotation**: Rotating points around the x, y, and z axes.
3. **Transformation Matrix**: Applying a general 3D transformation using a transformation matrix.

## Assignment Details

You are required to implement the following methods in the `Transform3D` class inside the `transform3d.py` file.

### 1. `translate(point, offset) (5 points)`

- **Input**:
  - `point`: A 3D point represented as a NumPy array, e.g., `[x, y, z]`.
  - `offset`: The translation offset for the x, y, and z axes, represented as a NumPy array.
  
- **Output**: The translated point as a NumPy array.

### 2. `rotate_x(point, angle) (5 points)`

- **Input**:
  - `point`: A 3D point represented as a NumPy array.
  - `angle`: The rotation angle (in degrees) around the x-axis.
  
- **Output**: The rotated point as a NumPy array.

### 3. `rotate_y(point, angle) (5 points)`

- **Input**:
  - `point`: A 3D point represented as a NumPy array.
  - `angle`: The rotation angle (in degrees) around the y-axis.
  
- **Output**: The rotated point as a NumPy array.

### 4. `rotate_z(point, angle) (5 points)`

- **Input**:
  - `point`: A 3D point represented as a NumPy array.
  - `angle`: The rotation angle (in degrees) around the z-axis.
  
- **Output**: The rotated point as a NumPy array.

### 5. `apply_transformation(point, transformation_matrix) (5 points)`

- **Input**:
  - `point`: A 3D point represented as a NumPy array.
  - `transformation_matrix`: A 4x4 transformation matrix.
  
- **Output**: The transformed point as a NumPy array.

> **Hint:** You will likely need to convert the point into **homogeneous coordinates** to apply the transformation matrix.

### 6. `Transforming Points Between Coordinate Frames (25 points)`
![Coordinate Frames](image/frames.png)
Given three coordinate frames `{A}`, `{B}`, and `{C}` as shown in the figure, the transformation between these frames can be modeled as translations and rotations in 3D space.

### Assumptions

1. The point **p<sub>A</sub> = [x<sub>A</sub>, y<sub>A</sub>, z<sub>A</sub>]** is represented in frame {A}.
2. The origin of frame {B} is translated from the origin of frame {A} by the vector **t<sub>A→B</sub> = [dx, dy, dz]**.
3. Frame {C} is rotated relative to frame {B} by an angle **θ** around the Z-axis.
4. The point **p<sub>B</sub> = [x<sub>B</sub>, y<sub>B</sub>, z<sub>B</sub>]** is rotated into frame {C}.

## Task

Using the provided `Transform3D` class, calculate the final position of the point **p<sub>C</sub>** in frame {C}.

### 7. `Analyzing and Applying a Transformation Matrix in 3D Space (25 points)`
You are given two coordinate frames, `{A}` and `{B}`, along with a transformation matrix that represents both rotation and translation from frame `{A}` to frame `{B}`.

### Coordinate Frames and Transformation

1. A point in frame `{A}` is represented as **p<sub>A</sub> = [x<sub>A</sub>, y<sub>A</sub>, z<sub>A</sub>]**.
2. The transformation matrix **T<sub>A→B</sub>** includes:
   - A rotation around the Z-axis by 30°
   - A translation vector **[dx, dy, dz]** which moves the point by 1 unit in the X direction, 2 units in the Y direction, and 3 units in the Z direction.
### Tasks

1. **Analyze the Components of the Transformation Matrix:**
   - Break down the matrix into its rotation and translation components.
   - Verify the rotation matrix for a 30° rotation around the Z-axis.
   - Confirm the translation vector.

2. **Calculate the New Position of the Point in Frame `{B}`:**
   - Use the `apply_transformation` method of the `Transform3D` class to determine the new coordinates of the point **p<sub>B</sub>** in frame `{B}`.
   
3. **Apply the Transformation to the Point:**
   - Apply the transformation to the point **p<sub>A</sub> = [4, 2, 7]** and determine its coordinates in frame `{B}`.
