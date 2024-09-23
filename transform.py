import numpy as np

class Transform3D:
    def __init__(self):
        pass
    
    def translate(self, point, offset):
        """
        Translate a point in 3D space by a given offset.
        
        Args:
            point (list or tuple): The original point as [x, y, z].
            offset (list or tuple): The translation offset as [dx, dy, dz].
            
        Returns:
            numpy.ndarray: Translated point as [new_x, new_y, new_z].
        """
        point = np.array(point)
        offset = np.array(offset)
        
        translated_point = point + offset
        return translated_point
    
    def rotate_x(self, point, angle_degrees):
        """
        Rotate a point around the X-axis by a given angle.
        
        Args:
            point (list or tuple): The original point as [x, y, z].
            angle_degrees (float): The rotation angle in degrees.
            
        Returns:
            numpy.ndarray: The rotated point as [new_x, new_y, new_z].
        """
        angle_radians = np.radians(angle_degrees)
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(angle_radians), -np.sin(angle_radians)],
            [0, np.sin(angle_radians), np.cos(angle_radians)]
        ])
        
        point = np.array(point)
        rotated_point = Rx @ point
        return rotated_point
    
    def rotate_y(self, point, angle_degrees):
        """
        Rotate a point around the Y-axis by a given angle.
        
        Args:
            point (list or tuple): The original point as [x, y, z].
            angle_degrees (float): The rotation angle in degrees.
            
        Returns:
            numpy.ndarray: The rotated point as [new_x, new_y, new_z].
        """
        angle_radians = np.radians(angle_degrees)
        Ry = np.array([
            [np.cos(angle_radians), 0, np.sin(angle_radians)],
            [0, 1, 0],
            [-np.sin(angle_radians), 0, np.cos(angle_radians)]
        ])
        
        point = np.array(point)
        rotated_point = Ry @ point
        return rotated_point
    
    def rotate_z(self, point, angle_degrees):
        """
        Rotate a point around the Z-axis by a given angle.
        
        Args:
            point (list or tuple): The original point as [x, y, z].
            angle_degrees (float): The rotation angle in degrees.
            
        Returns:
            numpy.ndarray: The rotated point as [new_x, new_y, new_z].
        """
        angle_radians = np.radians(angle_degrees)
        Rz = np.array([
            [np.cos(angle_radians), -np.sin(angle_radians), 0],
            [np.sin(angle_radians), np.cos(angle_radians), 0],
            [0, 0, 1]
        ])
        
        point = np.array(point)
        rotated_point = Rz @ point
        return rotated_point
    
    def apply_transformation(self, point, transformation_matrix):
        """
        Apply a transformation matrix to a point in 3D space.
        
        Args:
            point (list or tuple): The original point as [x, y, z].
            transformation_matrix (numpy.ndarray): A 4x4 transformation matrix.
            
        Returns:
            numpy.ndarray: The transformed point as [new_x, new_y, new_z].
        """
        point = np.array(point + [1])  # Convert to homogeneous coordinates
        
        transformed_point = transformation_matrix @ point
        return transformed_point[:3]  # Return the x, y, z coordinates only
