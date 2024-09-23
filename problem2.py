import numpy as np
from transform import Transform3D

def solving():
    
    # Initialize the transformation matrix
    transform = Transform3D()
    
    # Define the rotation angle in radians
    angle = np.deg2rad(45)
    
    # Define the rotation matrix around the Z-axis
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0,             0,            1]
    ])
    
    # Define the translation vector
    translation_vector = np.array([1, 2, 3])
    
    # Construct the full transformation matrix
    transform_matrix = np.eye(4)  # 4x4 identity matrix
    transform_matrix[:3, :3] = rotation_matrix  # Rotation part
    transform_matrix[:3, 3] = translation_vector  # Translation part
    
    # Apply the transformation to the point pA
    pA = np.array([4, 2, 7, 1])  # Add homogeneous coordinate
    pB_homogeneous = transform_matrix @ pA  # Matrix multiplication
    
    # Return the result as a 3D point in frame B
    return pB_homogeneous[:3]

# Example of running the function and printing the result
if __name__ == "__main__":
    result = solving()
    print("Transformed point pB:", result)
